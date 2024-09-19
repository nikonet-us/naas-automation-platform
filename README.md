# The Challenges of Classical Network Management

## Introduction

In today's rapidly evolving digital landscape, efficient network management is crucial for maintaining robust and scalable IT infrastructures. Traditional methods, while offering control, often fall short in meeting the demands of modern, dynamic environments. This presentation explores the challenges of classical network management and introduces the Network as a Service (NaaS) Automation Platform as a comprehensive solution to these issues.

## The Challenges of Classical Network Management

Traditionally, networks have been managed through manual configurations via the Command Line Interface (CLI). While this approach offers granular control over individual devices, it comes with several challenges:

- **Error-Prone**: Manual configurations can lead to human errors, causing misconfigurations or inconsistencies across devices.
- **Time-Consuming**: Managing large-scale networks requires configuring multiple devices one by one, which is slow and inefficient, especially in dynamic environments.
- **Lack of Scalability**: As networks grow in size and complexity, maintaining consistency and ensuring reliability through manual processes becomes increasingly difficult.
- **Limited Collaboration**: Network configurations are typically siloed and lack version control, making it harder for teams to collaborate or track changes.

These challenges have driven the need for network automation, which simplifies and streamlines the process of managing network infrastructure.

## How Network Automation Solves These Challenges

Network automation addresses the limitations of traditional CLI-based network management by automating the configuration, management, and monitoring of network devices. Here’s how it solves key challenges:

- **Minimizes Human Error**: Automated processes reduce the chance of misconfigurations and ensure that network changes are applied consistently across all devices.
- **Increases Efficiency**: Network automation significantly reduces the time spent on manual configuration by automating repetitive tasks, allowing engineers to focus on higher-level strategic work.
- **Enables Scalability**: As networks grow, automation ensures that devices are configured and managed uniformly, making it easier to scale operations without sacrificing reliability.
- **Improves Collaboration**: By using version control and automated pipelines, teams can collaborate more effectively, track changes, and ensure that configurations are deployed in a controlled manner.

## Introducing the NaaS Automation Platform

The Network as a Service (NaaS) Automation Platform is designed to manage the entire lifecycle of network services across diverse environments, including Enterprise, Data Centers, Cloud, and Service Provider networks. By applying a single, unified approach to automation, NaaS ensures scalability, efficiency, and consistency across all network types.

This platform simplifies the management and provisioning of network services by leveraging the principles of Infrastructure as Code (IaC) with GitOps and best practices from the NetDevOps discipline. The NaaS platform delivers a comprehensive, automated solution for the entire network lifecycle, encompassing everything from initial provisioning to ongoing management and monitoring. With a focus on automation and reliability, NaaS ensures efficient and seamless network operations across all environments.

## Key Concepts

### What is Network Automation?

Network automation refers to the process of using software to automate the configuration, management, and operations of network devices. This reduces the need for manual intervention, minimizes errors, and improves network efficiency and agility.

### What is a Platform?

A platform is a combination of tools and systems that work together by communicating through APIs (Application Programming Interfaces). In the context of the NaaS Automation Platform, it integrates various network automation tools, monitoring systems, and task management systems, providing a cohesive environment for automating network services.

### What is Infrastructure as Code (IaC)?

Infrastructure as Code (IaC) is a practice in which infrastructure configurations are defined and managed using code rather than manual processes. This allows for consistent, repeatable, and scalable deployment of network resources using version-controlled repositories like GitHub.

### What is GitOps?

GitOps is a modern operational framework that uses Git as the single source of truth for defining infrastructure and application configurations. It allows automated pipelines to continuously monitor Git repositories and apply changes to infrastructure in a controlled and reliable way.

### What is NetDevOps?

NetDevOps combines network engineering with the principles of DevOps, which emphasizes collaboration between development and operations teams. In the NetDevOps approach, network automation is treated as a software development process, ensuring continuous integration and delivery of network configurations through version control and automation tools.

### What is CI/CD?

CI/CD stands for **Continuous Integration** and **Continuous Delivery** (or **Continuous Deployment**), practices that automate the process of integrating code changes, testing them, and delivering them to production environments. In the context of the **NaaS Automation Platform**, CI/CD pipelines form a continuous loop that ensures fast, reliable, and error-free network operations by automating the integration, testing, deployment, and monitoring of network configurations.

### What are CI/CD Pipelines?

CI/CD pipelines are automated workflows that enable the continuous testing, building, and deployment of network configurations. In the NaaS platform, CI/CD pipelines ensure that all changes are automatically validated and deployed, ensuring fast, reliable, and error-free network operations.

## The CI/CD Loop

The CI/CD loop is divided into distinct phases, each playing a critical role in ensuring the stability, efficiency, and accuracy of network changes:

1. **Plan**: Define network changes, requirements, and collaborate on design using tools like Jira and Confluence.
2. **Code**: Use Infrastructure as Code (IaC) principles to develop and configure network infrastructure, with version control in GitHub ensuring consistency and traceability.
3. **Build**: Trigger CI/CD pipelines to build the virtual testbed environment using tools like Cisco Modeling Labs (CML) to simulate the network infrastructure for testing network changes.
4. **Test**: The network configurations are validated in the controlled environment to ensure they meet the required standards without impacting existing services.
5. **Release**: After successful validation, the configurations are marked as ready for deployment, and the release is created and approved.
6. **Deploy**: Automatically roll out the validated configurations to the live network, ensuring minimal disruption to existing services.
7. **Operate**: Monitor the network’s performance in real-time using tools like Prometheus and Grafana to proactively detect and address issues.
8. **Monitor and Feedback**: Continuously monitor the deployed configurations and use telemetry data to improve future network changes, feeding insights back into the planning stage.

By looping through these phases, the NaaS Automation Platform ensures a seamless and reliable delivery of network services, reducing the risk of errors and maintaining high operational efficiency.

## NaaS Automation Platform Core Technologies and Their Roles

The NaaS Automation Platform integrates a suite of core technologies, each playing a pivotal role in the automation and management of network services:

1. **Nautobot**
   - **Role**: Store and manage network data, configurations, and inventory.
   - **Features**: Extensible data models, powerful APIs, and integration capabilities with various network automation tools.
   
2. **Cisco NSO**
   - **Role**: Provision and manage network devices based on data provided by Nautobot.
   - **Features**: Model-driven service orchestration, multi-vendor support, and service lifecycle management.
   
3. **Service Portal**
   - **Role**: Customer-facing portal for requesting network services.
   - **Features**: Self-service interface, request tracking, and integration with automation processes.
   
4. **Jira/Confluence**
   - **Role**: Coordination, task tracking, and documentation for human-to-human interactions.
   - **Features**: Task management, issue tracking, cross-team collaboration, and centralized documentation.
   
5. **Git/GitHub**
   - **Role**: Provide version control and a collaborative development environment.
   - **Features**: Version control, pull requests, issue tracking, and integration with CI/CD pipelines.
   
6. **kea-dns-server**
   - **Role**: Provide DNS services for dynamic registration of IP addresses and FQDNs.
   - **Features**: Automatic DNS registration, integration with DHCP for seamless IP-to-FQDN mapping, and high scalability.
   
7. **kea-dhcp-server**
   - **Role**: Provide DHCP services for network infrastructures.
   - **Features**: High performance, extensibility, and rich configuration options.
   
8. **Cisco Modeling Labs (CML)**
   - **Role**: Validate network service changes in a virtual environment.
   - **Features**: Virtual network simulation, comprehensive device support, and integration with CI/CD pipelines.
   
9. **IxNetwork Virtual Edition (VE)**
   - **Role**: Test and validate network traffic flows.
   - **Features**: Comprehensive network testing, virtual and physical traffic validation, and scalability for production environments.
   
10. **Cisco pyATS**
    - **Role**: Validate network services.
    - **Features**: Automated testing, network device interactions, and comprehensive test coverage.
    
11. **gNMIc and Prometheus**
    - **Role**: Collect and aggregate telemetry data.
    - **Features**: Real-time data collection, flexible querying, and alerting capabilities.
    
12. **Grafana**
    - **Role**: Visualize and analyze telemetry data.
    - **Features**: Interactive dashboards, alerting, and extensive plugin support.
    
13. **PagerDuty**
    - **Role**: Incident management and alerting.
    - **Features**: Real-time alerts, integration with monitoring tools, and automated incident resolution workflows.
    
14. **HashiCorp Vault**
    - **Role**: Manage secrets and SSL certificates.
    - **Features**: Secure storage, dynamic secrets, and data encryption.

## Real-World Example: Network Fabric as a Service (NFaaS)

To illustrate how these technologies come together, let’s explore a real-world example using the Network Fabric as a Service (NFaaS) solution. In this example, the NFaaS platform automates the entire process of fulfilling a compute service request through its CI/CD pipeline. Here’s a breakdown of the main steps in this pipeline:

### 1. Plan

- **Define network changes and requirements**.
- **Collaborate on design** using Jira and Confluence to document the High-Level Design (HLD) and Low-Level Design (LLD) for the compute request.
- **Identify necessary network configurations and infrastructure** (spine/leaf fabric).

**Process**:
A client submits a compute service request through the Service Portal. Nautobot evaluates the request and determines that a new spine/leaf fabric is required to support the compute infrastructure. It calculates the necessary number of racks, servers, switches, and cabling, along with the power requirements. Once the service manager approves the request, Nautobot generates Jira tickets for the relevant teams (e.g., purchasing, facilities, and networking) to handle the required tasks, such as ordering equipment and scheduling rack installation.

### 2. Code

- **Define configurations using IaC principles** in GitHub.
- **Automate generation of configurations** for switches, VLANs, subnets, and IP addresses using predefined templates.
- **Commit configurations to GitHub** for version control.

**Process**:
Network engineers utilize Infrastructure as Code (IaC) principles to automate the creation of network configurations. Nautobot leverages predefined templates to automatically generate configurations for spine and leaf switches, VLANs, subnets, and IP addresses. All configurations are then committed to GitHub, providing a version-controlled record that prepares the setup for the next phase.

### 3. Build

- **Trigger GitHub CI/CD processes** to initiate automated pipelines.
- **Build the virtual testbed environment** for testing network changes.

**Process**:
Once the network configurations are committed to GitHub, automated pipelines are triggered to build the virtual testbed environment. This involves setting up simulated network infrastructures using tools like Cisco Modeling Labs (CML) and IxNetwork VE, ensuring that the environment accurately represents the live network. The virtual testbed environment is then ready for the subsequent testing phase.

### 4. Test

- **Validate network changes in the virtual testbed** using Cisco Modeling Labs (CML) and IxNetwork VE.
- **Ensure configurations meet service requirements** without impacting existing services using Cisco pyATS.

**Process**:
In the test phase, the spine/leaf fabric is validated within the virtual environment before deployment. Utilizing Cisco Modeling Labs (CML), a virtual testbed simulates the new spine/leaf architecture, where network devices are interconnected, and traffic is routed between leaf and spine switches. IxNetwork VE appliances simulate compute traffic to ensure correct traffic flow and routing. Automated testing frameworks such as Cisco pyATS run comprehensive tests to validate connectivity, routing protocols (e.g., BGP or OSPF), and VLAN configurations. Only configurations that pass all tests are approved for release, ensuring that they meet the required standards and do not adversely affect existing services.

### 5. Release

- **Create and publish a new release** in the GitHub repository after passing all validation tests.
- **Review, approve, and schedule deployment**.

**Process**:
Once the spine/leaf fabric configurations pass all validation tests, a new release is created and published in the GitHub repository. This release includes all validated configurations, such as switch settings, VLANs, subnets, and IP addresses for the fabric. The release is reviewed, approved, and scheduled by the control change committee, ensuring compliance with organizational standards. Once approved, the release is scheduled for deployment during a maintenance window.

### 6. Deploy

- **Deploy configurations to the physical network** using Nautobot and Cisco NSO.
- **Allocate subnets and IP addresses**, and push necessary configurations via TFTP, DHCP, and DNS servers.
- **Validate fabric’s performance and operational readiness** through automated tests.

**Process**:
Nautobot and Cisco NSO work together to deploy the spine/leaf fabric in the physical network. Nautobot pulls the latest configurations from GitHub, updates its internal database, and generates the necessary device configurations based on validated templates. These configurations, which include the allocation of subnets and IP addresses, are then applied through integration with DHCP and DNS servers. Additionally, base configurations are uploaded to a TFTP server for zero-touch provisioning. Once the configurations are computed, Nautobot sends them to Cisco NSO via its northbound RESTCONF interface. Cisco NSO processes the configurations and distributes them to the respective network devices through its southbound APIs, such as NETCONF, RESTCONF, SNMP, and CLI. Post-deployment tests are automatically triggered to validate the fabric’s performance, ensuring proper spine-to-leaf connectivity, BGP neighbor relationships, and overall service readiness. This deployment process guarantees that the new fabric is seamlessly integrated into the broader infrastructure with consistency and without manual errors.

### 7. Operate

- **Begin real-time monitoring** using Prometheus and Grafana to track performance.
- **Respond to issues** with alerts from PagerDuty.
- **Ensure efficient operation** through continuous monitoring.

**Process**:
Once the spine/leaf fabric is live, real-time monitoring of the compute service and underlying fabric is initiated using Prometheus and Grafana. These tools gather performance metrics such as latency, packet loss, and resource utilization on the spine and leaf switches. If any anomalies arise, PagerDuty alerts the relevant engineers for immediate action, ensuring that the fabric remains stable and meets the performance expectations.

### 8. Monitor and Feedback

- **Continuously monitor performance and stability**.
- **Analyze telemetry data** via gNMIc and visualize insights with Grafana.
- **Incorporate feedback** into the planning stage for adjustments and optimizations.

**Process**:
After the spine/leaf fabric is deployed, continuous monitoring ensures that the network infrastructure operates smoothly. Telemetry data from gNMIc is collected from the fabric switches and analyzed using Grafana, providing insights into network performance, such as throughput, switch CPU usage, and link health. Any anomalies or performance optimizations are looped back into the planning phase for potential reconfiguration or scaling, ensuring the fabric continues to meet operational needs over time.

## Conclusion

The NaaS Automation Platform showcases the power of modern network automation, integrating open-source and commercial tools to transform how networks are managed across diverse environments, from enterprise to data centers, cloud, and service providers. By adopting NetDevOps practices and Infrastructure as Code (IaC) principles, the platform ensures that network services are not only provisioned with precision but also managed with efficiency and scalability. This reduces manual intervention, minimizes errors, and accelerates the deployment of services, making it ideal for dynamic and growing network environments.

NaaS delivers continuous innovation by enabling real-time monitoring, proactive incident resolution, and seamless updates through its CI/CD pipeline, allowing organizations to stay ahead in today’s fast-evolving digital landscape. It enhances the agility of network operations, ensures scalability to meet future demands, and promotes consistency in configurations and compliance.

Moreover, the NaaS Automation Platform offers a forward-looking framework that evolves with industry trends, accommodating new technologies, integrations, and automation techniques as they emerge. This forward-thinking approach positions NaaS as a vital solution for organizations striving for digital transformation, where operational efficiency, security, and scalability are critical to staying competitive.

By automating the lifecycle of network operations, from provisioning to deployment and monitoring, NaaS enables network engineers to focus on strategic initiatives rather than routine tasks, fostering innovation and driving business outcomes. It is not just a solution to replace manual processes—it’s a platform designed to unlock the full potential of network automation in any modern IT ecosystem.

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

- [Nautobot Documentation](https://nautobot.readthedocs.io/)
- [Cisco Network Services Orchestrator (NSO)](https://www.cisco.com/c/en/us/products/cloud-systems-management/network-services-orchestrator/index.html)
- [Cisco Modeling Labs (CML)](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html)
- [Cisco pyATS](https://developer.cisco.com/docs/pyats/)
- [IxNetwork Virtual Edition (VE)](https://www.keysight.com/us/en/products/network-test/protocol-load-test/ixnetwork-ve.html)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [HashiCorp Vault](https://www.vaultproject.io/)
