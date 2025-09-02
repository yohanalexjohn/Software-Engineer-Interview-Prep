# Embedded Linux

- Linux distributions specifically designed for embedded systems-devices with limited resources, specific hardware requirements and specific functionality

## Boot sequence general Linux

1. BIOS/UEFI loads the bootloader
2. Bootloader loads the Linux Kernel into memory
3. Kernel Initialises Hardware, mounts root file system
4. Init/systemd starts user-space processes and services

## Embedded Linux Stack

┌─────────────────────────────────────┐
│         Embedded Linux Stack        │
├─────────────────────────────────────┤
│         Application Layer           │
│      (Custom applications)          │
├─────────────────────────────────────┤
│         System Services             │
│      (Init system, networking)      │
├─────────────────────────────────────┤
│         Linux Kernel                │
│      (Optimized for target)         │
├─────────────────────────────────────┤
│         Bootloader                  │
│      (U-Boot, GRUB, etc.)           │
├─────────────────────────────────────┤
│         Hardware Layer              │
│      (Target-specific)              │
└─────────────────────────────────────┘

## Build System Philosophy

Automate the process of creating custom distributions. They handle dependency resolutions, 
cross compilation and system integration to produce bootable images 

### Core Component

1. Package Management: Source code, patches and configuration 
2. Build Environment: Cross Compilation tool chains
3. Dependency Resolution: Package relationships and conflicts 
4. Image Generation: Bootable System Images
5. Configuration Management: System and package configuration

## Build root Framework

1. Lightweight build system that creates embedded Linux systems from source code.

### Core Components 

┌─────────────────────────────────────┐
│         Buildroot Structure         │
├─────────────────────────────────────┤
│         Config.in                   │
│      (Package selection)            │
├─────────────────────────────────────┤
│         Rules.mak                   │
│      (Build rules)                  │
├─────────────────────────────────────┤
│         Package/                    │
│      (Package definitions)          │
├─────────────────────────────────────┤
│         Board/                      │
│      (Board configurations)         │
├─────────────────────────────────────┤
│         Configs/                    │
│      (Default configurations)       │
└─────────────────────────────────────┘

## YOCTO 

┌─────────────────────────────────────┐
│         Yocto Architecture          │
├─────────────────────────────────────┤
│         BitBake                     │
│      (Build engine)                 │
├─────────────────────────────────────┤
│         OpenEmbedded Core           │
│      (Build system)                 │
├─────────────────────────────────────┤
│         Meta Layers                 │
│      (Configuration & packages)     │
├─────────────────────────────────────┤
│         Build Output                │
│      (Images, packages, SDK)        │
└─────────────────────────────────────┘
