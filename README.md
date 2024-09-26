# Network as a Service (NaaS) Automation Platform

## Introduction

In today's rapidly evolving digital landscape, efficient network management is critical for maintaining scalable and resilient IT infrastructures. Traditional management methods, while providing control, often struggle to keep up with the complexity and speed required in modern environments. This presentation explores the challenges of classical network management and proposes the **Network as a Service (NaaS) Automation Platform** as a forward-thinking solution designed to address these issues. The NaaS Automation Platform offers a blueprint for automating and optimizing the full lifecycle of network services, ensuring scalability, consistency, and operational efficiency.

## The Challenges of Classical Network Management

While traditional network management methods—such as manual configurations via the Command Line Interface (CLI)—have long provided granular control, they fall short in addressing the demands of modern networks. As organizations scale and adapt to increasingly complex infrastructures, these manual approaches present several significant challenges:

- **Error-Prone Processes**: Relying on human input for device configuration often results in misconfigurations, leading to network inconsistencies, service disruptions, and increased downtime.
- **Time-Consuming Operations**: Configuring and maintaining a large number of devices individually through CLI is labor-intensive and inefficient, particularly in fast-paced, dynamic environments where rapid changes are necessary.
- **Scalability Limitations**: As network infrastructures grow in size and complexity, traditional manual methods struggle to maintain uniformity and reliability across devices, leading to configuration drift and operational inefficiencies.
- **Limited Collaboration and Visibility**: Without version control or collaboration tools, network changes are often siloed, making it difficult for teams to work together or track configuration history, thus increasing the risk of errors.

These limitations highlight the need for a more streamlined, automated approach to network management—one that reduces manual intervention and supports the scalability, agility, and reliability required by modern IT infrastructures.

## How Network Automation Solves These Challenges

To overcome the limitations of traditional network management, **network automation** provides a modern solution that simplifies and streamlines the process of configuring, managing, and monitoring network devices. By replacing manual, error-prone processes with automated workflows, network automation offers several key advantages:

- **Minimizing Human Error**: By automating configuration tasks, the potential for human errors—such as misconfigurations or inconsistencies—is greatly reduced. Automation ensures that changes are applied uniformly across all devices, leading to a more stable and reliable network environment.
  
- **Improving Efficiency**: Automation drastically reduces the time and effort required to configure and maintain large-scale networks. Engineers can focus on strategic, higher-level tasks while repetitive, time-consuming configuration work is handled automatically, speeding up deployment times and reducing operational overhead.

- **Enabling Scalability**: As networks grow, automation ensures that devices are managed consistently and efficiently, eliminating the scalability limitations of manual processes. Automated systems can handle large numbers of devices without sacrificing reliability, allowing networks to expand seamlessly.

- **Enhancing Collaboration and Visibility**: Automation platforms often integrate version control and collaboration tools, allowing teams to work together more effectively. By tracking changes and maintaining a history of configurations, these tools provide greater transparency and control, reducing the risk of conflicting updates or overlooked errors.

In short, network automation provides the agility, scalability, and consistency required to manage modern networks efficiently, positioning it as a critical solution for overcoming the challenges of classical network management.

## Introducing the NaaS Automation Platform

In response to the growing challenges of classical network management, the **Network as a Service (NaaS) Automation Platform** offers a comprehensive solution to address the complexity, scale, and operational demands of modern networks. The NaaS platform automates and streamlines the full lifecycle of network services across diverse environments, including Enterprise, Data Centers, Cloud, and Service Provider networks.

The NaaS platform introduces a unified approach to managing network infrastructure by applying modern practices such as **Infrastructure as Code (IaC)** and **GitOps**. These principles ensure that all network configurations are maintained in version-controlled repositories, enabling consistent, repeatable, and traceable network changes. By integrating automation into every step of the network service lifecycle—from provisioning to monitoring—NaaS aims to enhance scalability, improve reliability, and reduce manual intervention.

At its core, the NaaS platform leverages the best practices of **NetDevOps**, combining the efficiency of DevOps workflows with the specific needs of network operations. By automating routine tasks, minimizing human error, and supporting collaborative workflows, NaaS empowers organizations to achieve operational excellence, offering an efficient, scalable, and consistent method for managing network services across a variety of environments.

## Key Concepts

### What is Network Automation?

Network automation is the practice of using software to automate the configuration, management, and monitoring of network devices. By automating these processes, organizations reduce the need for manual intervention, which minimizes human errors, speeds up network changes, and improves overall operational efficiency. Automation allows networks to scale more easily and adapt to dynamic environments, supporting faster deployment and consistent management of network infrastructure.

### What is a Platform?

A platform refers to an integrated system of tools and technologies that communicate through **APIs (Application Programming Interfaces)** to achieve a specific goal. In the context of the **NaaS Automation Platform**, it brings together various network automation, monitoring, and task management tools into a cohesive ecosystem. By doing so, it enables seamless workflows for automating the entire network service lifecycle—from provisioning to monitoring—ensuring efficiency and consistency across all network environments.

### What is Infrastructure as Code (IaC)?

Infrastructure as Code (IaC) is a methodology where network and infrastructure configurations are treated as code. This means defining network settings in files, stored in version control systems like Git, which allows for automated and repeatable deployment of configurations. IaC ensures that infrastructure is consistent across environments, reduces manual errors, and makes network changes easier to track, validate, and deploy.

### What is GitOps?

GitOps is an operational model that uses Git as the single source of truth for infrastructure and application configurations. With GitOps, changes are tracked, tested, and applied through **CI/CD pipelines**, ensuring that infrastructure deployments are automated and repeatable. This method provides transparency and traceability, allowing teams to continuously monitor and apply configuration changes reliably and in a controlled manner.

### What is NetDevOps?

NetDevOps extends the principles of DevOps—collaboration, automation, and continuous delivery—into the world of network operations. It applies the same processes used in software development, such as version control, testing, and automation, to network configuration and management. By treating network automation as a software development process, NetDevOps enables faster, more reliable network changes and fosters collaboration between network and operations teams.

### What is CI/CD?

**CI/CD** stands for **Continuous Integration** and **Continuous Delivery/Deployment**. These are automation practices used to speed up the delivery of network changes by integrating and testing code in a continuous manner. In the context of the **NaaS Automation Platform**, CI/CD ensures that network configurations are automatically validated and deployed to the production environment in a reliable, error-free way. It enables faster updates to the network infrastructure while maintaining high standards of quality and consistency.

### What are CI/CD Pipelines?

CI/CD pipelines are automated workflows that manage the continuous integration, testing, and deployment of network configurations. In the **NaaS Automation Platform**, these pipelines validate network changes before they are deployed, ensuring that every configuration is thoroughly tested and meets the required standards. CI/CD pipelines enable organizations to maintain a continuous loop of improvement, monitoring, and feedback for their network operations.

## The CI/CD Loop

The NaaS Automation Platform follows a Continuous Integration and Continuous Delivery (CI/CD) loop to automate the full lifecycle of network services. Each phase of the loop ensures that network changes are implemented efficiently, consistently, and with minimal disruption to the network:

1. **Plan**: Define network changes, requirements, and high-level designs using collaborative tools. This phase establishes the goals and scope of the changes, providing a clear direction for automation and ensuring that all stakeholders are aligned.

2. **Code**: Develop and configure network infrastructure using Infrastructure as Code (IaC) principles. Network configurations are written as code, ensuring they are version-controlled, traceable, and consistent across environments.

3. **Build**: The CI/CD pipeline creates a virtual testing environment where the proposed network changes can be safely simulated. This environment mirrors the production network, allowing engineers to validate configurations without impacting live services.

4. **Test**: In this phase, network configurations are tested within the virtual testbed. The goal is to ensure the changes meet performance standards, validate connectivity, and check for errors before deployment to the live network.

5. **Release**: After the configurations pass all necessary tests, a release is prepared. The release is reviewed, approved, and marked for deployment, ensuring that the network changes are ready for production.

6. **Deploy**: The validated configurations are rolled out to the live network. The deployment is automated to ensure consistent and accurate application of the changes, with minimal manual intervention and disruption to existing services.

7. **Operate**: Once deployed, the network’s performance is monitored in real-time. This phase ensures that the changes are functioning as expected, and any issues that arise are detected and addressed promptly.

8. **Monitor and Feedback**: Continuous monitoring collects performance data and telemetry from the deployed configurations. This feedback is analyzed and used to inform future network changes, driving a continuous improvement loop for network operations.


## NaaS Automation Platform Core Technologies and Their Roles

The NaaS Automation Platform integrates a suite of core technologies, each playing a pivotal role in the automation and management of network services:

### Nautobot

- **Role**: Store and manage network data, configurations, and inventory.
- **Features**: Extensible data models, powerful APIs, and integration capabilities with various network automation tools.

Nautobot is an open-source network automation platform designed to act as a **Source of Truth (SoT)** for network operations. It provides a centralized repository for all network-related data, such as device configurations, inventory, and topology data. Its flexible and extensible data models allow it to scale according to the needs of any organization. With robust APIs, Nautobot facilitates integration with other automation and orchestration tools, making it an essential component for modern network automation workflows.

Within the NaaS Automation Platform, Nautobot plays a central role by collecting and maintaining all the necessary data to build network configurations. It integrates seamlessly with other tools in the platform to ensure that all network configurations are up-to-date, accurate, and ready for deployment. By acting as the platform's main data repository, Nautobot enables automated network configuration generation, provisioning, and management, supporting the platform’s goal of efficient and scalable network automation.

### Cisco NSO

- **Role**: Provision and manage network devices based on data provided by Nautobot.
- **Features**: Model-driven service orchestration, multi-vendor support, and service lifecycle management.

Cisco Network Services Orchestrator (NSO) is a powerful automation platform designed to provision and manage network devices across diverse network environments. NSO is built around a **model-driven** architecture, meaning it uses network models (YANG) to abstract device-specific details, making it possible to manage a wide range of vendors and technologies through a unified interface. NSO offers **multi-vendor support**, ensuring compatibility with different device types and technologies while also enabling **service lifecycle management**—from initial provisioning to updates and decommissioning. This allows for highly reliable, automated operations across a variety of network devices and platforms, reducing manual intervention and enhancing scalability.

In the NaaS Automation Platform, Cisco NSO works closely with Nautobot to handle device-level configuration and provisioning. Nautobot pre-computes all the necessary device configurations and sends them to Cisco NSO over its **northbound RESTCONF API**. NSO then takes these configurations and distributes them to individual devices using its **Network Element Drivers (NEDs)**, which utilize **NETCONF, RESTCONF, SNMP, or CLI** to interface with the devices. This workflow ensures that all network configurations are deployed consistently and efficiently, leveraging Cisco NSO’s robust orchestration capabilities to manage complex, multi-vendor networks.

### Service Portal

- **Role**: Customer-facing portal for requesting network services.
- **Features**: Self-service interface, request tracking, and integration with automation processes.

The **Service Portal** acts as the main interface for end-users to request network services in an automated and streamlined manner. It provides a self-service platform where users can submit service requests, monitor their status, and interact with the underlying network infrastructure without needing direct support from network engineers. The portal is built with intuitive user interaction features that simplify complex processes like network provisioning, ensuring ease of use for both technical and non-technical users.

Within the **NaaS Automation Platform**, all service requests submitted through the Service Portal are forwarded to **Nautobot** for processing. Nautobot analyzes each request, assessing the required infrastructure resources—such as IP addresses, subnets, and devices—and determines what is available or needs to be provisioned. By automating the resource allocation and provisioning steps, the Service Portal ensures that services are efficiently deployed without manual intervention, speeding up delivery times and maintaining consistency across the network.

### Jira/Confluence

- **Role**: Coordination, task tracking, and documentation for human-to-human interactions.
- **Features**: Task management, issue tracking, cross-team collaboration, and centralized documentation.

**Jira** and **Confluence** are essential tools for managing coordination and documentation within the NaaS Automation Platform. **Jira** facilitates task management, allowing teams to assign, track, and manage activities related to network service delivery. It ensures that all tasks are organized, deadlines are met, and dependencies are clear. Meanwhile, **Confluence** serves as the central repository for documentation, including High-Level Designs (HLDs), Low-Level Designs (LLDs), and all other resources related to network automation. It provides a collaborative environment where teams can document processes, share knowledge, and ensure that everyone involved in the network lifecycle has access to up-to-date information.

In the **NaaS Automation Platform**, **Nautobot** integrates seamlessly with **Jira** to automate the creation of tasks based on service requests. For example, when a new service request is submitted through the **Service Portal**, Nautobot analyzes the request and automatically generates relevant tasks in **Jira** for different departments—such as purchasing, network engineering, and facilities—based on the infrastructure and service requirements. This automated task creation reduces the administrative burden on network teams and ensures that service requests are fulfilled in a timely and coordinated manner. 

### Git/GitHub

- **Role**: Provide version control and a collaborative development environment.
- **Features**: Version control, pull requests, issue tracking, and integration with CI/CD pipelines.

**Git** is a widely-used version control system that allows teams to collaborate on code and manage changes efficiently. Paired with **GitHub**, a cloud-based platform built on Git, it provides additional features such as pull requests, code reviews, issue tracking, and seamless integration with CI/CD pipelines. GitHub is a central hub for managing repositories, enabling teams to work on code simultaneously, track progress, and ensure that changes are deployed in a controlled and traceable manner. It allows engineers to collaborate effectively on network automation workflows, leveraging Git's branching and merging capabilities to maintain consistency and manage complex development cycles.

Within the **NaaS Automation Platform**, **GitHub** plays a crucial role in storing the YAML files that represent network configurations and other automation instructions. **Nautobot** integrates directly with **GitHub** to pull these YAML files, ensuring that all configurations are version-controlled and traceable. When new changes are committed to the GitHub repository, **Nautobot** triggers the appropriate automation workflows to update network devices and services based on the latest configurations. This ensures that network updates are applied consistently, with a clear audit trail of changes, and that configuration management is fully automated across the NaaS platform.

### kea-dhcp-server

- **Role**: Provide DHCP services for network infrastructures.
- **Features**: High performance, extensibility, and rich configuration options.

**kea-dhcp-server** is an open-source, modern DHCP server developed by the Internet Systems Consortium (ISC). It is designed to provide high-performance, scalable, and flexible DHCP services for both IPv4 and IPv6 networks. The kea-dhcp-server supports dynamic IP address allocation, and its extensible architecture allows for custom hooks and configurations tailored to specific network environments. With its REST API, Kea is well-suited for integration with network automation systems, enabling real-time updates and dynamic configuration changes.

In the **NaaS Automation Platform**, **Nautobot** pre-computes the DHCP configurations required for the network and automatically updates the **kea-dhcp-server** when necessary. When DHCP-related objects (such as subnets, leases, or pools) are modified in the platform, Nautobot updates the pre-computed DHCP configuration stored in its database. This configuration is then pushed to the kea-dhcp-server via its REST API, ensuring that the DHCP server always has the most up-to-date configuration without the need for manual intervention. This integration ensures seamless IP address management and reduces the risk of configuration errors across the network.

   ### kea-dns-server

- **Role**: Provide DNS services for dynamic registration of IP addresses and FQDNs.
- **Features**: Automatic DNS registration, high scalability, and support for both IPv4 and IPv6 addressing schemes.

The **kea-dns-server** is a high-performance, scalable DNS server designed to manage DNS name resolution dynamically. It automatically registers and updates DNS records, ensuring that devices on the network are assigned Fully Qualified Domain Names (FQDNs) that are easily discoverable. The server supports both IPv4 and IPv6, providing flexibility and extensibility through its modular architecture. Its ability to scale makes it suitable for networks of all sizes, where maintaining up-to-date DNS records is critical for efficient network operations.

In the **NaaS Automation Platform**, **Nautobot** is responsible for managing and updating DNS records on the **kea-dns-server**. When changes occur in the network, such as new devices being added or IP addresses being reallocated, Nautobot automatically triggers the required updates to ensure that DNS records are accurate and reflect the current state of the network. By automating DNS updates, the platform reduces the need for manual intervention, ensuring that DNS resolution remains consistent and up-to-date.

### Cisco Modeling Labs (CML)

- **Role**: Validate network service changes in a virtual environment.
- **Features**: Virtual network simulation, comprehensive device support, and integration with CI/CD pipelines.

**Cisco Modeling Labs (CML)** is a powerful platform for network simulation and validation. It allows engineers to design, simulate, and test network configurations in a fully virtualized environment. CML supports a wide range of device types and network topologies, making it a versatile tool for creating realistic, scalable network simulations. With its ability to replicate production network environments, CML enables thorough testing and validation of network designs and configurations, ensuring that changes can be confidently rolled out without impacting live services. Its flexibility and device coverage make it an ideal solution for network engineers looking to validate complex, multi-vendor environments.

Within the **NaaS Automation Platform**, **Cisco Modeling Labs (CML)** plays a key role in the testing and validation phase. Before network configuration changes are applied to the production environment, they are tested in a virtual network environment managed by CML. This ensures that all changes—such as device configurations, protocols, and connectivity—are thoroughly vetted in a controlled setting. By integrating with the CI/CD pipeline, CML allows automated deployment of test environments, which reduces the risk of errors and improves the overall reliability of network services. 

### IxNetwork Virtual Edition (VE)

- **Role**: Test and validate network traffic flows.
- **Features**: Comprehensive network testing, virtual and physical traffic validation, and scalability for production environments.

**IxNetwork Virtual Edition (VE)** is a powerful network testing tool that simulates and validates network traffic flows in both virtual and physical environments. Developed by **Keysight Technologies**, IxNetwork VE offers an extensive set of features to test network performance, including the ability to generate high volumes of traffic, measure latency, and validate network functions. The platform supports a wide variety of network protocols, making it versatile for testing complex, multi-vendor networks. With the ability to scale across virtual environments, IxNetwork VE ensures that network configurations and services meet the required performance standards before being deployed in a production environment.

Within the **NaaS Automation Platform**, **IxNetwork Virtual Edition (VE)** is integrated into both testing and production environments to generate and validate network traffic flows. During the testing phase, IxNetwork VE is used to simulate traffic across virtualized network topologies, ensuring that all network changes meet performance and connectivity standards. In production, it validates that the live network can handle real-world traffic patterns and loads. By automating the traffic validation process, IxNetwork VE helps ensure that the NaaS platform delivers high-quality, scalable network services without introducing performance bottlenecks or failures.
   
### Cisco pyATS

- **Role**: Validate network services.
- **Features**: Automated testing, network device interactions, and comprehensive test coverage.

**Cisco pyATS** is an advanced test automation framework that simplifies the validation of network services and configurations. pyATS allows engineers to automate network testing by providing extensive capabilities to interact with network devices, execute commands, and validate their behavior. The framework supports a wide variety of testing scenarios, from basic connectivity checks to complex multi-device interactions, ensuring that all elements of the network are functioning as expected. pyATS also integrates seamlessly with existing automation tools, making it easier to test and validate network changes in both virtual and physical environments.

Within the **NaaS Automation Platform**, **Cisco pyATS** is used during the testing phase to validate network changes before they are applied to production environments. After configurations are deployed in a virtual testbed, pyATS executes automated tests to ensure that all network services—such as routing protocols, VLAN configurations, and device connectivity—are functioning correctly. By automating these validation processes, pyATS ensures that network changes are thoroughly tested and verified, reducing the risk of errors and ensuring high-quality deployments across the platform.

### gNMIc and Prometheus

- **Role**: Collect and aggregate telemetry data.
- **Features**: Real-time data collection, flexible querying, and alerting capabilities.

**gNMIc** is a flexible open-source tool that provides support for **gRPC Network Management Interface (gNMI)**, a protocol used to collect real-time telemetry data from network devices. gNMIc allows engineers to subscribe to telemetry data streams, retrieve device state information, and analyze metrics that provide insight into the health and performance of network infrastructure. **Prometheus** is a powerful open-source monitoring system known for its flexible querying capabilities and real-time alerting. Prometheus collects time-series data from various sources, making it ideal for tracking metrics such as network latency, traffic, and resource utilization. Together, gNMIc and Prometheus enable comprehensive monitoring and visibility into network operations.

In the **NaaS Automation Platform**, **gNMIc** is responsible for collecting telemetry data from network devices, while **Prometheus** stores and aggregates this data. Prometheus queries the data collected by gNMIc to monitor network performance and identify potential issues in real time. The telemetry data gathered includes critical metrics such as bandwidth usage, packet loss, and device health, which are essential for ensuring optimal network performance. By providing timely alerts and enabling detailed insights, gNMIc and Prometheus allow NaaS to maintain a proactive approach to network monitoring and troubleshooting, ensuring reliable service delivery and efficient operations.

### Grafana

- **Role**: Visualize and analyze telemetry data.
- **Features**: Interactive dashboards, alerting, and extensive plugin support.

**Grafana** is a widely-used open-source analytics and monitoring tool designed to visualize time-series data from various sources. It excels in creating interactive, customizable dashboards that allow users to track performance metrics, visualize trends, and generate reports in real-time. With extensive support for plugins, Grafana can integrate with multiple data sources like **Prometheus**, **Elasticsearch**, **Graphite**, and more. Its alerting functionality enables users to set thresholds and receive notifications when certain conditions are met, providing proactive monitoring and enabling quick responses to potential issues.

In the **NaaS Automation Platform**, **Grafana** is used to visualize the metrics collected by **Prometheus**. Telemetry data such as network latency, bandwidth utilization, and device health are presented in intuitive, real-time dashboards, making it easy for engineers to monitor the health and performance of network infrastructure. Grafana's ability to support a wide range of visualizations—including graphs, heatmaps, and tables—ensures that all key metrics are easily interpretable, helping the platform maintain high levels of operational visibility and performance optimization. 

### PagerDuty

- **Role**: Incident management and alerting.
- **Features**: Real-time alerts, integration with monitoring tools, and automated incident resolution workflows.

**PagerDuty** is a leading platform for incident management that helps organizations detect, respond to, and resolve critical incidents in real-time. It integrates seamlessly with a wide range of monitoring tools like **Prometheus**, **Grafana**, and others, ensuring that alerts from various systems are aggregated and routed to the appropriate on-call teams. PagerDuty provides real-time notifications via multiple channels (SMS, email, phone, and mobile apps), allowing teams to respond to incidents quickly and efficiently. Its automation capabilities enable the creation of workflows to escalate issues and trigger automated responses based on pre-defined conditions, reducing downtime and improving operational resilience.

Within the **NaaS Automation Platform**, **PagerDuty** is responsible for managing incidents and alerts related to network services. When telemetry data collected from monitoring tools like **Prometheus** or **Grafana** indicate an issue—such as service degradation or device failure—PagerDuty triggers real-time alerts to the appropriate network teams. By integrating with the platform’s monitoring systems, PagerDuty ensures that incidents are handled swiftly, preventing extended outages and maintaining service continuity. Automated incident resolution workflows also reduce the need for manual intervention, allowing for more efficient network management.

### HashiCorp Vault

- **Role**: Manage secrets and SSL certificates.
- **Features**: Secure storage, dynamic secrets, and data encryption.

**HashiCorp Vault** is a robust tool for managing secrets, sensitive data, and encryption keys used by distributed systems. Vault offers secure storage for secrets, such as passwords, API keys, and SSL certificates, through policies and access control. It ensures that data is encrypted both at rest and in transit, providing high levels of security. Vault also supports dynamic secrets, which are generated on-demand and automatically expired after use, reducing the risk of compromised credentials. With extensive APIs and integrations, Vault can be integrated with automation pipelines, enabling secure, seamless management of credentials and certificates across infrastructure.

In the **NaaS Automation Platform**, **HashiCorp Vault** is used to securely manage all passwords, secrets, and SSL certificates necessary for the operation of the platform. **Nautobot** and other components interact with Vault through its API to retrieve or store sensitive information, such as device login credentials and encryption keys, without exposing them directly in the configuration files. This integration enhances the security of the platform by ensuring that secrets are stored and accessed in a controlled, encrypted environment, reducing the attack surface and minimizing the risk of unauthorized access.

## Real-World Example: Network Fabric as a Service (NFaaS)

The **Network Fabric as a Service (NFaaS)** is one of the network service apps built on top of the **NaaS Automation Platform**. The NFaaS solution runs as a **Nautobot Plugin/App** within the NaaS platform, providing the automation logic necessary to deploy and manage spine/leaf data center fabrics. While NaaS is responsible for integrating various tools such as Nautobot, Cisco NSO, and others, NFaaS defines the automation processes and orchestrates workflows that automate the entire lifecycle of fabric management. This real-world example illustrates how NFaaS automates the process of fulfilling a compute service request through its CI/CD pipeline, leveraging the foundational capabilities of the NaaS platform.

### 1. Plan

The process begins when a client submits an NFaaS compute service request through the Service Portal. The NFaaS App, built as a Nautobot plugin, evaluates the request and determines that a new spine/leaf fabric is needed to support the requested compute infrastructure. The NFaaS App then calculates the required number of racks, servers, switches, cabling, and power requirements. Once the service manager reviews and approves the request, the app automatically generates Jira tasks for the relevant teams—such as purchasing, facilities, and networking—to handle tasks like ordering equipment and scheduling rack installation.

### 2. Code

Network engineers use the NFaaS App to automatically generate the Low-Level Design (LLD) as YAML code. This LLD includes all configurations such as VLANs, IP prefixes, and address assignments, along with underlay and overlay network setups for the spine/leaf fabric. It also defines the rack layout, detailing the placement of servers and network devices, and specifies cabling requirements. Predefined templates are leveraged to ensure consistency in configurations. Once finalized, the YAML code representing the LLD is committed to GitHub, ensuring version control, traceability, and readiness for the CI/CD pipeline.

### 3. Build

Once the Low-Level Design (LLD) is committed to GitHub, the CI/CD pipeline is automatically triggered. In this stage, the YAML files representing the LLD are processed to create a virtual testbed environment. Tools like Cisco Modeling Labs (CML) are employed to simulate the network topology, including the spine/leaf architecture and all specified configurations from the LLD, such as VLANs, IP prefixes, and cabling. This simulation mirrors the planned physical deployment, enabling a precise and controlled environment for validation. The virtual topology is used for subsequent testing, ensuring that the network design functions as expected before any real-world deployment.

### 4. Test

With the virtual testbed in place, the **Test** phase begins to validate the network’s performance and correctness. The testbed simulates the production environment with accurate device and traffic patterns. **IxNetwork Virtual Edition (VE)** generates and tests network traffic flows to confirm routing and switching efficiency between devices.

Automated frameworks like **Cisco pyATS** perform comprehensive tests to ensure that all critical network functions—such as routing protocols and device connectivity—are working as expected. This reduces the risk of misconfigurations or disruptions, and only after passing all tests are the configurations approved for deployment.

### 5. Release

Once all tests have passed successfully, the next step is to package the validated configurations for deployment. In this Release phase, a new release is created in the GitHub repository. This release contains the approved configurations, ensuring they are version-controlled and ready for deployment.

The release is reviewed and approved by the control change committee to ensure that the changes adhere to organizational policies and standards. Following the review, the release is scheduled for deployment during a maintenance window to minimize any potential impact on live services. Using version control in GitHub ensures traceability and accountability, with the option to revert changes if needed.

### 6. Deploy

Once the release is scheduled, the NFaaS App automatically handles the deployment during the designated maintenance window. The deployment process begins by pulling the release from the GitHub repository, ensuring that the correct configurations are applied. The NFaaS App then executes a workflow that updates the Nautobot database with the latest configurations and prepares the necessary infrastructure services.

As part of the deployment workflow, the app updates both the **DHCP** and **DNS** servers to ensure that new devices within the fabric receive the correct IP addresses and have the appropriate DNS entries. For zero-touch provisioning, the app generates base configurations for all spine and leaf devices, uploading these to a **TFTP server** so that the devices can be automatically configured upon boot.

Simultaneously, the NFaaS App computes the detailed network configurations, such as routing protocols and interface settings, and sends them to **Cisco NSO**. NSO processes and pushes these configurations to the physical network devices via its southbound APIs. Once all devices are configured and operational, the NFaaS App updates the monitoring systems to ensure metrics are collected from the newly deployed fabric and alerts are set up for real-time performance monitoring and issue detection.

This automated deployment process ensures a seamless and error-free integration of the new fabric into the existing network infrastructure.

### 7. Operate

Once the spine/leaf fabric is live, the NFaaS App initiates real-time monitoring of both the compute service and the underlying fabric. Prometheus and Grafana are leveraged to collect and visualize performance metrics such as latency, packet loss, and resource utilization across the spine and leaf switches. This continuous monitoring ensures that any anomalies are detected early, providing valuable insights into the overall health of the fabric.

PagerDuty is integrated to send real-time alerts to engineers if any critical issues are detected, enabling fast resolution of performance bottlenecks or device malfunctions. Additionally, Grafana dashboards are accessible to field technicians, offering visibility into device statuses, such as faulty line cards and down connections due to missing or incorrect transceivers. The dashboards also display critical information about miswired cables, helping technicians quickly identify and rectify physical wiring issues that could affect network performance. This hands-on visibility ensures that any hardware or connection issues are promptly addressed, ensuring the fabric remains operational and performs as expected.

### 8. Monitor and Feedback

Once the spine/leaf fabric is operational, continuous monitoring ensures its performance and stability by collecting real-time telemetry data from the fabric’s switches. Metrics like throughput, CPU utilization, and link health are visualized in Grafana to provide engineers with real-time insights and detect potential bottlenecks or degraded performance. This feedback is not only used to address immediate issues but also informs future planning cycles, driving continuous improvement.

Feedback loops play a crucial role in optimizing automation workflows, incorporating predictive analytics, and introducing dynamic scaling based on traffic patterns. By analyzing telemetry data, the platform can improve fault tolerance by adjusting failover procedures, enhancing service provisioning logic, or fine-tuning resource allocation. Additionally, feedback from operational data helps strengthen security protocols and detect vulnerabilities, ensuring the network remains resilient and adaptive to evolving operational needs.

## Conclusion

The NaaS Automation Platform showcases the transformative power of network automation, integrating advanced tools and workflows to enhance scalability, reliability, and operational efficiency. By adopting NetDevOps practices and Infrastructure as Code (IaC), NaaS minimizes manual intervention and accelerates service delivery across various environments. With continuous innovation and real-time monitoring, it enables organizations to adapt swiftly to evolving demands, ensuring both seamless operations and future scalability. Ultimately, NaaS not only simplifies network management but unlocks the full potential of automation, driving strategic value in modern IT ecosystems.

### Glossary

Include a glossary to define key terms and acronyms used throughout the document:

- **CLI**: Command Line Interface
- **IaC**: Infrastructure as Code
- **GitOps**: Operational framework using Git as the single source of truth
- **NetDevOps**: Network engineering integrated with DevOps principles
- **CI/CD**: Continuous Integration and Continuous Delivery/Deployment
- **NaaS**: Network as a Service
- **HLD**: High-Level Design
- **LLD**: Low-Level Design
- **SoT**: Source of Truth

### References and Further Reading

- [Nautobot](https://nautobot.readthedocs.io/)
- [Cisco Network Services Orchestrator (NSO)](https://www.cisco.com/c/en/us/products/cloud-systems-management/network-services-orchestrator/index.html)
- [Cisco Modeling Labs (CML)](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html)
- [Cisco pyATS](https://developer.cisco.com/docs/pyats/)
- [IxNetwork Virtual Edition (VE)](https://www.keysight.com/us/en/products/network-test/protocol-load-test/ixnetwork-ve.html)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [PagerDuty](https://www.pagerduty.com/)
- [HashiCorp Vault](https://www.vaultproject.io/)
