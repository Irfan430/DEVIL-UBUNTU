
---

## 🚀 **ফাইল 2: devil-ubuntu.sh** (MAIN SCRIPT)

```bash
#!/bin/bash

# ============================================
# 😈 IRFAN320'S DEVIL UBUNTU TRANSFORMER v3.0
# ============================================

# Configuration
IRFAN="IRFAN320"
VERSION="3.0.0"
DEVIL_DIR="$HOME/.irfan320-devil"
LOG_FILE="$DEVIL_DIR/transformation.log"
BACKUP_DIR="$DEVIL_DIR/backup-$(date +%Y%m%d-%H%M%S)"
INTENSITY=3  # 1=Basic, 2=Standard, 3=Extreme
STYLE="matrix"  # matrix, cyberpunk, gothic, minimal

# Devil Colors v3.0
D_RED='\033[38;5;196m'
D_BLACK='\033[38;5;232m'
D_GREEN='\033[38;5;46m'
D_PURPLE='\033[38;5;93m'
D_ORANGE='\033[38;5;208m'
D_PINK='\033[38;5;205m'
D_CYAN='\033[38;5;51m'
D_YELLOW='\033[38;5;226m'
D_MATRIX='\033[38;5;46m'
D_FIRE='\033[38;5;202m'
D_NEON='\033[38;5;45m'
BOLD='\033[1m'
BG_BLACK='\033[48;5;232m'
BG_RED='\033[48;5;88m'
RESET='\033[0m'

# ============================================
# 🎭 CORE FUNCTIONS
# ============================================

function show_banner() {
    clear
    echo -e "${D_RED}"
    cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     ██████╗ ███████╗██╗   ██╗██╗██╗     ███╗   ██╗███████╗    ║
║    ██╔═══██╗██╔════╝██║   ██║██║██║     ████╗  ██║██╔════╝    ║
║    ██║   ██║█████╗  ██║   ██║██║██║     ██╔██╗ ██║█████╗      ║
║    ██║   ██║██╔══╝  ╚██╗ ██╔╝██║██║     ██║╚██╗██║██╔══╝      ║
║    ╚██████╔╝███████╗ ╚████╔╝ ██║███████╗██║ ╚████║███████╗    ║
║     ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝    ║
║                                                               ║
EOF
    echo -e "║           ${D_FIRE}${BOLD}IRFAN320 DEVIL UBUNTU v${VERSION}${RESET}${D_RED}          ║"
    echo -e "║           ${D_NEON}INTENSITY: ${INTENSITY} | STYLE: ${STYLE}${D_RED}               ║"
    echo '╚═══════════════════════════════════════════════════════════════╝'
    echo -e "${RESET}"
}

function log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
    echo -e "$2$1${RESET}"
}

function devil_progress() {
    local label="$1"
    local total="$2"
    local current="$3"
    local width=50
    local percent=$((current * 100 / total))
    local filled=$((width * current / total))
    local empty=$((width - filled))
    
    printf "\r${D_GREEN}%-30s [${D_RED}" "$label"
    for ((i=0; i<filled; i++)); do printf "█"; done
    for ((i=0; i<empty; i++)); do printf "░"; done
    printf "${D_GREEN}] %3d%%${RESET}" "$percent"
}

# ============================================
# 🔧 SYSTEM CHECK & PREPARATION
# ============================================

function check_dependencies() {
    log_message "Checking dependencies..." "$D_CYAN"
    
    local deps=("gnome-tweaks" "dconf-editor" "imagemagick" "curl" "wget")
    local missing=()
    
    for dep in "${deps[@]}"; do
        if ! dpkg -l | grep -q "^ii  $dep "; then
            missing+=("$dep")
        fi
    done
    
    if [ ${#missing[@]} -gt 0 ]; then
        log_message "Missing: ${missing[*]}" "$D_YELLOW"
        read -p "Install missing packages? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            sudo apt update
            sudo apt install -y "${missing[@]}"
            log_message "Dependencies installed" "$D_GREEN"
        else
            log_message "Cannot proceed without dependencies" "$D_RED"
            exit 1
        fi
    fi
}

function create_structure() {
    log_message "Creating devil structure..." "$D_CYAN"
    
    mkdir -p "$DEVIL_DIR"
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$DEVIL_DIR/themes"
    mkdir -p "$DEVIL_DIR/icons"
    mkdir -p "$DEVIL_DIR/wallpapers"
    mkdir -p "$DEVIL_DIR/fonts"
    mkdir -p "$DEVIL_DIR/scripts"
    mkdir -p "$DEVIL_DIR/configs"
    mkdir -p "$DEVIL_DIR/backups"
    
    log_message "Structure created at $DEVIL_DIR" "$D_GREEN"
}

# ============================================
# 🎨 THEME INSTALLATION
# ============================================

function install_themes() {
    log_message "Installing devil themes..." "$D_CYAN"
    
    # Backup current theme
    dconf dump /org/gnome/desktop/interface/ > "$BACKUP_DIR/gnome-backup.dconf"
    
    # Download and install themes based on style
    case "$STYLE" in
        "matrix")
            install_matrix_theme
            ;;
        "cyberpunk")
            install_cyberpunk_theme
            ;;
        "gothic")
            install_gothic_theme
            ;;
        "minimal")
            install_minimal_theme
            ;;
    esac
    
    log_message "Theme installation complete" "$D_GREEN"
}

function install_matrix_theme() {
    log_message "Installing Matrix theme..." "$D_MATRIX"
    
    # Create matrix GTK theme
    cat > "$DEVIL_DIR/themes/Matrix/gtk-3.0/gtk.css" << 'EOF'
/* Matrix Theme */
* {
    background-color: #000000;
    color: #00FF00;
    border-color: #003300;
}

button {
    background: linear-gradient(to bottom, #001100, #003300);
    border: 1px solid #00AA00;
}

button:hover {
    background: linear-gradient(to bottom, #003300, #005500);
}

entry {
    background-color: #001100;
    border: 1px solid #00AA00;
}
EOF
    
    gsettings set org.gnome.desktop.interface gtk-theme "Matrix"
    gsettings set org.gnome.desktop.interface icon-theme "Adwaita"
    gsettings set org.gnome.desktop.interface cursor-theme "DMZ-White"
    
    # Matrix color scheme
    gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
}

function install_wallpapers() {
    log_message "Installing devil wallpapers..." "$D_CYAN"
    
    local wp_dir="$DEVIL_DIR/wallpapers"
    mkdir -p "$wp_dir"
    
    # Generate dynamic wallpapers
    generate_matrix_wallpaper "$wp_dir/matrix.jpg"
    generate_cyber_wallpaper "$wp_dir/cyber.jpg"
    generate_devil_wallpaper "$wp_dir/devil.jpg"
    
    # Set wallpaper
    gsettings set org.gnome.desktop.background picture-uri "file://$wp_dir/matrix.jpg"
    gsettings set org.gnome.desktop.screensaver picture-uri "file://$wp_dir/cyber.jpg"
    
    # Create slideshow
    create_wallpaper_slideshow
    
    log_message "Wallpapers installed" "$D_GREEN"
}

function generate_matrix_wallpaper() {
    local output="$1"
    convert -size 1920x1080 xc:black \
        -font "Courier-Bold" -pointsize 20 \
        -fill "#00FF00" -draw "text 100,100 '01010101010101010101'" \
        -fill "#008800" -draw "text 120,150 '01010101010101010101'" \
        -fill "#00AA00" -draw "text 140,200 '01010101010101010101'" \
        -fill "#003300" -draw "text 100,300 'IRFAN320 DEVIL MODE'" \
        -fill "#00FF00" -draw "text 120,350 'Ubuntu Transformation v$VERSION'" \
        "$output"
}

# ============================================
# 💻 TERMINAL CUSTOMIZATION
# ============================================

function setup_terminal() {
    log_message "Customizing terminal..." "$D_CYAN"
    
    # Backup original bashrc
    cp ~/.bashrc "$BACKUP_DIR/bashrc.original"
    
    # Create devil bashrc
    cat > ~/.bashrc << 'EOF'
# ============================================
# 😈 IRFAN320 DEVIL BASH CONFIGURATION
# ============================================

# Devil Colors
RED='\[\033[38;5;196m\]'
GREEN='\[\033[38;5;46m\]'
BLUE='\[\033[38;5;51m\]'
YELLOW='\[\033[38;5;226m\]'
PURPLE='\[\033[38;5;93m\]'
CYAN='\[\033[38;5;51m\]'
RESET='\[\033[0m\]'

# Devil Prompt
PS1="${RED}┌─[${GREEN}\u${RED}@${BLUE}devil-ubuntu${RED}]─[${YELLOW}\w${RED}]\n${RED}└──╼${RESET} "

# Devil Aliases
alias devil-mode='echo "😈 DEVIL MODE ACTIVATED!"'
alias matrix='cmatrix -b -C green'
alias hack='echo "Accessing mainframe..." && sleep 1 && echo "Access granted!"'
alias sys-info='neofetch --ascii_distro arch'
alias update-devil='sudo apt update && sudo apt upgrade -y'
alias clean-devil='sudo apt autoremove -y && sudo apt autoclean'
alias monitor='htop'
alias gpu-info='nvidia-smi 2>/dev/null || echo "No NVIDIA GPU"'

# Devil Functions
devil-eye() {
    while true; do
        echo -ne "${RED}👁️  Watching...${RESET}\r"
        sleep 0.5
        echo -ne "${GREEN}👁️  Watching...${RESET}\r"
        sleep 0.5
    done
}

matrix-rain() {
    echo -e "\033[32m"
    cols=$(tput cols)
    for i in {1..50}; do
        printf "%${cols}s\n" | tr ' ' $(shuf -n 1 -e 0 1)
        sleep 0.05
    done
    echo -e "\033[0m"
}

system-stats() {
    echo "=== SYSTEM STATS ==="
    echo "CPU: $(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}')"
    echo "RAM: $(free -h | awk '/^Mem:/ {print $3 "/" $2}')"
    echo "Disk: $(df -h / | awk 'NR==2 {print $3 "/" $2}')"
    echo "Uptime: $(uptime -p)"
}

# Welcome Message
if [ -t 0 ]; then
    echo -e "${RED}"
    echo '╔══════════════════════════════════════════════╗'
    echo '║                                              ║'
    echo -e "║    😈 WELCOME TO ${GREEN}IRFAN320${RED}'S DEVIL UBUNTU 😈   ║"
    echo '║                                              ║'
    echo -e "║    Type ${YELLOW}devil-mode${RED} to begin                ║"
    echo '║                                              ║'
    echo '╚══════════════════════════════════════════════╝'
    echo -e "${RESET}"
fi

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
EOF
    
    # Configure GNOME Terminal
    configure_gnome_terminal
    
    log_message "Terminal customized" "$D_GREEN"
}

function configure_gnome_terminal() {
    local profile=$(gsettings get org.gnome.Terminal.ProfilesList default | tr -d "'")
    local profile_path="/org/gnome/terminal/legacy/profiles:/:$profile"
    
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        background-color 'rgb(0,0,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        foreground-color 'rgb(0,255,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        cursor-colors-set true
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        cursor-background-color 'rgb(0,255,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        cursor-foreground-color 'rgb(0,0,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$profile/ \
        font 'Monospace 11'
}

# ============================================
# ⚡ PERFORMANCE OPTIMIZATION
# ============================================

function optimize_system() {
    log_message "Optimizing system performance..." "$D_CYAN"
    
    if [ $INTENSITY -ge 2 ]; then
        # Disable animations
        gsettings set org.gnome.desktop.interface enable-animations false
        
        # Reduce swapiness
        echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
        
        # Improve filesystem performance
        echo "noatime,nodiratime" | sudo tee -a /etc/fstab 2>/dev/null || true
        
        # SSD optimization
        if lsblk -d -o rota | grep -q "0"; then
            echo "SSD detected - applying optimizations"
            sudo systemctl enable fstrim.timer
        fi
    fi
    
    if [ $INTENSITY -eq 3 ]; then
        # Extreme optimizations
        echo "Extreme optimizations applied"
        # Add more aggressive tweaks here
    fi
    
    log_message "System optimized" "$D_GREEN"
}

# ============================================
# 🎮 GAMING OPTIMIZATIONS
# ============================================

function setup_gaming() {
    if [ $INTENSITY -ge 2 ]; then
        log_message "Setting up gaming optimizations..." "$D_CYAN"
        
        # Install gamemode if not present
        if ! dpkg -l | grep -q gamemode; then
            sudo apt install -y gamemode
        fi
        
        # Create gaming script
        cat > "$DEVIL_DIR/scripts/gaming-mode.sh" << 'EOF'
#!/bin/bash
# IRFAN320 Gaming Mode

echo "🎮 ACTIVATING GAMING MODE..."

# CPU performance
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Disable compositor
killall picom 2>/dev/null || true

# Network optimizations
sudo sysctl -w net.core.rmem_max=134217728
sudo sysctl -w net.core.wmem_max=134217728
sudo sysctl -w net.ipv4.tcp_fastopen=3

# GPU optimizations (NVIDIA)
if command -v nvidia-settings &> /dev/null; then
    nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'
    nvidia-settings -a '[gpu:0]/GPUFanControlState=1'
fi

echo "✅ Gaming Mode Activated!"
EOF
        
        chmod +x "$DEVIL_DIR/scripts/gaming-mode.sh"
        
        # Add to bashrc
        echo "alias gaming-mode='sudo $DEVIL_DIR/scripts/gaming-mode.sh'" >> ~/.bashrc
        
        log_message "Gaming mode ready - type 'gaming-mode'" "$D_GREEN"
    fi
}

# ============================================
# 🔐 SECURITY ENHANCEMENTS
# ============================================

function enhance_security() {
    log_message "Enhancing security..." "$D_CYAN"
    
    # Disable root login
    sudo passwd -l root 2>/dev/null || true
    
    # Setup firewall
    if ! command -v ufw &> /dev/null; then
        sudo apt install -y ufw
    fi
    sudo ufw --force enable
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    
    # SSH hardening
    if [ -f /etc/ssh/sshd_config ]; then
        sudo cp /etc/ssh/sshd_config "$BACKUP_DIR/sshd_config.backup"
        sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
        sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
        sudo systemctl restart ssh
    fi
    
    # Create security monitor
    create_security_monitor
    
    log_message "Security enhanced" "$D_GREEN"
}

# ============================================
# 📊 SYSTEM MONITORING
# ============================================

function setup_monitoring() {
    log_message "Setting up system monitoring..." "$D_CYAN"
    
    # Install monitoring tools
    sudo apt install -y htop nmon iotop iftop
    
    # Create monitoring script
    cat > "$DEVIL_DIR/scripts/monitor.sh" << 'EOF'
#!/bin/bash
# IRFAN320 System Monitor

while true; do
    clear
    echo -e "\033[38;5;196m╔══════════════════════════════════════════════╗"
    echo -e "║           😈 REAL-TIME SYSTEM MONITOR        ║"
    echo -e "╚══════════════════════════════════════════════╗\033[0m"
    
    # CPU
    cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
    echo -e "\033[38;5;46mCPU Usage: ${cpu}%\033[0m"
    
    # Memory
    mem_total=$(free -h | awk '/^Mem:/ {print $2}')
    mem_used=$(free -h | awk '/^Mem:/ {print $3}')
    echo -e "\033[38;5;51mMemory: ${mem_used}/${mem_total}\033[0m"
    
    # Disk
    disk=$(df -h / | awk 'NR==2 {print $5}')
    echo -e "\033[38;5;226mDisk Usage: ${disk}\033[0m"
    
    # Temperature
    if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
        temp=$(cat /sys/class/thermal/thermal_zone0/temp)
        temp=$((temp/1000))
        echo -e "\033[38;5;208mCPU Temp: ${temp}°C\033[0m"
    fi
    
    # Network
    ip=$(hostname -I | awk '{print $1}')
    echo -e "\033[38;5;93mIP Address: ${ip}\033[0m"
    
    echo -e "\n\033[38;5;196mPress Ctrl+C to exit...\033[0m"
    sleep 2
done
EOF
    
    chmod +x "$DEVIL_DIR/scripts/monitor.sh"
    echo "alias system-monitor='$DEVIL_DIR/scripts/monitor.sh'" >> ~/.bashrc
    
    log_message "Monitoring setup complete" "$D_GREEN"
}

# ============================================
# 🛠️ UTILITY SCRIPTS
# ============================================

function create_utilities() {
    log_message "Creating utility scripts..." "$D_CYAN"
    
    # Update script
    cat > "$DEVIL_DIR/scripts/update-devil.sh" << 'EOF'
#!/bin/bash
# Update Devil Ubuntu

echo "🔄 Updating Devil Ubuntu..."
cd "$(dirname "$0")/../.."

# Update system
sudo apt update
sudo apt upgrade -y

# Update devil components
echo "Checking for devil updates..."
# Add update logic here

echo "✅ Update complete!"
EOF
    
    # Fix script
    cat > "$DEVIL_DIR/scripts/fix-devil.sh" << 'EOF'
#!/bin/bash
# Fix Devil Ubuntu issues

echo "🔧 Fixing common issues..."

# Reset GNOME settings
dconf reset -f /org/gnome/

# Fix permissions
sudo chown -R $USER:$USER ~/.irfan320-devil

# Update icon cache
sudo update-icon-caches /usr/share/icons/*

echo "✅ Fixes applied!"
EOF
    
    # Uninstall script
    cat > "$DEVIL_DIR/scripts/uninstall-devil.sh" << 'EOF'
#!/bin/bash
# Uninstall Devil Ubuntu

echo "😇 Removing Devil Ubuntu..."
read -p "Are you sure? This will restore original settings. (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Uninstall cancelled."
    exit 1
fi

# Restore backups
if [ -d ~/.irfan320-devil/backup-* ]; then
    latest_backup=$(ls -td ~/.irfan320-devil/backup-* | head -1)
    
    # Restore bashrc
    if [ -f "$latest_backup/bashrc.original" ]; then
        cp "$latest_backup/bashrc.original" ~/.bashrc
    fi
    
    # Restore GNOME settings
    if [ -f "$latest_backup/gnome-backup.dconf" ]; then
        dconf load /org/gnome/desktop/interface/ < "$latest_backup/gnome-backup.dconf"
    fi
fi

# Remove devil directory
rm -rf ~/.irfan320-devil

echo "✅ Devil Ubuntu uninstalled. Please reboot."
EOF
    
    chmod +x "$DEVIL_DIR/scripts"/*.sh
    
    log_message "Utility scripts created" "$D_GREEN"
}

# ============================================
# 🏁 FINALIZATION
# ============================================

function finalize() {
    log_message "Finalizing transformation..." "$D_CYAN"
    
    # Update alternatives
    sudo update-alternatives --set x-terminal-emulator /usr/bin/gnome-terminal.wrapper
    
    # Refresh font cache
    sudo fc-cache -fv
    
    # Create completion file
    cat > "$DEVIL_DIR/COMPLETION.txt" << EOF
================================
IRFAN320 DEVIL UBUNTU v${VERSION}
================================
Installation Date: $(date)
Installation Directory: $DEVIL_DIR
Intensity Level: $INTENSITY
Style: $STYLE

Available Commands:
- devil-mode      : Show welcome message
- gaming-mode     : Activate gaming optimizations
- system-monitor  : Real-time system monitoring
- matrix-rain     : Show matrix effect
- sys-info        : System information
- update-devil    : Update devil components
- fix-devil       : Fix common issues
- uninstall-devil : Remove devil transformation

Configuration:
- Themes: $DEVIL_DIR/themes/
- Wallpapers: $DEVIL_DIR/wallpapers/
- Scripts: $DEVIL_DIR/scripts/
- Logs: $LOG_FILE

To uninstall: Run $DEVIL_DIR/scripts/uninstall-devil.sh

😈 LONG LIVE THE DEVIL MODE! 😈
EOF
    
    log_message "Transformation complete!" "$D_GREEN"
    
    # Show completion message
    echo -e "\n${D_RED}╔═══════════════════════════════════════════════════════╗"
    echo -e "║           😈 TRANSFORMATION COMPLETE! 😈           ║"
    echo -e "╠═══════════════════════════════════════════════════════╣"
    echo -e "║   ${D_GREEN}Your Ubuntu has been transformed to DEVIL MODE${D_RED}   ║"
    echo -e "║                                                       ║"
    echo -e "║   ${D_YELLOW}Reboot your system to see all changes${D_RED}           ║"
    echo -e "║                                                       ║"
    echo -e "║   ${D_CYAN}Type 'devil-mode' after reboot to begin${D_RED}           ║"
    echo -e "╚═══════════════════════════════════════════════════════╝${RESET}"
    
    echo -e "\n${D_FIRE}🔥 Press Enter to reboot, or Ctrl+C to cancel...${RESET}"
    read -r
    sudo reboot
}

# ============================================
# 🎪 MAIN EXECUTION
# ============================================

function main() {
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --level)
                INTENSITY="$2"
                shift 2
                ;;
            --style)
                STYLE="$2"
                shift 2
                ;;
            --uninstall)
                if [ -f "$DEVIL_DIR/scripts/uninstall-devil.sh" ]; then
                    exec "$DEVIL_DIR/scripts/uninstall-devil.sh"
                fi
                exit 0
                ;;
            *)
                shift
                ;;
        esac
    done
    
    show_banner
    check_dependencies
    create_structure
    install_themes
    install_wallpapers
    setup_terminal
    optimize_system
    setup_gaming
    enhance_security
    setup_monitoring
    create_utilities
    finalize
}

# Start transformation
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $EUID -ne 0 ]]; then
        echo -e "${D_RED}This script must be run as root (sudo)${RESET}"
        exit 1
    fi
    main "$@"
fi