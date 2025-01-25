# Glossary

<!-- markdownlint-disable MD013 line-length, MD001 heading-increment -->

### 32-bit versus 64-bit

Processing modes referring to the size of each instruction processed by the CPU.

- **32-bit CPUs** replaced earlier 16-bit CPUs and were used through the 1990s to the present day.
- **64-bit CPUs** now dominate, with the main platform called **AMD64** or **EM64T** (by Intel).
- 64-bit versions of Windows and various Linux distributions support this platform.
- **Note:** 64-bit CPUs can run most 32-bit software, but a 32-bit CPU cannot execute 64-bit software.

---

### 8.3 Filenames

The DOS file naming standard:

- **Format:** An eight-character ASCII name followed by a three-character file extension (e.g., `example.txt`).
- Windows supports long file names but can generate short file names based on DOS 8.3 naming rules for backward compatibility.

---

### AAA

**Authentication, Authorization, and Accounting**:

- The principal stages of security control to protect a resource.

---

### Accelerometer/Gyroscope

Components in mobile devices:

- **Accelerometer**: Detects motion.
- **Gyroscope**: Detects rotation.\
  Applications: Switch screen orientation or serve as a control mechanism (e.g., using a tablet as a steering wheel in a driving game).

---

### Access Control

The process of protecting a resource by creating barriers:

- Each resource has an **Access Control List (ACL)** specifying user permissions.
- Example: Permissions to read or read and edit a file.

---

### ACL (Access Control List)

Permissions configured on a network resource, such as:

- **Resources**: Folders, files, firewalls.
- **Subjects**: User accounts, host IP addresses.
- **Privileges**: Read-only, read/write, etc.

---

### Active Partition

- The **primary partition** marked as active (one per system).
- This partition becomes the **bootable partition**.
- In Microsoft terminology, the **system partition** is where the PC boots from.

---

### Adapter Card

- A circuit board providing additional functionality to the computer (e.g., video, sound, networking, modem).
- Fits into a **slot** on the PC's expansion bus (e.g., PCI, PCIe).
- Often provides **ports** accessible through the back of the PC case.

---

### Addressing (Network)

- Each host on a network must have an **address** to communicate.
- **IPv4**: 32-bit binary number expressed in **dotted decimal notation** (e.g., `192.168.1.1`).
- **IPv6**: 128-bit binary number expressed in **hexadecimal**.
- Routable addressing schemes, such as IP, identify distinct networks and hosts.

---

### Adware

Software that records information about a PC and its user:

- Often used with user consent (e.g., an online store tracking purchases to suggest products).

---

### Airplane Mode

- A toggle on mobile devices to **quickly disable or enable wireless functionality** (e.g., Wi-Fi, Bluetooth).

---

### Algorithm

A defined method for performing a process:

- **Encryption Algorithms**: Techniques used to encrypt a message.
- **Key Size**: Determines algorithm strength (minimum secure key size: 2048 bits).
- Examples of encryption technologies:
  - **Hash Functions**: SHA-1, MD5.
  - **Symmetric Encryption**: 3DES, AES, RC, IDEA, Blowfish/Twofish, CAST.
  - **Asymmetric Encryption**: Diffie-Hellman, RSA, ElGamal, ECC.

---

### AMD (Advanced Micro Devices)

- A CPU manufacturer providing competition for Intel.
- Known for popular chips such as **K6**, **Athlon 64**, and **Opteron**, which have often outperformed their Intel equivalents.

---

### Android

- Mobile operating system (OS) for smartphones and tablets.
- Developed by the **Open Handset Alliance**, primarily sponsored by Google.
- **Open source software**.

---

### Anti-virus

- Software capable of detecting and removing:
  - **Viruses**.
  - Other malware types: worms, Trojans, rootkits, adware, spyware, etc.
- Works using:
  - **Signatures**: Identifying known malware.
  - **Heuristics**: Detecting suspicious behavior.
- Must be regularly updated with the latest malware definitions.

---

### AP (Access Point)

- A device providing connectivity between wireless devices and a cabled network.
- Public APs with Internet access are often referred to as **hotspots**.

---

### Apple

- Manufacturer of desktop and portable computers, as well as smartphones and tablets.
- Apple computers use **OS X**, making them incompatible with IBM PC/Windows-based software.

---

### ARM (Advanced RISC Machines)

- Designer of CPU and chipset architectures widely used in mobile devices.
- **RISC**: Reduced Instruction Set Computing.
- RISC uses simple instructions processed quickly, contrasting with CISC (Complex Instruction Set Computing).

---

### ARP (Address Resolution Protocol)

- Resolves an IP address to a device's **MAC address**.
- Hosts cache mappings in an **ARP table** for a few minutes.
- **`arp` utility**: Used to manage the ARP cache.

---

### Array

- An identifier for a group of variables of the same type.
- **Fixed size**: The number of elements is set when the array is declared.

---

### ASCII

- **7-bit code page** mapping binary values to character glyphs.
- Standard ASCII can represent **127 characters**, with some values reserved for non-printing control characters.

---

### Assembly Language

- A machine code represented in **human-readable text**.
- Created using the instruction set of the CPU platform.

---

### Attack Surface

- The degree of exposure a network or software has to attacks.
- Example: A server with many open ports or features installed increases the risk of attack.

---

### Audio Card

- An adapter card providing sound playback and recording functionality.

---

### Audio Port

- **Audio I/O ports** found on motherboards or sound cards.
- Common types:
  - **Audio Out**
  - **Audio In**
  - **Speaker Out**
  - **Microphone Input/Mic**
  - **Headphones**

---

### Authentication

- Means for a user to **prove their identity** to a computer system.
- Methods:
  - **Something you know**: Username/password.
  - **Something you have**: Smart card or key fob.
  - **Something you are**: Biometric information.
- Commonly uses **2-factor authentication**.

---

### Availability

- Ensuring resources are accessible when needed.
- Examples:
  - Avoiding overly strict security policies (e.g., users writing passwords on sticky notes).
  - Implementing **key recovery** or escrow to recover encrypted data.
  - Protecting resources against loss, damage, or **DoS attacks**.

### Backup

- **Definition**: A system to recover data using backup mechanisms.
- **Common Features**:
  - Support for **tape devices** as a reliable medium.
  - Different backup types:
    - **Full**: Copies all data.
    - **Incremental**: Copies only changes since the last backup.
    - **Differential**: Copies changes since the last full backup.
- **Balance**: Media capacity, backup time, and restore time.

---

### Binary

- **Definition**: A notational system with two values per digit (0 and 1).
- **Purpose**: Used by computers because their transistors have two states: off and on.

---

### Biometric

- **Definition**: Identifying features stored as digital data to authenticate users.
- **Examples**: Facial pattern, iris, retina, fingerprint pattern, and signature recognition.
- **Requirements**:
  - Scanning device (e.g., fingerprint reader).
  - Database of biometric templates.

---

### BIOS (Basic Input/Output System)

- **Definition**: Firmware for basic PC component operations (e.g., drives, keyboard, display).
- **Functions**:
  - Configuration via setup routines.
  - Power-On Self-Test (POST) for detecting faults.
  - **Security**: Supervisor password for BIOS settings and user password for booting.

---

### Bit/Byte

- **Definition**: Units of data storage.
- **See Also**: [Data Units](#data-units).

---

### Bluetooth

- **Definition**: Short-range radio technology for device communication (up to 10m at 1 Mbps).
- **Uses**:
  - Connect peripherals (e.g., mice, keyboards).
  - Device communication (e.g., laptop to smartphone).
- **Challenges**:
  - Signals blocked by thick walls/metal.
  - Interference from other 2.4 GHz devices.
- **Bluetooth Low Energy (BLE)**:
  - Designed for low-power devices with infrequent data transmission.
  - Not backward-compatible with classic Bluetooth, though devices can support both.

---

### Blu-ray

- **Definition**: Latest generation of optical drive technology.
- **Capacity**: 25 GB per layer.
- **Transfer Rates**: Multiples of 36 MBps.

---

### Boolean

- **Definition**: Data type supporting 1-bit storage (TRUE/FALSE).
- **Purpose**: Supports conditional logic (branching and looping) in computer programs.

---

### Boot Partition

- **Definition**: The partition containing the operating system (`\WINDOWS` folder).
- **Note**: Typically different from the **system partition**, which contains the boot files.

---

### bps (Bits per Second)

- **Definition**: Measure of data transfer speed.
- **Note**: Higher bps indicates faster transmission.

---

### Browser

- **Definition**: Software to view HTML pages.
- **Requirements**:
  - Proper configuration and up-to-date system patches for security.
- **Common Vulnerabilities**:
  - Browser plug-ins (e.g., Flash, PDF readers).

---

### Bus

- **Definition**: Connections between components on the motherboard and peripherals.
- **Functions**:
  - Data sharing.
  - Memory addressing.
  - Power supply.
  - Timing.
- **Types**:
  - PCI.
  - PCI Express.
  - ExpressCard.
  - USB.

---

### Business Continuity Plan (BCP) / Continuity of Operations Plan (COOP)

- **Definition**: Plan to ensure critical business functions remain available and fault-tolerant.
- **Key Elements**:
  - Redundant resources (e.g., cluster services, RAID arrays, UPS).
  - Employee, utility, supplier, and customer considerations.
- **Associated Plan**: Disaster Recovery Plan (DRP), detailing actions for critical incidents.

### Cable (Hybrid Fiber Coax)

- **Definition**: Internet connection often bundled with cable telephone/television service (Cable Access TV \[CATV]).
- **Technology**: Combines a fiber optic core with coaxial links to consumer premises equipment.
- **Interface**: Uses a cable "modem" functioning like a bridge.

---

### CAD (Computer-Aided Design)

- **Definition**: Software that facilitates the creation and revision of technical drawings and schematics.

---

### Captive Portal

- **Definition**: A web page or website that redirects clients before granting full network access.
- **Uses**:
  - Limited browsing.
  - Authentication.
  - Providing resources for compliance (patches, signature updates).
- **Mechanism**: Redirects a user’s browser to a server for credentials or payment.

---

### CD-ROM (Compact Disc—Read Only Memory)

- **Definition**: Optical storage technology with a capacity of 700 MB or 80 minutes of audio data.
- **Types**:
  - Recordable (R).
  - Re-writable (RW).
- **Uses**:
  - Backup.
  - Archiving.
  - Preserving tamper-proof records.

---

### Celeron Processor Series

- **Definition**: Budget processor models from Intel, produced alongside Pentium and Core ranges.

---

### Cell Phone

- **Definition**: Mobile communication device using base station transmitters (cells) for network access.
- **Data Communication Generations**:
  - **2G**: GSM (up to 14 Kbps).
  - **2.5G**: GPRS, HSCSD, EDGE (up to 48 Kbps).
  - **3G**: WCDMA (up to 2 Mbps).

---

### Certificate

- **Definition**: A public key certified by an agency to verify its owner’s identity.
- **Uses**:
  - Encrypting messages.
  - Authentication.
  - Signing documents.
- **Standards**:
  - X.509.
  - PGP web of trust.

---

### Char

- **Definition**: Data type that supports storage of a single character.

---

### Chipset

- **Definition**: Manages communication between PC components through controllers (e.g., memory, graphics, I/O).
- **Historical Design**:
  - **Northbridge**: Handles fast controllers (memory, video).
  - **Southbridge**: Handles slower buses (SATA, USB, audio, LAN, legacy buses).
- **Modern Design**:
  - Memory and video controllers integrated into the CPU.

---

### Chrome OS

- **Definition**: Proprietary OS derived from Linux and Chromium.
- **Developer**: Google.
- **Hardware**: Runs on Chromebooks (laptops) and Chromeboxes (PCs).

---

### CIA Triad

- **Definition**: Goals for secure information management.
- **Components**:
  - **Confidentiality**: Protecting data from unauthorized access.
  - **Integrity**: Ensuring data accuracy and consistency.
  - **Availability**: Ensuring data and resources are accessible.

---

### Client

- **Definition**: A system or software that requests and receives resources, applications, or data from a server over a network.

- **Function**: Provides connectivity to servers for accessing resources and interacting with hosted services.

- **Model**
  - **Client-Server**: Centralized server provides resources; clients initiate requests to utilize them.
- **Examples**: Windows, NetWare, Linux clients.

---

### Cloud Computing

- **Definition**: A service model where software (e.g., SaaS, PaaS) or resources (e.g., IaaS, NaaS) are provided to end users without requiring their involvement in the underlying infrastructure.
- **Features**:
  - Elasticity of resources.
  - Pay-per-use pricing.
- **Access Models**:
  - Public.
  - Hosted private.
  - Private (onsite or offsite).

---

### Compatibility Mode

- **Definition**: Windows feature enabling older programs to run using settings from previous versions of Windows.
- **Configuration**: Accessed from the program’s shortcut properties dialog.

---

### Compression Software

- **Definition**: Utilities that reduce file size for storage or transmission by compressing data.
- **Purpose**:
  - Save storage space.
  - Reduce bandwidth usage.

---

### Computer Management Console

- **Definition**: A Windows tool providing administrative functions such as:
  - Device Manager.
  - Event Viewer.
  - Disk Management.
  - Services.
  - Performance Monitor.
- **Access**: Right-click (My) Computer > Manage.

---

### Constant

- **Definition**: An identifier for a value that remains unchanged during program execution.

---

### Control Panel

- **Definition**: The primary management interface in Windows, used for configuring system settings.

---

### Cookie

- **Definition**: A small text file storing information about a user’s session on a website.
- **Vulnerabilities**: Cookies can be exploited in replay attacks if session data is intercepted.

---

### Cooling Device

- **Definition**: Mechanism to dissipate heat generated by a CPU to prevent damage.
- **Types**:
  - **Active**: Requires power (e.g., fan or liquid cooling).
  - **Passive**: Requires no power (e.g., heatsinks).
- **Features**:
  - Uses thermal compound to improve heat transfer.
  - May include advanced cooling solutions for high-performance systems.

---

### Core Processor Series

- **Definition**: Intel’s premium line of CPUs, including Core, Core 2, and Core iX processors.
- **Features**:
  - Successors to the Pentium M architecture.
  - Designed for both desktop and mobile platforms.

---

### CPU (Central Processing Unit)

- **Definition**: The primary microprocessor in a computer or smartphone responsible for executing operating systems and applications software.

---

### CRT (Cathode Ray Tube) Monitor

- **Definition**: An analog monitor that displays images using red, green, and blue dots on the screen.
- **Features**:
  - Screen size is measured diagonally.
  - Obsolete; replaced by LCD panels.

---

### DAC (Discretionary Access Control)

- **Definition**: An access control model where the owner of a resource manages its Access Control List (ACL).

---

### Data Rate

- **Definition**: The speed at which data can be transferred between components, either within a computer or across a network.
- **Key Metrics**:
  - Peak rate (maximum theoretical speed).
  - Actual throughput (sustained speed).

---

### Data Units

- **Definition**: Units used to measure data storage and transfer.
- **Basic Units**:
  - 1 bit = binary digit (0 or 1).
  - 8 bits = 1 byte (B).
- **Hierarchy**:
  - 1024 bytes = 1 Kilobyte (KB).
  - 1024 KB = 1 Megabyte (MB).
  - 1024 MB = 1 Gigabyte (GB).
  - 1024 GB = 1 Terabyte (TB).
- **Additional Units**:
  - Nibble = ½ byte.
  - Word = 2 bytes.

---

### Database

- **Definition**: A system for managing data utilized by network applications.
- **Major Database Servers**:
  - Oracle.
  - Microsoft SQL Server.
  - IBM DB2 and Informix.
  - Sybase.
  - MySQL (freeware).
- **Key Features**:
  - Uses SQL (Structured Query Language).
  - Security and patching are critical.

---

### DDR SDRAM (Double Data Rate SDRAM)

- **Definition**: A standard for SDRAM that transfers data twice per clock cycle.
- **Variants**:
  - DDR2/DDR3 SDRAM: Lower voltage chips, higher bus speeds.

---

### Default Account

- **Definition**: Pre-configured administrative and guest accounts on servers and network devices.
- **Best Practices**:
  - Rename Windows administrative accounts.
  - Avoid using the "root" system owner account on UNIX/Linux.

---

### Default Gateway

- **Definition**: A TCP/IP address parameter identifying the router on the local subnet for external network communication.

---

### Delimiter

- **Definition**: A symbol or set of symbols used to separate individual elements in structured data.

- **Examples**:

  - A comma (`,`) separates values in CSV (Comma-Separated Values) files.
  - A tab character (`\t`) is used in tab-delimited files.
  - Semicolons (`;`) and pipes (`|`) are commonly used in custom data formats.

- **Features**:
  - Essential for parsing and organizing structured data.
  - Customizable in many file formats to meet specific needs.

---

### Desktop

- **Definition**: Primary user interface in Windows 7 and earlier.
- **Components**:
  - Contains Computer, Documents, Network, and Recycle Bin.
  - Stores shortcuts to programs and files.

---

### Device Driver

- **Definition**: A small program that allows the operating system to interact with hardware.
- **Features**:
  - Loaded during the boot sequence.
  - Must be signed in Windows to ensure OS stability.

---

### Device Manager

- **Definition**: Windows tool for managing hardware devices.
- **Features**:
  - Enable/disable devices.
  - View hardware properties and system resources.
  - Update device drivers.

---

### Digital Camera (Digicam)

- **Definition**: A camera that uses light-sensitive diodes and electronic storage instead of film.
- **Features**:
  - Uses CCD arrays for image capture.
  - Resolution: Typically 5 megapixels or better.
  - Connects via USB or Firewire.

---

### Digital Certificate

- **Definition**: An X.509 certificate issued by a Certificate Authority (CA) to guarantee the authenticity of a public key.
- **Uses**:
  - Encrypt messages using the public key.
  - Messages are decrypted using the private key (asymmetric encryption).
- **Infrastructure**:
  - Referred to as Public Key Infrastructure (PKI).

---

### Digital Signaling

- **Definition**: Signaling using discrete states to represent simple values like 1 or 0.

---

### DIMM (Dual Inline Memory Module)

- **Definition**: Standard packaging for system memory.
- **Pin Configurations**:
  - SDRAM: 168 pins.
  - DDR SDRAM: 184 pins.
  - DDR2/3 SDRAM: 240 pins.

---

### Directory

- **Definition**: A file system object used to organize files.
- **Features**:
  - Root directory is the base of a drive.
  - Subdirectories can be created within directories.
  - In Windows, directories are referred to as folders.

---

### Disaster Recovery Plan

- **Definition**: A documented and resourced plan showing actions and responsibilities during critical incidents.
- **Features**:
  - Includes practice drills for staff preparation.
  - Emphasizes the importance of maintaining secure systems.

---

### DisplayPort

- **Definition**: A digital A/V interface developed by VESA.
- **Features**:
  - Supports cross-compatibility with DVI and HDMI devices.

---

### DNS (Domain Name System)

- **Definition**: Industry standard name resolution system for mapping names to IP addresses.
- **Features**:
  - Hierarchical, distributed database.
  - DNS name servers host authoritative domain data.
  - Uses TCP/UDP port 53.

---

### DoS (Denial of Service)

- **Definition**: A network attack aiming to disrupt a service.
- **Variants**:
  - Distributed DoS (DDoS): Uses a botnet of compromised computers ("zombies").

---

### DOS (Disk Operating System)

- **Definition**: A single-tasking, real-mode operating system developed by Microsoft.
- **Key Fact**: Widely adopted in the 1980s; version 6.3 released in 1993.

---

### DRAM (Dynamic RAM)

- **Definition**: A type of volatile memory storing data as electronic charges in transistors.
- **Features**:
  - Requires periodic refreshing.
  - Standard DRAM is a precursor to modern DDR2/3 SDRAM.

---

### DSL (Digital Subscriber Line)

- **Definition**: Technology for data transfer over voice-grade telephone lines.
- **Features**:
  - Uses higher frequencies of copper lines.
  - Includes various types: ADSL, SDSL, VDSL, and G.SHDSL.

---

### DTP (Desktop Publishing)

- **Definition**: Similar to word processing but focuses on formatting and layout of documents.

---

### Dual Core

- **Definition**: CPU design with two chips in the same package; cost-effective for providing SMP (Symmetric Multiprocessing).

---

### Dumpster Diving

- **Definition**: A social engineering technique of searching discarded materials to gain information about an organization or person.

---

### DVD (Digital Video/Versatile Disk)

- **Definition**: Optical discs with higher capacity (4.7 GB per layer) than CDs.
- **Features**:
  - Recordable and re-writable formats: ±R, ±RW, DVD-RAM.

---

### DVI (Digital Video Interface)

- **Definition**: Video adapter designed to replace VGA ports.
- **Features**:
  - Supports digital-only or digital-and-analog signaling.

---

### Eavesdropping

- **Definition**: The interception of communications over transmission media.
- **Prevention**:
  - Securing transmissions with encryption.

---

### Email

- **Definition**: An electronic store-and-forward messaging system.
- **Features**:
  - Supports text and binary file attachments.
  - Uses protocols:
    - **SMTP** (Simple Mail Transfer Protocol) for forwarding.
    - **POP3** (Post Office Protocol) or **IMAP** (Internet Mail Access Protocol) for accessing mailboxes.

---

### Embedded System

- **Definition**: A computer system designed for specific, dedicated functions.
- **Examples**:
  - Microcontrollers in medical devices.
  - Components managing industrial control systems.

---

### Encryption

- **Definition**: Scrambling characters in a message to make it unreadable without proper decryption.
- **Uses**:
  - Secure data transmission.
  - User authentication.
  - Secure data storage.
- **Levels**: 128-bit encryption is currently considered secure.

---

### Ethernet (802.3)

- **Definition**: Popular Local Area Networking (LAN) technology.
- **Features**:
  - Supports multiple media types: coax (10BASE-5, 10BASE-T), UTP cable (10BASE-TX, 100BASE-TX, 1000BASE-T), and fiber optic (100BASE-FX, 10G).
  - Wireless devices can connect via a Wireless Access Point.

---

### Extranet

- **Definition**: A semi-trusted network of hosts, typically for business partners, suppliers, or customers.
- **Requirement**: Hosts must authenticate to access the extranet.

---

### FAT (File Allocation Table)

- **Definition**: File system used to track file locations on a disk.
- **Versions**:
  - FAT16: Original 16-bit version.
  - FAT32: Enhanced 32-bit version.
  - exFAT: 64-bit version introduced with Windows 7, supported by other OS versions.

---

### Fault Tolerance (Redundancy)

- **Definition**: Protection against system failure by providing redundant capacity.
- **Examples**:
  - Redundant disks (RAID) for data.
  - UPS for emergency power.

---

### Fax

- **Definition**: Transferring document images over a telephone line using fax modems or Multifunction Devices.

---

### File

- **Definition**: A unit of data stored on a computer.
- **Types**:
  - Plain text or binary data.
- **Attributes**:
  - Primary: Read-Only, System, Hidden, Archive.
  - Extended (on NTFS): Access control, compression, encryption.

---

### File Server

- **Definition**: A server providing centralized file and print services.
- **Benefits**:
  - Ease of administration through centralization.

---

### File System

- **Definition**: A standardized format for storing data on a disk.
- **Examples**:
  - Hard disks: FAT16, FAT32, NTFS.
  - Optical media: CDFS (ISO 9660), UDF (Universal Disk Format).

---

### Fingerprint Scanner

- **Definition**: Biometric authentication device comparing a user’s fingerprint template for authentication.

---

### Firewall

- **Definition**: Hardware or software filtering traffic between networks.
- **Types**:
  - Packet-filtering (Layers 3-4 of OSI model).
  - Advanced firewalls: Proxy and stateful inspection (higher-layer filtering).

---

### Firewire (IEEE 1394 Standard)

- **Definition**: Serial SCSI bus standard for high data rates.
- **Applications**:
  - Video cameras.
  - Satellite receivers.
  - Digital media players.

---

### Firmware

- **Definition**: Software instructions stored semi-permanently on hardware.
- **Examples**:
  - BIOS instructions stored in ROM chips.

---

### Flash Memory

- **Definition**: A type of memory that retains information when power is removed and can be reprogrammed quickly.
- **Uses**:
  - USB thumb drives.
  - Memory cards for digital cameras.
  - Solid State Drives (SSD).
  - Hybrid drives (standard hard drives with flash memory cache).

---

### Flatbed Scanner

- **Definition**: A scanner where the object is placed on a glass faceplate and the scan head moves underneath.

---

### Float

- **Definition**: A data type supporting storage of decimal fractions (floating point numbers).

---

### Fn (Function) Keys

- **Definition**: Special command keys on laptop keyboards.
- **Uses**:
  - Adjusting display output.
  - Controlling volume.
  - Disabling wireless radios.

---

### FQDN (Fully Qualified Domain Name)

- **Definition**: A DNS name that specifies a host within a subdomain and top-level domain.

---

### Frame

- **Definition**: The basic unit of data transmitted at Layer 2.
- **Components**:
  - Source and target MAC addresses.
  - Data region.
  - Error-checking region.
- **Role**: Constructed and interpreted by network interface cards.

---

### FSB (Frontside Bus)

- **Definition**: The bus connecting the CPU to the memory controller (system RAM).

---

### FTP (File Transfer Protocol)

- **Definition**: Protocol for transferring files across the Internet.
- **Variants**:
  - SFTP: Secure FTP.
  - FTPS/FTPES: FTP with SSL.
  - TFTP: Trivial FTP.
- **Ports**: Uses ports 20 and 21.

---

### Fuser

- **Definition**: Printer assembly that fixes toner to media.
- **Components**:
  - Heat roller.
  - Pressure roller.
  - Non-contact flash fusing (on high-end printers).

---

### Gesture-based Interaction

- **Definition**: Touchscreen gestures interpreted as events for software responses.
- **Examples**:
  - Taps.
  - Swipes.
  - Pinches.
  - Stretches.

---

### GPS (Global Positioning System)

- **Definition**: A system that determines a receiver's position based on satellite signals.
- **Requirement**: Line-of-sight to GPS satellites.

---

### Group Account

- **Definition**: A collection of user accounts for managing file permissions and user rights efficiently.

---

### GUI (Graphical User Interface)

- **Definition**: Intuitive interface for operating systems.
- **Examples**:
  - Apple Mac OS (1984).
  - Microsoft Windows (WIMP-based: Windows, Icons, Menus, Pointing device).

---

### HDD (Hard Disk Drive)

- **Definition**: High-capacity storage for PCs, using spinning platters with magnetic coating.
- **Types**:
  - Fixed disks (installed in a PC).
  - Portable storage with enclosures.
  - Network Attached Storage (NAS).

---

### HDMI (High Definition Multimedia Interface)

- **Definition**: A high-specification digital connector for audio-video equipment.

---

### Hexadecimal

- **Definition**: Notational system with 16 values per digit (0-9, A-F).
- **Uses**:
  - Compactly referring to long byte values (e.g., MAC and IPv6 addresses).

---

### Homegroup

- **Definition**: A Windows networking feature introduced in Windows 7 to allow home networks to share files and printers through a simple password mechanism.
- **Compatibility**: Not supported in earlier versions of Windows.

---

### Host

- **Definition**: In TCP/IP networking, a "host" is a device that can directly communicate on a network, similar to a node.

---

### Hot Swappable

- **Definition**: A device that can be added or removed without restarting the operating system.

---

### HTML (HyperText Markup Language)

- **Definition**: The language used to create web pages.

---

### HTTP (HyperText Transfer Protocol)

- **Definition**: The protocol used to provide web content to browsers.
- **Ports**:
  - **Port 80**: Standard HTTP.
  - **Port 443**: HTTPS for encrypted transfers using SSL.

---

### I/O (Input/Output) Ports

- **Definition**: Device connections through which data is sent and received.

---

### IEEE (Institute of Electrical and Electronics Engineers)

- **Definition**: A professional organization overseeing the development of electronic standards.
- **Examples**:
  - IEEE 802 protocols for network technologies.

---

### IM (Instant Messaging)

- **Definition**: Real-time text communication with support for file exchange and remote desktop.
- **Security Concerns**:
  - Communications are often unencrypted and unauthenticated.
  - IM traffic can bypass network restrictions by operating over HTTP.

---

### IMAP (Internet Message Access Protocol)

- **Definition**: A protocol allowing a client to access email stored on a remote server while keeping messages on the server.
- **Features**:
  - Mailbox management (e.g., subfolders).
  - Shared mailbox access by multiple clients.
- **Port**: IMAP4 uses TCP port 143.

---

### Implicit Deny

- **Definition**: A security principle where access is denied unless explicitly granted.
- **Example**: Firewall rules with a default "deny all" rule.

---

### Ink Dispersion Printer (Inkjet)

- **Definition**: A printer that sprays ink onto paper through microscopic nozzles.
- **Types**:
  - **Thermal Shock**: Uses heat to form a bubble that bursts through the nozzles.
  - **Piezoelectric**: Uses a tiny element that changes shape to pump the ink.

---

### Integer

- **Definition**: A data type supporting storage of whole numbers.

---

### Intel

- **Definition**: A leading CPU and chipset manufacturer, dominating the PC and laptop market.
- **History**: Provided processors for the first IBM PCs.

---

### Internet

- **Definition**: A global network of networks based on the TCP/IP protocol.
- **Components**: Includes commercial, government, and educational systems routing data across high-speed communication lines.

---

### Internet Appliance

- **Definition**: A SOHO device providing Internet routing via DSL, cable, or satellite links.
- **Features**:
  - 4-port LAN switch.
  - Wi-Fi.
  - Built-in firewall.

---

### Internet of Things (IoT)

- **Definition**: A global network of interconnected devices equipped with sensors, software, and connectivity, such as phones, appliances, and vehicles.

---

### Intranet

- **Definition**: A private network for information processing within a company or organization, using Internet technologies but managed privately.

---

### iOS

- **Definition**: A mobile operating system developed by Apple for iPhone and iPad devices.

---

### IP (Internet Protocol)

- **Definition**: Network (Internet) layer protocol in the TCP/IP suite providing packet addressing and routing for all higher-level protocols in the suite.

---

### IP Address

- **Definition**: Each IP host must have a unique address.
- **Formats**:
  - **IPv4**: 32-bit binary address, expressed as dotted decimal (e.g., `10.0.5.1`).
  - **IPv6**: 128-bit hexadecimal address (e.g., `2001:db8::0bcd:abcd:ef12:1234`).
- **Advantages of IPv6**:
  - Larger address space.
  - Stateless autoconfiguration.
  - Efficient multicast transmissions.

---

### ISP (Internet Service Provider)

- **Definition**: Provides Internet connectivity and other web- and email-related services.
- **Connection Methods**: Includes DSL, cable, or fiber.

---

### Java

- **Definition**: Programming language used for creating web server applications (J2EE) and client-side applications (running in the Java VM).

---

### JavaScript

- **Definition**: Scripting language for adding interactivity to web pages and HTML-format emails.
- **Security Note**: Can be used maliciously to exploit software vulnerabilities; browsers can block scripts through security settings.

---

### Kernel

- **Definition**: The low-level code in an operating system responsible for controlling all other components of the OS.
- **Windows Kernel**: Features multiprocessor awareness and pre-emptive multitasking.

---

### Key (Encryption)

- **Definition**: A value used by encryption algorithms to scramble (encrypt) and unscramble (decrypt) messages.
- **Types**:
  - **Symmetric Encryption**: Uses the same key for both encryption and decryption.
  - **Asymmetric Encryption**: Uses a pair of linked keys (public and private).

---

### Keyboard

- **Definition**: A fundamental PC input device.
- **Interfaces**: Includes PS/2, USB, or wireless (IrDA or Bluetooth).
- **Special Features**: Country-specific designs and additional special keys.

---

### Kinetics

- **Definition**: Mobile device technology using accelerometers and gyroscopes to detect motion and serve as a control system.

---

### Knowledge Base

- **Definition**: A searchable database of product FAQs, troubleshooting advice, and known issues.
- **Example**: Microsoft's Knowledge Base at [support.microsoft.com](http://support.microsoft.com/search).

---

### LAN (Local Area Network)

- **Definition**: A network typically confined to a single geographic location and owned/managed by one organization.

---

### Laptop/Notebook

- **Definition**: A portable computer with functionality similar to a desktop.
- **Features**:
  - Built-in LCD screens and input devices.
  - Power options include AC adapter or battery.
  - Connects peripherals via USB, PCMCIA, or ExpressCard adapters.

---

### Laser Printer

- **Definition**: A printer that uses electrical charges to develop an image with toner, which is then fixed to paper using a fuser.
- **Types**:
  - **Monochrome**: Common for office printing.
  - **Color**: Uses four toner cartridges (Cyan, Magenta, Yellow, Black).

---

### LCD (Liquid Crystal Display) Panel

- **Definition**: Display technology using liquid crystal cells controlled by electrical charges.
- **Advantages**:
  - High-quality images.
  - Compact and lightweight.
- **Limitations**: Best at displaying images at the native resolution.

---

### Least Privilege

- **Definition**: A security principle stating that users or processes should be granted only the minimum necessary rights, privileges, or information to perform their roles.

---

### Libraries

- **Definition**: Virtual folder feature introduced in Windows 7 as a wrapper for multiple folder locations (local or network) storing files that are part of the same logical "collection."
- **Examples**: Default libraries include Documents, Pictures, and Music. Users can add locations or create new libraries.

---

### Licensing

- **Definition**: Terms governing the installation and use of operating system and application software.
- **Scope**: May cover single computer use, multiple devices, or concurrent users at a site.

---

### Lightning

- **Definition**: Proprietary connector and interface for Apple devices.

---

### Linux

- **Definition**: An open-source operating system supported by a wide range of hardware and software vendors.

---

### Liquid Cooling System

- **Definition**: A cooling system that uses water piped around the PC and heatsinks.
- **Advantages**: More efficient cooling, fewer fans, and reduced noise.

---

### LTE (Long Term Evolution)

- **Definition**: Cellular providers' (3GPP) upgrade to 3G technologies like W-CDMA and HSPA.
- **Variant**: LTE Advanced, designed to meet 4G standards.

---

### MAC (Mandatory Access Control)

- **Definition**: Access control model where resources are protected by inflexible, system-defined rules.
- **Privilege Models**: Examples include Bell-LaPadula, Biba, and Clark-Wilson for confidentiality or integrity.

---

### MAC (Media Access Control) Address

- **Definition**: A unique hardware address hard-coded into a network card by the manufacturer.
- **Details**:
  - Used for directing data frames across a network.
  - 48 bits long, with the first half representing the manufacturer's Organizationally Unique Identifier (OUI).

---

### Mailbox

- **Definition**: Part of a message store designed to receive emails for a specific recipient.
- **Aliases**: A mailbox can have multiple email addresses using aliases.

---

### Man-in-the-Middle

- **Definition**: An attack where the attacker intercepts communications between two hosts.

---

### MAPI (Message Application Programming Interface)

- **Definition**: Windows messaging interface, primarily used by Outlook to communicate with Exchange mail servers.

---

### Mapping

- **Definition**: The process of establishing a connection with a file resource on a remote server.
- **Example**: Mapping a network drive.

---

### Markup Language

- **Definition**: A system of tags used to structure a document.
- **Examples**: HTML (HyperText Markup Language), XML (eXtensible Markup Language).

---

### Microsoft

- **Definition**: The world's leading supplier of operating system and Office productivity software.
- **Historical Significance**: Dominated the PC market since the development of IBM-compatible PCs running MS-DOS.

---

### Mobile Device

- **Definition**: Portable phones and smartphones used to interface with workstations via Bluetooth or USB.
- **Security Risks**: Vulnerable to viruses and malware; a risk when taken offsite if they store sensitive information.

---

### Mobile Phone

- **Definition**: UK English term for a cell phone.

---

### Modem (Modulator/Demodulator)

- **Definition**: A device that converts digital computer signals to analog for transmission over public phone lines and vice versa.
- **Forms**: Available as internal or external devices with varying speeds and capabilities.

---

### Motherboard

- **Definition**: Also called the system board, it is the foundation for a computer's hardware, including the processor, RAM, BIOS, and expansion cards.
- **Standards**: Various standards exist with different layouts and advantages.

---

### Mouse

- **Definition**: Essential device for a WIMP GUI, controlling cursor movement to select objects on screen.
- **Features**: Two click buttons (configured for different actions) and often a scroll wheel.
- **Interfaces**: PS/2, USB, or wireless (IrDA or Bluetooth).

---

### MPEG (Moving Pictures Expert Group)

- **Definition**: ISO standards committee for audio and video compression and playback.
- **Standards**:
  - **MPEG-1**: Includes the popular MP3 audio compression format.
  - **MPEG-2**: Widely used for file and broadcast delivery.
  - **MPEG-4 (MP4)**: Extends MPEG-2, supporting Digital Rights Management (DRM) for hardware-tied playback.

---

### Multifactor Authentication

- **Definition**: Strong authentication combining multiple factors:
  - **Something you know** (e.g., a password).
  - **Something you have** (e.g., a smart card).
  - **Something you are** (e.g., a fingerprint).
- **Example**: Using a smart card with a PIN.

---

### Multimedia

- **Definition**: Refers to PC components that can play back and record sound and video, or to the sound/video files themselves.
- **File Formats**:
  - **Windows-specific**: WAV (audio), AVI (video/audio), ASF (compressed as WMA or WMV).
  - **Apple-specific**: MOV, QT, AIFF.
  - **RealNetworks**: RA, RAM.
  - **Standards-based**: MPEG.

---

### Multiprocessing

- **Definition**: Use of two or more processors on a single motherboard to share operations and increase performance.
- **Requirements**:
  - Compatible motherboard.
  - Operating system capable of utilizing multiple processors.
  - Optimized software.
- **Windows Support**: Symmetric Multiprocessing (SMP), allowing up to 2 CPUs.

---

### NAS (Network Attached Storage)

- **Definition**: A storage device with an embedded OS supporting network file access protocols (e.g., TCP/IP, SMB).
- **Security Concerns**:
  - Exploit attacks (embedded OS reduces attack footprint).
  - Unauthorized device connections to the network.

---

### Network

- **Definition**: Two or more computers connected to share data via an appropriate transmission medium.
- **Complexity**: Networks can be interconnected and even link dissimilar networks.

---

### Network Adapter (NIC - Network Interface Card)

- **Definition**: Hardware for physical connection between a host and transmission media.
- **Functions**:
  - Addresses other cards and recognizes data intended for it using the MAC address.
  - Performs error checking.
- **Compatibility**: Specific to network types, speeds, and connectors.

---

### NFC (Nearfield Communications)

- **Definition**: Standard for peer-to-peer radio communication over very short distances (~4 inches).
- **Applications**: Contactless payment and similar technologies.
- **Technology**: Based on RFID.

---

### Notification Area

- **Definition**: Part of the taskbar (right-hand side) displaying background applications and status information.
- **Examples**: Date and time, anti-virus software, network connections, alerts.
- **Legacy Name**: Sometimes called the "system tray."

---

### NTFS (New Technology Filing System)

- **Definition**: A file system with a 64-bit address space.
- **Features**:
  - File-by-file compression.
  - RAID support.
  - Advanced file attribute management.
  - Encryption and disk quotas.

---

### OCR (Optical Character Recognition)

- **Definition**: Software identifying characters and digits in printed images, converting them into editable electronic data files.
- **Advanced Version**: Intelligent Character Recognition (ICR) focuses on handwritten text.

---

### OOP (Object-Oriented Programming)

- **Definition**: A programming technique focused on defining "classes" of objects.
- **Features**:
  - Objects have attributes, methods, and properties.
  - External code interfaces with objects through their public methods and properties.

---

### Open Source

- **Definition**: Software where the programming code is freely available for use, modification, and distribution.

---

### OS X

- **Definition**: Apple's operating system for iMacs, Mac workstations, and MacBook portables.
- **Base**: Built on the BSD version of UNIX.
- **Applications**: Widely supported, especially in design industries (e.g., Adobe/Macromedia).

---

### P2P (Peer-to-Peer)

- **Definition**: File sharing networks where data is distributed among clients.
- **Concerns**:
  - Consumes bandwidth and disk space.
  - Associated with malware and illegal content.

---

### Partition

- **Definition**: A defined storage area on a hard disk.
- **Types**:
  - Master Boot Record (MBR) scheme.
  - GUID Partition Table (GPT) scheme.
- **Features**:
  - Can be formatted with different file systems.
  - Can be marked as active (bootable).

---

### Password

- **Definition**: A secret text string used for authentication.
- **Best Practices**:
  - At least 8 characters with a mix of uppercase, lowercase, numbers, and symbols.
  - Should be stored securely (hashed) and masked during entry.
- **Vulnerabilities**: Subject to guessing and cracking attacks if weak.

---

### Password Cracker

- **Definition**: Software used to guess or crack passwords (e.g., John the Ripper, Cain and Abel).
- **Methods**:
  - Brute force: Trying all possible combinations.
  - Dictionary attacks: Using standard words or phrases.

---

### Password Policy

- **Definition**: Rules to promote secure password practices.
- **Examples**:
  - Enforcing password complexity and expiration.
  - Educating users to avoid reusing or writing down passwords.

---

### Patch Management

- **Definition**: The process of identifying, testing, and deploying updates for OS and applications.
- **Patch Types**: Critical, security-critical, recommended, and optional.

---

### Patent

**A form of intellectual property protection for inventions**:

- **Utility Patent**: Protects functional inventions (e.g., machines, processes). Typically lasts 20 years.
- **Design Patent**: Protects product designs (e.g., smartphone shapes). Typically lasts 15 years.
- **Plant Patent**: Protects new plant varieties (e.g., hybrid crops). Typically lasts 20 years.

---

### PCI (Peripheral Component Interconnect) Bus

- **Definition**: Expansion bus introduced in 1995.
- **Features**:
  - Connects CPU, memory, and peripherals.
  - 32-bit working at 33 MHz.
  - Supports Plug-and-Play, bus mastering, and IRQ steering.

---

### PCI Express

- **Definition**: Latest expansion bus standard.
- **Features**:
  - Serial with point-to-point connections.
  - Links made of one or more lanes (e.g., x1, x2, x4, etc.).
  - Transfer rates per lane:
    - 250 MBps (v1.0).
    - 500 MBps (v2.0).
    - 1 GBps (v3.0).
  - Software compatible with PCI.

---

### PDF (Portable Document Format)

- **Definition**: Adobe's format for distributing finalized documents.

---

### Pentium Processor Series

- **Definition**: Intel's re-positioned premium CPU brand for reliable, always-on systems.

---

### Permissions

- **Definition**: The ability to access files and folders granted by an administrator.
- **Supported By**: NTFS-based Windows systems.

---

---

### Phishing

- **Definition**: Fraudulent attempt to obtain user authentication or financial information.
- **Types**:
  - **Phishing**: Emailing links to fake sites or using malware to steal information.
  - **Pharming**: DNS spoofing to redirect users to fake sites.
  - **Vishing**: Phishing attacks conducted over voice channels (e.g., VoIP).
  - **Spear Phishing/Whaling**: Attacks directed at specific individuals, such as senior executives.

---

### PII (Personally Identifiable Information)

- **Definition**: Data that can identify or contact an individual.
- **Examples**:
  - Social Security number.
  - Names, Date of Birth, email address, phone number, address.
  - Biometric data.

---

### PIM (Personal Information Manager)

- **Definition**: Software for organizing information such as contacts, calendar events, and appointments.

---

### PIN (Personal Identification Number)

- **Definition**: A number used for authentication alongside devices such as smart cards.
- **Purpose**: Ensures the loss of a smart card alone does not represent a security risk.

---

### PKI (Public Key Infrastructure)

- **Definition**: System for linking public-private key pairs with specific users via digital certificates.
- **Components**:
  - **Certificate Authority (CA)**: Issues and guarantees certificates.
  - **Digital Certificates**: Validate user identity.
  - **Trust Relationships**: Established between users and CAs.
- **Policies**:
  - Certificate Policies and Certificate Practice Statements.

---

### Plug-and-Play (PnP)

- **Definition**: A system that auto-configures hardware when added or removed.
- **Requirements**:
  - Compatible BIOS.
  - Operating system.
  - Hardware.

---

### POP (Post Office Protocol)

- **Definition**: Email protocol for accessing messages stored on a remote server.
- **Features**:
  - Messages are deleted from the server after download.
  - POP3 uses TCP port 110.

---

### Popup Blocker

- **Definition**: Software that prevents pop-up windows from opening in a browser.
- **Types of Pop-ups**:
  - Scripts on the host page.
  - Adware or spyware.
  - Flash or Shockwave plug-ins.

---

### Port

- **Definition**: A unique number assigned to application protocols in TCP/UDP.
- **Purpose**: Forms a bi-directional socket for data exchange.
- **Security**:
  - Only required ports should remain open.
  - Ports can be blocked using a firewall.

---

### POST (Power-On Self-Test)

- **Definition**: A hardware check routine built into PC firmware.
- **Checks**:
  - Memory chips, processor, system clock, display, firmware.
  - Errors indicated by beep codes or on-screen messages.
- **Tools**:
  - Interpreter boards for diagnosing boot failures.

---

### Presentation

- **Definition**: Software for creating business presentations.
- **Output**:
  - On-screen slide shows.
  - Printed overhead projector transparencies.

---

### Pre-shared Key

- **Definition**: A shared private key for symmetric encryption (e.g., WEP).
- **Purpose**: Both parties must use the same key securely.
- **Key Generation**:
  - Derived from a passphrase.
  - Passphrase should be longer than a password and include varied characters.

---

### Printer

- **Definition**: Refers to both the physical print device and the associated software components.
- **Software Components**:
  - Spool directory.
  - Printer driver.
  - Configuration information.

---

---

### Privacy Policy

- **Definition**: A policy detailing monitoring and data collection practices.
- **Purpose**:
  - Covers monitoring of employees.
  - Governs data collection from third parties (e.g., customers and suppliers).
  - May need to comply with civil rights and data protection laws in certain jurisdictions.

---

### Product Key

- **Definition**: A unique code used to authenticate software use.
- **Purpose**: Often required for software activation.

---

### Program Files

- **Definition**: Default Windows folder for application executables and supporting files.
- **Notes**:
  - Applications should store user data in user profile folders, not Program Files.
  - In x64 Windows versions:
    - "Program Files" stores 64-bit applications.
    - "Program Files (x86)" stores 32-bit applications.

---

### Projector

- **Definition**: Large-format display device.
- **Technologies**:
  - CRT, LCD, and DLP (market-leading technology).

---

### Protocol

- **Definition**: A set of rules enabling data exchange between systems.
- **Details**:
  - Defines header fields for packets, payload length, and processing methods.
  - Multiple protocols are used within a single network.

---

### Proxy Server

- **Definition**: A server mediating communications between a client and another server.
- **Functions**:
  - Filters and modifies communications.
  - Provides caching to improve performance.

---

### PS/2 Connector

- **Definition**: Port for attaching a keyboard and mouse to a desktop computer.
- **Status**: Largely replaced by USB.

---

### Pseudocode

- **Definition**: Writing program sequences using logical code blocks without specific programming syntax.

---

### Quarantine

- **Definition**: Isolating a virus-infected file or a compromised PC.
- **Functions**:
  - Prevents infected files from being opened.
  - Isolates compromised PCs from networks.

---

### RAID (Redundant Array of Independent/Inexpensive Disks/Devices)

- **Definition**: Technology for configuring multiple hard disks to improve performance and/or fault tolerance.
- **Levels**:
  - RAID 0: No fault tolerance.
  - RAID 1–6: Provide varying levels of fault tolerance and backup.

---

### RAM (Random Access Memory)

- **Definition**: Principal storage for data and program instructions.
- **Characteristics**:
  - Volatile: Data is lost when power is removed or the computer reboots.

---

### Ransomware

- **Definition**: Malware designed to extort money by locking a computer or encrypting files.

---

### RCA Connector

- **Definition**: High-quality A/V connector with a distinctive collar or ring.
- **Origin**: Named after Radio Corporation of America (RCA).
- **Alternate Name**: Phono plug.

---

### RDP (Remote Desktop Protocol)

- **Definition**: Protocol for remote connections to a Windows machine.
- **Features**:
  - Allows specified users to log in remotely.
  - Transfers screen data, mouse, and keyboard input between client and host.
  - Uses TCP port 3389.

---

---

### Recordable CD Drives

- **Definition**: CD/DVD writers used for data transfer and archiving.
- **Formats**:
  - **CD-R**: Write once, read many.
  - **CD-RW**: Rewritable.
- **Techniques**:
  - Laser disruption of disk medium (heating dye, altering magnetic properties, or structural changes).
- **Other Media**:
  - **DVD**: Available in R and RW formats with competing "+" and "-" standards.
  - **Blu-ray**: Recordable (BD-R) and rewritable (BD-RE) formats, supports dual-layer recording.
- **Considerations**:
  - Dual-layer or double-sided recording capabilities.

---

### Recycle Bin

- **Definition**: Temporary storage for deleted files from a local hard disk.
- **Function**: Allows recovery of files unless permanently deleted.

---

### Registry

- **Definition**: Configuration database for Windows.
- **Usage**:
  - Directly editable by experienced personnel.
  - Should be backed up before system changes.

---

### Relational Database

- **Definition**: Structured database storing information in tables.
- **Key Concepts**:
  - **Columns**: Represent data fields.
  - **Rows**: Represent records.
  - **Relationships**: Link a primary key field in one table to a foreign key field in another.
- **Schema**: Overall structure of the database.

---

### Remote Wipe

- **Definition**: Software allowing remote deletion of data and settings on a mobile device.

---

### Removable Media

- **Definition**: Interim storage medium for sharing files.
- **Examples**:
  - Floppy disks, optical discs, tape drives, high-capacity disks, removable hard drives.

---

### Resolution

- **Definition**: Measure of image clarity, described in pixels per inch (ppi).
- **Printer Resolution**:
  - Measured in dots per inch (dpi).
  - Multiple print dots required to accurately represent a single image pixel.

---

### RF (Radio Frequency)

- **Definition**: Radio waves propagating at different frequencies and wavelengths.
- **Wi-Fi Frequencies**:
  - 2.4 GHz or 5 GHz.

---

### RFID (Radio Frequency IDentification)

- **Definition**: Wireless-readable chip.
- **Applications**: Barcodes and smart cards.

---

### RJ (Registered Jack) Connector

- **Definition**: Connector used for twisted pair cabling.
- **Types**:
  - **RJ-45**: Used for 4-pair network cabling.
  - **RJ-11**: Used for modem/telephone 2-pair cabling.

---

### Role-Based Access Control

- **Definition**: Access control model where permissions are assigned based on job function.
- **Characteristics**:
  - ACLs managed by administrators.
  - Users assigned permissions by role.

---

### Router

- **Definition**: Device linking dissimilar networks.
- **Functions**:
  - Supports multiple paths based on speed, traffic, and cost.
  - Operates at Layer 3 (Network) of the OSI model.
  - Enables subnet division and alternate path tracking.

---

### Rule-Based Access Control

- **Definition**: Access control model following system-enforced rules.
- **Examples**:
  - Firewalls, MAC, and role-based models.
- **Non-Rule-Based Example**:
  - DAC, where decisions are made by resource owners.

---

---

### SATA (Serial ATA)

- **Definition**: Serial ATA allows for faster transfer rates and longer, more compact cabling compared to standard IDE/ATA.
- **Features**:
  - 7-pin data connector.
  - Bandwidths of 1.5 Gbps, 3 Gbps, and 6 Gbps.
  - 15-pin power connector (adapters available for 4-pin Molex).
- **External Drives**: Supported via eSATA interface.

---

### Satellite

- **Definition**: System of microwave transmissions relaying signals between terrestrial receivers or other orbital satellites.
- **Internet Connectivity**:
  - Requires a reception antenna and DVB-S modem.

---

### Scanner

- **Definition**: Device converting the image of a physical object into an electronic data file.
- **Components**:
  - Lamp for illumination.
  - Array of CCDs (Charge Coupled Devices) for recording.
- **Types**:
  - Flatbed or sheet-fed (often integrated into multifunction devices).
- **Outputs**: Printer or file formats (JPEG, PNG, TIFF).
- **Interfaces**: TWAIN, WIA, SANE, ISIS.

---

### Scalability

- **Definition**: The ability of a system, network, or process to expand usage without increasing costs at the same rate.

- **Examples**:

  - A database system supporting additional users or larger datasets without significant performance loss.
  - Cloud services that can scale resources up or down based on demand.

- **Features**:
  - Ensures consistent performance under varying workloads.
  - Can involve horizontal scaling (adding more machines) or vertical scaling (adding more resources to an existing machine).
  - Focuses on optimizing cost efficiency as usage grows.

---

### Script Support

- **Definition**: Many web pages use scripts for rich content or navigation.
- **Risks**:
  - Exploitation of browser/OS vulnerabilities.
  - Annoying behaviors (e.g., pop-ups).
- **Browser Settings**: Enable/disable scripting on a site-by-site basis.

---

### SD (Secure Digital) Card

- **Definition**: One of the first types of flash memory card.

---

### SDRAM (Synchronous DRAM)

- **Definition**: DRAM chip variant running at the system clock speed for faster refresh cycles.
- **Status**: Replaced by DDR/DDR2/3 SDRAM.

---

### Security Control

- **Definition**: Technology or procedure mitigating vulnerabilities and risk to ensure Confidentiality, Integrity, and Availability (CIA) of information.
- **Types**: Technical, operational, and management.

---

### Server

- **Definition**: A system or software that provides shared resources to clients over a network.
- **Functions**:
  - Centralized administration and security for network resources.
  - Requires careful configuration and maintenance.
- **Security**:
  - Protect with firewalls and secure configurations, especially for Internet-facing servers.

---

### Service

- **Definition**: Background functions on Windows (e.g., Plug-and-Play, print spooler, DHCP client).
- **Management**:
  - Configured via the Services console or `msconfig`.
  - Viewed and managed using Task Manager's Processes tab.

---

### Share

- **Definition**: Any resource (folder, printer, etc.) made available on a network.
- **Requirement**: Enable Windows File and Print Sharing.

---

### Shortcut

- **Definition**: Item pointing to a program or data file, typically placed on the desktop or Start menu.

---

### Shoulder Surfing

- **Definition**: Social engineering tactic to obtain someone's password or PIN by observing as they type it.

---

### Smart Card

- **Definition**: Card with a chip storing data, typically used for authentication.
- **Data Stored**: Digital certificates or other authentication credentials.

---

### Smartphone

- **Definition**: Mobile device combining phone functionality with general-purpose computing.
- **Features**:
  - Web browsing, email, and apps.
  - Screen sizes typically 4–5.5 inches.

---

---

### SMTP (Simple Mail Transfer Protocol)

- **Definition**: Protocol used to send mail between hosts on the Internet.
- **Port**: TCP port 25.

---

### Social Engineering

- **Definition**: Hacking technique involving deception to gain useful organizational information.
- **Methods**:
  - Impersonation
  - Domination
  - Charm
- **Reference**: Popularized by Kevin Mitnick in _The Art of Deception_.

---

### SOHO (Small Office Home Office)

- **Definition**: Refers to network devices designed for small-scale LANs (up to 10 users).

---

### SP (Service Pack)

- **Definition**: Collection of software updates and hotfixes released as one installable file.
- **Features**: Often includes new OS features.

---

### Spam

- **Definition**: Junk messages sent via email (or instant messaging \[SPIM]).
- **Mitigation**:
  - Filters and blacklists.
  - Prevent open relays on mail servers.

---

### Spoofing

- **Definition**: Attack where the attacker disguises their identity.
- **Examples**:
  - IP spoofing: Changing IP address.
  - Phishing: Setting up a false website.

---

### Spreadsheet

- **Definition**: Table of rows, columns, and cells where formulas can be applied for calculations.

---

### Spyware

- **Definition**: Malicious software recording information about a PC and its user.
- **Purpose**: Gather passwords or financial information like credit card details.

---

### SSID (Service Set ID)

- **Definition**: Identifies a specific Wireless LAN (WLAN).
- **Extended SSID (ESSID)**: Multiple APs configured with the same SSID.

---

### SSL (Secure Sockets Layer)

- **Definition**: Protocol developed by Netscape for privacy and authentication over the Internet.
- **Details**:
  - Works at layer 5 (Session).
  - Uses PKI (X.509 certificates).
  - Successor: Transport Layer Security (TLS).

---

### SSO (Single Sign-on)

- **Definition**: Authentication technology allowing a user to authenticate once for multiple services.
- **Example**: Kerberos.

---

### Start Menu

- **Definition**: Standard interface in Windows 7 and earlier to locate and load applications.
- **Evolution**: Layout and features vary across Windows versions.

---

### Start Screen

- **Definition**: User interface introduced with Windows 8 to replace the Start Menu.
- **Features**:
  - Manages Windows devices using a touchscreen.
  - Configurable to show Start Screen or Desktop at startup.

---

### String

- **Definition**: Data type supporting storage of a variable-length series of characters.

---

### Stylus

- **Definition**: Pointing device used with a digitizer, often employed as a drawing tool.

---

### Subnet Mask

- **Definition**: Used to distinguish the Network ID and Host ID in an IP address.
- **Format**:
  - Standard: 255.255.0.0.
  - Classless: 169.254.0.0/16 (where `/16` is the number of bits in the mask).
  - IPv6 uses similar `/nn` notation for network prefixes.

---

---

### Switch

- **Definition**: Ethernet (LAN) switches perform functions of a specialized bridge.
- **Operation**:
  - Receives incoming data into a buffer.
  - Compares destination MAC address with an address table.
  - Sends data only to the port with the corresponding MAC address.
- **Benefits**:
  - Each port in a switched network is a separate collision domain (microsegmentation).
  - Collisions cannot occur.
- **Advanced Functionality**:
  - Routing at layer 3 (IP), 4 (TCP), or 7 (Application).
  - Layer 4/7 switches are called load balancers and content switches.

---

### System Requirements

- **Definition**: Minimum hardware specifications needed to run an OS or software application.
- **Key Factors**:
  - CPU speed
  - Memory
  - Hard disk capacity
- **Notes**:
  - Software will not run if minimum requirements are unmet.
  - Performance may be slow if recommended requirements are not met.

---

### Tablet

- **Definition**: Ultra-portable laptop with a touchscreen.
- **Popularized By**: Apple's iPad devices running iOS.
- **Features**:
  - Form factors with 7" or 10" screens.
  - Devices running Android, iOS, or Windows (e.g., Microsoft Surface).
  - Smaller devices (phablets) resemble large smartphones.

---

### Tailgating

- **Definition**: Social engineering technique to gain unauthorized access by following someone into a building.

---

### Task Manager

- **Definition**: Program to recover stalled applications and control running tasks and system resources.
- **Access**:
  - `Ctrl+Shift+Esc`
  - `Ctrl+Alt+Del`
  - Alt-clicking the taskbar.

---

### Task Scheduler

- **Definition**: Enables automation of actions like running programs or scripts based on a schedule or triggers.

---

### Taskbar

- **Definition**: Interface to locate running programs, containing:
  - Start menu
  - System tray/notification area
  - Optional Quick Launch toolbar
- **Default Position**: Bottom of the desktop.

---

### TCP (Transmission Control Protocol)

- **Definition**: Transport layer protocol in the TCP/IP suite.
- **Features**:
  - Provides connection-oriented, guaranteed delivery of packets.
  - Relatively slow due to overhead of establishing sessions and acknowledging packets.

---

### TCP/IP

- **Definition**: Network protocol suite widely used for operating systems and the Internet.
- **Characteristics**:
  - Industry standard, vendor-independent, and open.
  - 4-layer model:
    - **Network Interface**: Physical/Data Link layers.
    - **Internet**: Network layer.
    - **Transport**: Transport layer.
    - **Application**: Session, Presentation, and Application layers.

---

### TFT (Thin Film Transistor) Active Matrix Display

- **Definition**: High-resolution flat-panel LCD display.
- **Features**:
  - High image clarity.
  - Contrast ratios: 150:1 to 200:1.
  - Fast refresh rates.
  - Wide viewing angles.

---

### Thumb Drive

- **Definition**: Flash memory card with USB adapter.

---

### Thunderbolt

- **Definition**: Interface developed by Intel, primarily used on Apple devices.
- **Features**:
  - Functions as a display interface (like DisplayPort).
  - Serves as a general peripheral interface (like USB 3).

---

### TKIP (Temporal Key Integrity Protocol)

- **Definition**: Mechanism in WPA to improve wireless encryption security over WEP.

---

### Token

- **Definition**: Contains authentication data.
- **Types**:
  - **Software Token**: Generated by logon systems (e.g., Kerberos) for Single Sign-on.
  - **Hardware Token**: Device with:
    - Digital certificate.
    - One-time password generation for two-factor authentication.

---

---

### Toner

- **Definition**: Specially formulated compound used in laser printers and photocopiers to impart dye to paper through an electrographic process.
- **Key Properties**:
  - **Colorant**: Dye used for coloring.
  - **Fusibility**: Wax or plastic compound for adhesion.
  - **Charge Holding**: Ability to maintain an electrostatic charge.
- **Types**:
  - **Dual Component**: Toner mixed with a separate magnetic developer.
  - **Mono-Component**: Magnetic toner.
  - **Non-Magnetic Mono-Component**: Static transfer toner.

---

### Touchpad

- **Definition**: Input device used on laptops as a mouse replacement.
- **Features**:
  - Cursor control by finger movement.
  - Recognizes "tap" events.
  - May have scroll areas and buttons.

---

### Touchscreen

- **Definition**: Display screen that responds to touch input.

---

### Trademark

- **Common Law Trademark**:
  - **Definition**: Automatically gained through mark usage in commerce.
  - **Protection**: Limited to local use; harder to enforce legally.
  - **Symbol**: ™ or SM.
  - **Cost**: Free.
  - **Examples**: Local business names or logos.
- **Registered Trademark**:
  - **Definition**: Granted by a trademark authority (e.g., USPTO).
  - **Protection**: Nationwide or international; strong legal rights.
  - **Symbol**: ®.
  - **Cost**: Filing and renewal fees.
  - **Examples**: Nike swoosh, Apple logo.

---

### Transfer Rate

- **Definition**: Amount of data transferred over a connection in a given time.
- **Measurements**:
  - Typically in bits or bytes per second (or suitable multiples).
- **Notes**:
  - Often quoted as peak or theoretical maximum.
  - Sustained throughput is typically lower.

---

### Trojan Horse

- **Definition**: Malicious software disguised as innocuous software.
- **Purpose**: Compromise the security of the target system.

---

### Troubleshooting

- **Steps**:
  1. **Backup**: Ensure data is backed up.
  2. **Gather Information**: From user, error messages, diagnostics, or inspection.
  3. **Analyze Problem**: Consult documentation, web resources, or manufacturer's help.
  4. **Categorize Issue**: Example: hardware vs. software.
  5. **Apply Solution**: Select and implement the most suitable fix.
  6. **Test System**: Verify functionality and ensure related systems are unaffected.
  7. **Document Issue**: Record the problem, steps taken, and outcomes.
  8. **Escalation**: If unresolved, escalate to another technician or manager.

---

### TWAIN

- **Definition**: Standard "driver" model for interfacing scanners with applications.

---

### UAC (User Account Control)

- **Definition**: Windows security system to restrict misuse of administrative privileges.
- **Features**:
  - Prompts for user authorization for administrative actions.
  - Allows installation of hardware/software without switching accounts.

---

### UDF (Universal Disk Format)

- **Definition**: File system for optical media, replacing CDFS (ISO 9660).

---

### UDP (User Datagram Protocol)

- **Definition**: Transport layer protocol in the TCP/IP suite.
- **Features**:
  - Connectionless, non-guaranteed communication.
  - Faster than TCP but lacks reliability and flow control.

---

### UNC (Universal Naming Convention)

- **Definition**: Microsoft standard for naming local network resources.
- **Format**: `\\server\share\file`
  - **server**: Remote machine name.
  - **share**: Folder on the remote machine.
  - **file**: File within the folder.

---

### Unicode

- **Definition**: Extensible system of code pages supporting millions of character glyphs.
- **Purpose**: Enables representation of international alphabets.

---

### UNIX

- **Definition**: Family of related operating systems originally developed by AT\&T.
- **Features**:
  - Supports parallel processing.
  - Runs on various platforms.
  - Offers multiple file systems.
  - Forms the backbone of Internet servers.
  - Uses TCP/IP for network compatibility.

---

### Updates

- **Definition**: Fixes or improvements provided by software manufacturers.
- **Types**:
  - **Hotfixes**: For selected customers, addressing limited problems.
  - **Patches**: Generally available fixes.
  - **Service Packs**: Installable collections of patches and improvements.

---

---

### UPS (Uninterruptible Power Supplies)

- **Definition**: Provides an alternative AC power supply during power failures.
- **Components**:
  - Array of batteries.
  - Charging circuit.
  - Inverter for DC to AC conversion.
  - Circuit for seamless power supply takeover.
  - Surge, spike, and brownout protection (may include line conditioner).

---

### URL (Uniform Resource Locator/Identifier)

- **Definition**: Application-level addressing scheme for TCP/IP, offering human-readable resource addresses.
- **Format**: `protocol://server/file`
  - **Protocol**: Type of resource (e.g., HTTP, FTP).
  - **Server**: Name of the host computer (e.g., `www.microsoft.com`).
  - **File**: Resource being accessed.
- **Note**: "URI" (Uniform Resource Indicator) is the preferred term in standards.

---

### USB (Universal Serial Bus)

- **Definition**: Interface allowing up to 127 peripheral connections.
- **Connectors**:
  - **Type A**: Larger connector for hosts.
  - **Type B**: Device connectors (also Mini-/Micro- versions).
- **Specifications**:
  - **USB 1.1**: 12 Mbps.
  - **USB 2.0**: 480 Mbps (backward compatible with 1.1).
  - **USB 3.0**: 4.8 Gbps SuperSpeed, supports 4.5W power delivery.
- **Features**: Hot-swappable, devices can draw power (up to 2.5W).

---

### Variable

- **Definition**: Identifier for a value that can change during program execution.
- **Usage**: Declared with a specific data type.

---

### Vector

- **Definition**: Identifier for a group of variables of the same type.
- **Features**: The number of elements can vary during execution.

---

### VGA (Video Graphics Array) Connector

- **Definition**: 15-pin HD analog connector for graphics adapters.
- **Status**: Becoming obsolete due to the rise of digital displays.

---

### Video Card

- **Definition**: Interface between a computer's graphics components and display device.
- **Features**:
  - Connectors: VGA, DVI, HDMI.
  - Receives information from the CPU and uses video RAM.
  - May support analog, digital, or both outputs.
  - Includes a GPU (Graphics Processing Unit) and onboard memory.

---

### Video Conferencing

- **Definition**: Software for virtual meetings with options for:
  - Voice.
  - Video.
  - Instant messaging.

---

### Video Standards

- **Definition**: Define resolution and color depth for graphics adapters and displays.
- **Examples**:
  - **VGA**: 640x480, 16 colors.
  - **SVGA**: 800x600, True Color (24-bit).
  - **XGA Variants**: Resolutions greater than 1024x768, some widescreen.

---

### Virtual Memory

- **Definition**: Hard disk area allocated to contain memory pages when physical RAM is insufficient.
- **Usage**:
  - Also known as paging or swapping.
  - Stores pages of memory in the paging (or swap) file.
  - Frees physical RAM for active tasks.

---

### Virtualization Technology

- **Definition**: Software enabling a single host computer to run multiple guest operating systems (VMs).
- **Features**:
  - Configured via a hypervisor or VM Monitor (VMM).
  - VMs can connect using virtual networks (vSwitch) or host's interfaces.
  - Allows sharing data with the host (e.g., shared folders, clipboard).
- **Applications**: Used in data centers, testing, and training.

---

### Virus

- **Definition**: Malicious code designed to infect files or disks and perform harmful actions.
- **Examples**:
  - Deleting files.
  - Altering system settings.

---

---

### VM (Virtual Machine)

- **Definition**: A separate environment for running 32-bit processes or multiple operating systems on a single host PC.
- **Usage**:
  - **Protected Mode**: Programs are protected from each other.
  - **Virtualization Software**: Hypervisors like Microsoft Hyper-V or VMware enable hosting multiple operating systems.

---

### VoIP (Voice over IP)

- **Definition**: Internet telephony that carries voice traffic over data networks.
- **Features**:
  - Integrates with fixed and mobile telephone networks.
  - Used in converged networks (voice and data on the same network).
- **Security Implications**:
  - Vulnerabilities include DoS attacks and eavesdropping.
  - Converged networks represent a single point of failure.

---

### VPN (Virtual Private Network)

- **Definition**: A secure tunnel between two endpoints connected via an unsecure network (e.g., the Internet).
- **Security**: Created using SSL/TLS or IPsec to ensure data privacy.

---

### WAN (Wide Area Network)

- **Definition**: A network spanning a large geographical area, incorporating multiple sites.
- **Connections**:
  - Telephone lines.
  - Fiber optic cables.
  - Satellite links.

---

### Web Application

- **Definition**: Software run from a web server and accessed via a web browser.

---

### Web Server

- **Definition**: HTTP servers hosting websites.
- **Features**:
  - Serve static HTML pages or dynamic front-end applications for databases.
  - Common for intranet services, especially on Microsoft networks.
- **Security**:
  - Targets for DoS, spoofing, and software exploits.
  - Should be placed in a DMZ if not hosted by a third party.

---

### Webcam

- **Definition**: A device for recording video, available in standalone units or integrated into laptops.
- **Features**:
  - Early devices had low resolution.
  - Modern devices are HD-capable.

---

### WEP (Wired Equivalent Privacy)

- **Definition**: Mechanism for encrypting data on wireless connections.
- **Security**:
  - Uses 64-bit RC4 cipher (later updated to 128-bit).
  - Considered flawed and replaced by WPA.

---

### WIA (Windows Image Acquisition)

- **Definition**: Driver model and API for interfacing scanner hardware with applications on Windows PCs.

---

### Wi-Fi

- **Definition**: IEEE standard for wireless networking using spread spectrum radio transmission.
- **Frequency Bands**: Operates in 2.4 GHz and 5 GHz bands.
- **Iterations**:
  - Standards include `a`, `b`, `g`, `n`, and `ac`.

---

### Windows

- **Definition**: Microsoft's ubiquitous operating system.
- **History**:
  - **Windows 3.1**: 16-bit with rudimentary network facilities.
  - **Windows NT**: Reliable 32-bit operations with secure networking.
  - **Windows 9x**: Home and business versions with lower reliability.
  - **Windows 2000**: Combined NT's reliability with 9x's interface and hardware flexibility.
  - **Windows XP**: Featured editions like Home, Professional, and 64-bit.
  - **Windows Vista/7**: Introduced Aero interface and security improvements.
  - **Windows 8/10**: Designed for touchscreen devices.
- **Server Versions**:
  - **Windows Server 2003/2008/2012/2016**: Introduced Active Directory and advanced features.

---

### Windows Defender

- **Definition**: Anti-malware tool included in Windows.
- **History**:
  - **Vista/7**: Provided anti-spyware protection.
  - **Windows 8**: Evolved into a full anti-malware scanner protecting against viruses, worms, Trojans, and spyware.

---

---

### Windows Explorer

- **Definition**: Standard interface for managing files and folders in Windows.
- **Renaming**: Known as **File Explorer** starting with Windows 10.

---

### Windows Firewall

- **Definition**: Built-in firewall enabled by default on all network and dial-up connections.
- **Advanced Features**:
  - Includes outbound port filtering.
  - Configurable through an advanced interface.

---

### Windows Update

- **Definition**: Website hosting patches and security updates for Microsoft Windows.
- **Feature**: The **Automatic Update** function allows Windows to connect and download updates automatically.

---

### Wireless

- **Definition**: Network connectivity using electromagnetic broadcast spectrum as the medium.
- **Transport Methods**:
  - Primarily uses spread-spectrum radio.
  - Microwave transmitters and infrared are also options.
- **Peripheral Connectivity**: Wireless can also refer to connecting peripherals to a computer.

---

### WLAN (Wireless Local Area Network)

- **Definition**: A network using wireless radio communications based on variants of the 802.11 standards.

---

### Word Processing

- **Definition**: Applications for writing and editing documents.
- **Features**:
  - Editing, formatting, and reviewing text quickly.

---

### Workgroup

- **Definition**: A peer-to-peer network of computers sharing resources.
- **Characteristics**:
  - No centralized directory.
  - Suitable for small networks.

---

### Worm

- **Definition**: A type of virus that spreads through memory and network connections rather than infecting files.

---

### WORM (Write Once, Read Many) Drive

- **Definition**: Drive capable of writing data to a recordable CD only once.
- **Usage**: The written data can be read multiple times.

---

### WPA (Wi-Fi Protected Access)

- **Definition**: Improved encryption scheme for securing Wi-Fi communications, designed to replace WEP.
- **Versions**:
  - **WPA**: Improved key distribution and authentication.
  - **WPA2**: Replaced TKIP and RC4 with the more secure AES cipher.

---

### WPS (Wi-Fi Protected Setup)

- **Definition**: Mechanism for auto-configuring a WLAN securely for home users.
- **Methods**:
  - Push-button configuration for compatible equipment.
  - PIN-based configuration for non-push-button adapters.

---

### XML (eXtensible Markup Language)

- **Definition**: A system for structuring documents to be both human- and machine-readable.
- **Usage**: Information is placed within tags that describe the document's structure.

---

### Zero Day Exploit

- **Definition**: Attack exploiting a software vulnerability unknown to the vendor and users.
- **Significance**: These vulnerabilities have high destructive potential because no patch is available at the time of exploitation.
