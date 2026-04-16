@dataclass(frozen=True)
class OOBManagementAddNetworkServiceCmd(AddNetworkServiceCmd):
    prefix: IPv4Network

    def execute(self, manager: NetworkServiceManager) -> None:
        network_service = NetworkServiceCatalog.OOB_MANAGEMENT.value

        # Step 1 - Add management prefix
        manager.resources.execute(
            PrefixAddNetworkResourceCmd(
                prefix=PrefixNetworkResource(
                    network_service=network_service,
                    prefix=self.prefix,
                    role=PrefixRole.OOB_MANAGEMENT,
                )
            )
        )

        # Step 2 - Allocate management interfaces
        for device in manager.resources.devices:
            manager.resources.execute(
                InterfaceAllocateNetworkResourceCmd(
                    network_service=network_service,
                    device=device,
                    role=InterfaceRole.OOB_MANAGEMENT,
                    all=True,
                )
            )

        # Step 3 - Allocate IP addresses for management interfaces
        for device in manager.resources.devices:
            oob_interfaces = manager.resources.get_interface_allocations(
                network_service=network_service,
                device=device,
            )

            while oob_interfaces:
                manager.resources.execute(
                    IPAddressAllocateNetworkResourceCmd(
                        network_service=network_service,
                        role=PrefixRole.OOB_MANAGEMENT,
                    )
                )
                oob_interfaces.pop()

        # Step 4 - Allocate default gateway IP address
        manager.resources.execute(
            IPAddressAllocateNetworkResourceCmd(
                network_service=network_service,
                role=PrefixRole.OOB_MANAGEMENT,
                last=True,
            )
        )

        # Step 5 - Configure OOB Management network service
        prefix = manager.resources.get_prefix_allocation(role=PrefixRole.OOB_MANAGEMENT)
        addresses = [address.address for address in prefix.allocations.addresses]
        default_gateway = addresses.pop()
        netmask = prefix.prefix.netmask
        prefix_length = str(prefix.prefix.prefixlen)

        devices = []
        for device in manager.resources.devices:
            _device = manager.resources.get_device(name=device)
            template = (
                OOBManagementDeviceNetworkServiceTemplate.SWITCH.value
                if _device.role == DeviceRole.FASI
                else OOBManagementDeviceNetworkServiceTemplate.ROUTER.value
            )

            interface_allocations = manager.resources.get_interface_allocations(
                device=device, network_service=network_service
            )

            interfaces = []
            while interface_allocations:
                name = interface_allocations.pop(0).name
                address = addresses.pop(0)
                interfaces.append(
                    OOBManagementInterface(
                        name=name,
                        address=address,
                        netmask=netmask,
                        prefix_length=prefix_length,
                    )
                )

            devices.append(
                OOBManagementNetworkServiceDevice(
                    name=device,
                    template=template,
                    default_gateway=default_gateway,
                    interfaces=interfaces,
                )
            )

        manager.add_network_service(
            NetworkService(
                name=NetworkServiceCatalog.OOB_MANAGEMENT.value,
                devices=devices
            )
        )

        manager.commit(
            msg=CommitMessage(f"sni-lite add oob-management {self.id}, {self.prefix}")
        )


class NetworkServiceManager:

    def __init__(
        self, repo_dir: str | None = None, repo_url: str | None = None
    ) -> None:
        self._repo_dir = repo_dir
        self._repo_url = repo_url
        self._path: Path | None = None
        self._repository: Repository | None = None
        self._resources: NetworkResourceManager | None = None
        self._network_service: RootNetworkService | None = None
        self._pending_renders: list[NetworkService] = []
