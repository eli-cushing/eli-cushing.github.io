# Module 3: Using Computer Hardware <!-- omit in toc -->

### 0.0.1. Table of Contents

- [1. System Components](#1-system-components)
  - [1.1. Selecting a Computer](#11-selecting-a-computer)
    - [1.1.1. Central Processing Unit (CPU)](#111-central-processing-unit-cpu)
    - [1.1.2. Memory (System Ram)](#112-memory-system-ram)
    - [1.1.3. Fixed Disk](#113-fixed-disk)
    - [1.1.4. Graphics Processing Unit (GPU)](#114-graphics-processing-unit-gpu)
    - [1.1.5. Network Interface](#115-network-interface)
  - [1.2. Motherboard Components](#12-motherboard-components)
  - [1.3. Processors](#13-processors)
    - [1.3.1. Intel CPU Brands](#131-intel-cpu-brands)
    - [1.3.2. AMD CPU Brands](#132-amd-cpu-brands)
    - [1.3.3. ARM CPUs](#133-arm-cpus)
  - [1.4. Features of Processors](#14-features-of-processors)
    - [1.4.1. Instruction Set (32-versus 64-bit)](#141-instruction-set-32-versus-64-bit)
    - [1.4.2. Clock Speed and Bus Speed](#142-clock-speed-and-bus-speed)
    - [1.4.3. Multiprocessing and Dual-core](#143-multiprocessing-and-dual-core)
  - [1.5. System and Expansion Bus Technologies](#15-system-and-expansion-bus-technologies)
  - [1.6. System Cooling](#16-system-cooling)
    - [1.6.1. Heatsinks and Thermal Paste](#161-heatsinks-and-thermal-paste)
    - [1.6.2. Liquid-based Cooling Systems](#162-liquid-based-cooling-systems)
  - [1.7. BIOS and UEFI System Firmware](#17-bios-and-uefi-system-firmware)
    - [1.7.1. System Firmware Setup Program](#171-system-firmware-setup-program)
    - [1.7.2. UEFI Setup Programs](#172-uefi-setup-programs)
- [2. Using Device Interfaces](#2-using-device-interfaces)
  - [2.1. Computer Port and Connector Types](#21-computer-port-and-connector-types)
  - [2.2. USB and Firewire](#22-usb-and-firewire)
    - [2.2.1. USB Ports and Connectors](#221-usb-ports-and-connectors)
    - [2.2.2. USB Data Rates](#222-usb-data-rates)
    - [2.2.3. Firewire](#223-firewire)
  - [2.3. Graphics Devices](#23-graphics-devices)
    - [2.3.1. Resolution and Color Depth](#231-resolution-and-color-depth)
  - [2.4. Graphics Device Interfaces](#24-graphics-device-interfaces)
    - [2.4.1. High Definition Multimedia Interface (HDMI)](#241-high-definition-multimedia-interface-hdmi)
    - [2.4.2. DisplayPort and Thunderbolt](#242-displayport-and-thunderbolt)
    - [2.4.3. Digital Visual Interface (DVI)](#243-digital-visual-interface-dvi)
    - [2.4.4. Video Graphics Array](#244-video-graphics-array)
  - [2.5. Input Devices](#25-input-devices)
    - [2.5.1. Keyboard](#251-keyboard)
    - [2.5.2. Mouse](#252-mouse)
    - [2.5.3. Laptop Keyboards and Touchpads](#253-laptop-keyboards-and-touchpads)
    - [2.5.4. Stylus Pen](#254-stylus-pen)
  - [2.6. Configuring Peripherals](#26-configuring-peripherals)
    - [2.6.1. Configuing a Mouse](#261-configuing-a-mouse)
    - [2.6.2. Configuring a Keyboard](#262-configuring-a-keyboard)
    - [2.6.3. Keyboard Regionalization](#263-keyboard-regionalization)
    - [2.6.4. Configuring a Pen/Stylus](#264-configuring-a-penstylus)
  - [2.7. Bluetooth](#27-bluetooth)
    - [2.7.1. Configuring Bluetooth](#271-configuring-bluetooth)
    - [2.7.2. Disabling Bluetooth](#272-disabling-bluetooth)
  - [2.8. RF and Near Field Communications (NFC)](#28-rf-and-near-field-communications-nfc)
  - [2.9. Network Interfaces](#29-network-interfaces)
    - [2.9.1. Ethernet Connector (RJ-45)](#291-ethernet-connector-rj-45)
    - [2.9.2. Telephone Connector (RJ-11)](#292-telephone-connector-rj-11)
- [3. Using Peripheral Devices](#3-using-peripheral-devices)
  - [3.1. Installing and Uninstalling Peripherals](#31-installing-and-uninstalling-peripherals)
    - [3.1.1. Plug-and-Play Installation](#311-plug-and-play-installation)
    - [3.1.2. Manual Driver Installation](#312-manual-driver-installation)
    - [3.1.3. Devices and Printers](#313-devices-and-printers)
    - [3.1.4. Removing and Uninstalling Devices](#314-removing-and-uninstalling-devices)
    - [3.1.5. IP-based Peripherals and Web Configurations](#315-ip-based-peripherals-and-web-configurations)
  - [3.2. Display Devices](#32-display-devices)
    - [3.2.1. Flat-screen Displays](#321-flat-screen-displays)
    - [3.2.2. Touchscreens](#322-touchscreens)
    - [3.2.3. Digital Projectors](#323-digital-projectors)
  - [3.3. Display Settings](#33-display-settings)
    - [3.3.1. Screen Resolution](#331-screen-resolution)
    - [3.3.2. Installing and Configuring Dual Monitors](#332-installing-and-configuring-dual-monitors)
    - [3.3.3. Configuring a Touchscreen](#333-configuring-a-touchscreen)
  - [3.4. Multimedia Ports and Devices](#34-multimedia-ports-and-devices)
    - [3.4.1. Audio Settings](#341-audio-settings)
    - [3.4.2. Changing the Volume](#342-changing-the-volume)
    - [3.4.3. Webcams](#343-webcams)
  - [3.5. Printer Types](#35-printer-types)
  - [3.6. Installing and Configuring a Printer](#36-installing-and-configuring-a-printer)
    - [3.6.1. Configuring Printers](#361-configuring-printers)
    - [3.6.2. Printer Properties and Preferences](#362-printer-properties-and-preferences)
  - [3.7. Scanners and Cameras](#37-scanners-and-cameras)
    - [3.7.1. Types of Scanners](#371-types-of-scanners)
    - [3.7.2. Scanning a Document](#372-scanning-a-document)
    - [3.7.3. Digital Cameras](#373-digital-cameras)
- [4. Using Storage Devices](#4-using-storage-devices)
  - [4.1. System Memory](#41-system-memory)
    - [4.1.1. DRAM](#411-dram)
    - [4.1.2. SDRAM](#412-sdram)
    - [4.1.3. Double Data Rate](#413-double-data-rate)
  - [4.2. Mass Storage Devices](#42-mass-storage-devices)
    - [4.2.1. Hard Disk Drives](#421-hard-disk-drives)
    - [4.2.2. HDD Capacity and Performace](#422-hdd-capacity-and-performace)
    - [4.2.3. HDD Interfaces](#423-hdd-interfaces)
    - [4.2.4. External Hard Drives](#424-external-hard-drives)
    - [4.2.5. Solid State Drives (SSD)](#425-solid-state-drives-ssd)
  - [4.3. Optical Discs and Drives](#43-optical-discs-and-drives)
    - [4.3.1. Recordable and Rewritable Optical Discs](#431-recordable-and-rewritable-optical-discs)
    - [4.3.2. DVD Media](#432-dvd-media)
    - [4.3.3. Blu-ray Discs](#433-blu-ray-discs)
    - [4.3.4. Optical Drive Units](#434-optical-drive-units)
  - [4.4. Removable Flash Memory Devices](#44-removable-flash-memory-devices)
- [5. Using File Systems](#5-using-file-systems)
  - [5.1. Managing the File System](#51-managing-the-file-system)
    - [5.1.1. Hard Disk Partition](#511-hard-disk-partition)
    - [5.1.2. Windows Drives](#512-windows-drives)
    - [5.1.3. File Systems](#513-file-systems)
    - [5.1.4. File System Features](#514-file-system-features)
  - [5.2. Folders and Directories](#52-folders-and-directories)
    - [5.2.1. Windows System Folders](#521-windows-system-folders)
    - [5.2.2. Linux Directories](#522-linux-directories)
  - [5.3. File Explorer](#53-file-explorer)
    - [5.3.1. Navigation Pane](#531-navigation-pane)
    - [5.3.2. User Profiles and Libraries](#532-user-profiles-and-libraries)
    - [5.3.3. Creating a Folder](#533-creating-a-folder)
  - [5.4. Files](#54-files)
    - [5.4.1. File Types and Extensions](#541-file-types-and-extensions)
    - [5.4.2. Creating and Opening Files](#542-creating-and-opening-files)
    - [5.4.3. File Explorer Options](#543-file-explorer-options)
    - [5.4.4. Renaming Files and Folders](#544-renaming-files-and-folders)
    - [5.4.5. Copying and Moving Files](#545-copying-and-moving-files)
    - [5.4.6. Deleting Files and the Recycle Bin](#546-deleting-files-and-the-recycle-bin)
    - [5.4.7. Selecting Multiple Files and Folders](#547-selecting-multiple-files-and-folders)
  - [5.5. File Attributes and Permissions](#55-file-attributes-and-permissions)
    - [5.5.1. File Properties Dialog](#551-file-properties-dialog)
    - [5.5.2. Folder and File Permissions](#552-folder-and-file-permissions)
  - [5.6. Searching for Folders and Files](#56-searching-for-folders-and-files)
    - [5.6.1. File Explorer Search](#561-file-explorer-search)
    - [5.6.2. View, Group, and Filter Options](#562-view-group-and-filter-options)
  - [5.7. File Types and Extensions](#57-file-types-and-extensions)
    - [5.7.1. Word Processing Software](#571-word-processing-software)
    - [5.7.2. Spreadsheet Software](#572-spreadsheet-software)
    - [5.7.3. Presentation Software](#573-presentation-software)
    - [5.7.4. PDF Viewers and Creators](#574-pdf-viewers-and-creators)
    - [5.7.5. Image File Types](#575-image-file-types)
    - [5.7.6. Video File Types](#576-video-file-types)
    - [5.7.7. Audio File Types](#577-audio-file-types)
    - [5.7.8. Executable Files](#578-executable-files)
    - [5.7.9. Compression Formats](#579-compression-formats)

### 0.0.2. Domain Objectives

    | **Domain**                              | Objectives/Examples                                                                                                                                                                                                                                                                                                                                                                            |
    | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Unit 3.1 / System Components            | **2.3 Explain the purpose of common internal computing components.** <br> • Motherboard/system board <br> • Firmware/BIOS <br> • RAM <br> • ARM CPU (Mobile phone, Tablet) <br> • 32-bit CPU (Laptop, Workstation, Server) <br> • 64-bit CPU (Laptop, Workstation, Server) <br> • Storage (Hard drive, SSD) <br> • GPU <br> • Cooling <br> • NIC (Wired vs. wireless, Onboard vs. add-on card) |
    | Unit 3.2 / Using Device Interfaces      | **2.1 Classify common types of input/output device interfaces.** <br> • Networking: <br> - Wired \[Telephone connector (RJ-11), Ethernet connector (RJ-45)] <br> - Wireless \[Bluetooth, NFC] <br> • Peripheral device: USB, FireWire, Thunderbolt, Bluetooth, RF <br> • Graphic device: VGA, HDMI, DVI, DisplayPort, Mini-DisplayPort                                                         |
    |                                         | **2.2 Given a scenario, set up and install common peripheral devices to a laptop/PC.** <br> • Devices: Keyboard, Mouse                                                                                                                                                                                                                                                                         |
    | Unit 3.3 / Using Peripheral Devices 2.2 | **Given a scenario, set up and install common peripheral devices to a laptop/PC.** <br> • Devices: Printer, Scanner, Camera, Speakers, Display <br> • Installation types: Plug-and-play vs. driver installation, Other required steps, IP-based peripherals, Web-based configuration steps                                                                                                     |
    |                                         | **3.1 Manage applications and software.** <br> • Device management                                                                                                                                                                                                                                                                                                                             |
    |                                         | **3.2 Compare and contrast components of an operating system.** <br> • Drivers                                                                                                                                                                                                                                                                                                                 |
    | Unit 3.4 / Using Storage Devices        | **2.2 Given a scenario, set up and install common peripheral devices to a laptop/PC.** <br> • Devices: External hard drive                                                                                                                                                                                                                                                                     |
    |                                         | **2.5 Compare and contrast storage types.** <br> • Volatile vs. non-volatile <br> • Local storage types: RAM, Hard drive (Solid state vs. spinning disk), Optical, Flash drive                                                                                                                                                                                                                 |
    | Unit 3.5 / Using File Systems           | **3.2 Compare and contrast components of an operating system.** <br> • File systems and features: File systems, NTFS, FAT32, HFS, Ext4 <br> • Features: Compression, Encryption, Permissions, Journaling, Limitations, Naming rules <br> • File management: Folders/directories, File types and extensions, Permissions                                                                        |

# 1. System Components

## 1.1. Selecting a Computer

### 1.1.1. Central Processing Unit (CPU)

### 1.1.2. Memory (System Ram)

### 1.1.3. Fixed Disk

### 1.1.4. Graphics Processing Unit (GPU)

### 1.1.5. Network Interface

## 1.2. Motherboard Components

## 1.3. Processors

### 1.3.1. Intel CPU Brands

### 1.3.2. AMD CPU Brands

### 1.3.3. ARM CPUs

## 1.4. Features of Processors

### 1.4.1. Instruction Set (32-versus 64-bit)

### 1.4.2. Clock Speed and Bus Speed

### 1.4.3. Multiprocessing and Dual-core

## 1.5. System and Expansion Bus Technologies

## 1.6. System Cooling

### 1.6.1. Heatsinks and Thermal Paste

### 1.6.2. Liquid-based Cooling Systems

## 1.7. BIOS and UEFI System Firmware

### 1.7.1. System Firmware Setup Program

### 1.7.2. UEFI Setup Programs

# 2. Using Device Interfaces

## 2.1. Computer Port and Connector Types

## 2.2. USB and Firewire

### 2.2.1. USB Ports and Connectors

### 2.2.2. USB Data Rates

### 2.2.3. Firewire

## 2.3. Graphics Devices

### 2.3.1. Resolution and Color Depth

## 2.4. Graphics Device Interfaces

### 2.4.1. High Definition Multimedia Interface (HDMI)

### 2.4.2. DisplayPort and Thunderbolt

### 2.4.3. Digital Visual Interface (DVI)

### 2.4.4. Video Graphics Array

## 2.5. Input Devices

### 2.5.1. Keyboard

### 2.5.2. Mouse

### 2.5.3. Laptop Keyboards and Touchpads

### 2.5.4. Stylus Pen

## 2.6. Configuring Peripherals

### 2.6.1. Configuing a Mouse

### 2.6.2. Configuring a Keyboard

### 2.6.3. Keyboard Regionalization

### 2.6.4. Configuring a Pen/Stylus

## 2.7. Bluetooth

### 2.7.1. Configuring Bluetooth

### 2.7.2. Disabling Bluetooth

## 2.8. RF and Near Field Communications (NFC)

## 2.9. Network Interfaces

### 2.9.1. Ethernet Connector (RJ-45)

### 2.9.2. Telephone Connector (RJ-11)

# 3. Using Peripheral Devices

## 3.1. Installing and Uninstalling Peripherals

### 3.1.1. Plug-and-Play Installation

### 3.1.2. Manual Driver Installation

### 3.1.3. Devices and Printers

### 3.1.4. Removing and Uninstalling Devices

### 3.1.5. IP-based Peripherals and Web Configurations

## 3.2. Display Devices

### 3.2.1. Flat-screen Displays

### 3.2.2. Touchscreens

### 3.2.3. Digital Projectors

## 3.3. Display Settings

### 3.3.1. Screen Resolution

### 3.3.2. Installing and Configuring Dual Monitors

### 3.3.3. Configuring a Touchscreen

## 3.4. Multimedia Ports and Devices

### 3.4.1. Audio Settings

### 3.4.2. Changing the Volume

### 3.4.3. Webcams

## 3.5. Printer Types

## 3.6. Installing and Configuring a Printer

### 3.6.1. Configuring Printers

### 3.6.2. Printer Properties and Preferences

## 3.7. Scanners and Cameras

### 3.7.1. Types of Scanners

### 3.7.2. Scanning a Document

### 3.7.3. Digital Cameras

# 4. Using Storage Devices

## 4.1. System Memory

### 4.1.1. DRAM

### 4.1.2. SDRAM

### 4.1.3. Double Data Rate

## 4.2. Mass Storage Devices

### 4.2.1. Hard Disk Drives

### 4.2.2. HDD Capacity and Performace

### 4.2.3. HDD Interfaces

### 4.2.4. External Hard Drives

### 4.2.5. Solid State Drives (SSD)

## 4.3. Optical Discs and Drives

### 4.3.1. Recordable and Rewritable Optical Discs

### 4.3.2. DVD Media

### 4.3.3. Blu-ray Discs

### 4.3.4. Optical Drive Units

## 4.4. Removable Flash Memory Devices

# 5. Using File Systems

## 5.1. Managing the File System

### 5.1.1. Hard Disk Partition

### 5.1.2. Windows Drives

### 5.1.3. File Systems

### 5.1.4. File System Features

## 5.2. Folders and Directories

### 5.2.1. Windows System Folders

### 5.2.2. Linux Directories

## 5.3. File Explorer

### 5.3.1. Navigation Pane

### 5.3.2. User Profiles and Libraries

### 5.3.3. Creating a Folder

## 5.4. Files

### 5.4.1. File Types and Extensions

### 5.4.2. Creating and Opening Files

### 5.4.3. File Explorer Options

### 5.4.4. Renaming Files and Folders

### 5.4.5. Copying and Moving Files

### 5.4.6. Deleting Files and the Recycle Bin

### 5.4.7. Selecting Multiple Files and Folders

## 5.5. File Attributes and Permissions

### 5.5.1. File Properties Dialog

### 5.5.2. Folder and File Permissions

## 5.6. Searching for Folders and Files

### 5.6.1. File Explorer Search

### 5.6.2. View, Group, and Filter Options

## 5.7. File Types and Extensions

### 5.7.1. Word Processing Software

### 5.7.2. Spreadsheet Software

### 5.7.3. Presentation Software

### 5.7.4. PDF Viewers and Creators

### 5.7.5. Image File Types

### 5.7.6. Video File Types

### 5.7.7. Audio File Types

### 5.7.8. Executable Files

### 5.7.9. Compression Formats
