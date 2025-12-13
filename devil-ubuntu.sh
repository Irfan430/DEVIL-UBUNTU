#!/bin/bash

# ============================================
# 😈 IRFAN320'S DEVIL UBUNTU TRANSFORMER v2.0
# ============================================

# Devil Colors v2.0
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
BOLD='\033[1m'
BG_BLACK='\033[48;5;232m'
BG_RED='\033[48;5;88m'
RESET='\033[0m'

# Irfan320's Signature
IRFAN="IRFAN320"
DEVIL_NAME="DEVIL-UBUNTU"
VERSION="2.0.0"
EMAIL="devil@irfan320.com"

# Configuration
DEVIL_DIR="$HOME/.irfan320-devil"
LOG_FILE="$DEVIL_DIR/devil.log"
BACKUP_DIR="$DEVIL_DIR/backup-$(date +%Y%m%d-%H%M%S)"

# ============================================
# 🎭 DEVIL ANIMATION FUNCTIONS
# ============================================

function show_devil_banner() {
    clear
    echo -e "${D_RED}"
    echo '╔═══════════════════════════════════════════════════════════════╗'
    echo '║                                                               ║'
    echo '║     ██████╗ ███████╗██╗   ██╗██╗██╗     ███╗   ██╗███████╗    ║'
    echo '║    ██╔═══██╗██╔════╝██║   ██║██║██║     ████╗  ██║██╔════╝    ║'
    echo '║    ██║   ██║█████╗  ██║   ██║██║██║     ██╔██╗ ██║█████╗      ║'
    echo '║    ██║   ██║██╔══╝  ╚██╗ ██╔╝██║██║     ██║╚██╗██║██╔══╝      ║'
    echo '║    ╚██████╔╝███████╗ ╚████╔╝ ██║███████╗██║ ╚████║███████╗    ║'
    echo '║     ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝    ║'
    echo '║                                                               ║'
    echo -e "║           ${D_FIRE}WELCOME TO ${IRFAN}'S ${DEVIL_NAME} v${VERSION}${D_RED}          ║"
    echo '║                                                               ║'
    echo '╚═══════════════════════════════════════════════════════════════╝'
    echo -e "${RESET}"
    
    echo -e "${D_FIRE}🔥 Initializing Devil Transformation...${RESET}"
    sleep 1
}

function matrix_effect() {
    echo -e "${D_MATRIX}"
    for i in {1..10}; do
        echo "0101010101010101010101010101010101010101010101010101010101010101"
        sleep 0.05
    done
    echo -e "${RESET}"
}

function devil_progress() {
    local label=$1
    local duration=$2
    echo -ne "${D_GREEN}${label} [${RESET}"
    for i in {1..20}; do
        echo -ne "${D_RED}█${RESET}"
        sleep $(echo "scale=2; $duration/20" | bc)
    done
    echo -e "${D_GREEN}] ✓${RESET}"
}

# ============================================
# 🔧 SYSTEM CHECK & PREPARATION
# ============================================

function check_system() {
    echo -e "${D_CYAN}🔍 Detecting System...${RESET}"
    
    # Check Ubuntu
    if ! grep -q "Ubuntu" /etc/os-release; then
        echo -e "${D_RED}❌ This script is for Ubuntu only!${RESET}"
        exit 1
    fi
    
    # Check GNOME
    if [ "$XDG_CURRENT_DESKTOP" != "GNOME" ]; then
        echo -e "${D_YELLOW}⚠️  GNOME not detected. Some features may not work.${RESET}"
    fi
    
    # Check sudo
    if [ "$EUID" -ne 0 ]; then
        echo -e "${D_RED}❌ Please run with sudo!${RESET}"
        exit 1
    fi
    
    devil_progress "System Check" 1
}

function create_devil_dirs() {
    echo -e "${D_CYAN}📁 Creating Devil Directories...${RESET}"
    
    mkdir -p "$DEVIL_DIR"
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$DEVIL_DIR/themes"
    mkdir -p "$DEVIL_DIR/icons"
    mkdir -p "$DEVIL_DIR/wallpapers"
    mkdir -p "$DEVIL_DIR/fonts"
    mkdir -p "$DEVIL_DIR/sounds"
    mkdir -p "$DEVIL_DIR/plymouth"
    mkdir -p "$DEVIL_DIR/terminal"
    mkdir -p "$DEVIL_DIR/scripts"
    mkdir -p "$DEVIL_DIR/configs"
    
    devil_progress "Directory Creation" 1
}

# ============================================
# 🎨 DEVIL THEME INSTALLATION
# ============================================

function install_devil_theme() {
    echo -e "${D_CYAN}🎨 Installing Devil GTK Theme...${RESET}"
    
    # Backup current theme
    dconf dump /org/gnome/desktop/interface/ > "$BACKUP_DIR/gtk-backup.txt"
    
    # Download and install Devil theme
    THEME_URL="https://github.com/EliverLara/Sweet/archive/refs/heads/nova.zip"
    THEME_DIR="/usr/share/themes"
    
    echo -e "${D_YELLOW}Downloading Devil Theme...${RESET}"
    wget -q "$THEME_URL" -O /tmp/devil-theme.zip
    
    if [ $? -eq 0 ]; then
        unzip -q /tmp/devil-theme.zip -d /tmp/
        sudo cp -r /tmp/Sweet-nova/* "$THEME_DIR/"
        
        # Set Devil theme
        gsettings set org.gnome.desktop.interface gtk-theme "Sweet-Dark"
        gsettings set org.gnome.desktop.wm.preferences theme "Sweet-Dark"
        
        echo -e "${D_GREEN}✅ Devil Theme Installed${RESET}"
    else
        echo -e "${D_RED}❌ Failed to download theme. Using fallback...${RESET}"
        # Fallback to existing dark theme
        gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark"
    fi
    
    devil_progress "Theme Installation" 2
}

function install_devil_icons() {
    echo -e "${D_CYAN}📱 Installing Devil Icons...${RESET}"
    
    ICON_URL="https://github.com/vinceliuice/Tela-icon-theme/archive/refs/heads/master.zip"
    ICON_DIR="/usr/share/icons"
    
    wget -q "$ICON_URL" -O /tmp/devil-icons.zip
    unzip -q /tmp/devil-icons.zip -d /tmp/
    sudo cp -r /tmp/Tela-icon-theme-master/Tela-red-dark/ "$ICON_DIR/Tela-Devil/"
    
    # Set icons
    gsettings set org.gnome.desktop.interface icon-theme "Tela-Devil"
    
    devil_progress "Icon Installation" 2
}

# ============================================
# 🖼️ DEVIL WALLPAPER COLLECTION
# ============================================

function install_devil_wallpapers() {
    echo -e "${D_CYAN}🖼️ Installing Devil Wallpapers...${RESET}"
    
    # Create wallpapers directory
    WALLPAPER_DIR="$HOME/Pictures/Devil-Wallpapers"
    mkdir -p "$WALLPAPER_DIR"
    
    # Generate Devil wallpapers using ImageMagick
    echo -e "${D_YELLOW}Generating Devil Wallpapers...${RESET}"
    
    # Wallpaper 1: Matrix Rain
    convert -size 1920x1080 xc:black \
        -fill "#00FF00" -pointsize 20 -draw "text 100,100 'IRFAN320 DEVIL MODE'" \
        -fill "#008800" -pointsize 15 -draw "text 150,150 '01010101010101010101'" \
        -fill "#00AA00" -pointsize 12 -draw "text 200,200 '01010101010101010101'" \
        "$WALLPAPER_DIR/matrix.jpg"
    
    # Wallpaper 2: Fire & Blood
    convert -size 1920x1080 gradient:red-black \
        -fill black -draw "rectangle 0,500 1920,1080" \
        -fill white -pointsize 60 -font "Arial-Bold" -draw "text 300,400 '$IRFAN'" \
        -fill red -pointsize 30 -draw "text 350,480 'DEVIL UBUNTU v$VERSION'" \
        "$WALLPAPER_DIR/fire-blood.jpg"
    
    # Wallpaper 3: Cyber Devil
    convert -size 1920x1080 xc:'#0a0a0a' \
        -fill 'none' -stroke '#ff0000' -strokewidth 2 \
        -draw "polygon 100,100 500,100 300,500" \
        -draw "polygon 1500,200 1800,200 1650,600" \
        -fill '#00ff00' -pointsize 40 -font "Courier" \
        -draw "text 700,300 'ROOT@$DEVIL_NAME'" \
        -draw "text 720,350 '# whoami'" \
        -draw "text 750,400 '$IRFAN'" \
        "$WALLPAPER_DIR/cyber-devil.jpg"
    
    # Set random wallpaper
    WALLPAPERS=("$WALLPAPER_DIR"/*.jpg)
    RANDOM_WALLPAPER="${WALLPAPERS[RANDOM % ${#WALLPAPERS[@]}]}"
    
    gsettings set org.gnome.desktop.background picture-uri "file://$RANDOM_WALLPAPER"
    gsettings set org.gnome.desktop.screensaver picture-uri "file://$RANDOM_WALLPAPER"
    
    # Create wallpaper switcher script
    cat > "$DEVIL_DIR/scripts/wallpaper-switcher.sh" << EOF
#!/bin/bash
WALLPAPERS=($WALLPAPER_DIR/*.jpg)
while true; do
    for wp in "\${WALLPAPERS[@]}"; do
        gsettings set org.gnome.desktop.background picture-uri "file://\$wp"
        sleep 300  # Change every 5 minutes
    done
done
EOF
    
    chmod +x "$DEVIL_DIR/scripts/wallpaper-switcher.sh"
    
    devil_progress "Wallpaper Setup" 2
}

# ============================================
# 💻 DEVIL TERMINAL CUSTOMIZATION
# ============================================

function setup_devil_terminal() {
    echo -e "${D_CYAN}💻 Configuring Devil Terminal...${RESET}"
    
    # Backup original bashrc
    cp ~/.bashrc "$BACKUP_DIR/bashrc.backup"
    
    # Create Devil bashrc
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
BLACK='\[\033[38;5;232m\]'
RESET='\[\033[0m\]'

# Devil Prompt
PS1="${RED}┌─[${GREEN}\u${RED}@${BLUE}DEVIL-UBUNTU${RED}]─[${YELLOW}\w${RED}]\n${RED}└──╼${RESET} "
# Short prompt alternative: PS1="${RED}😈 ${GREEN}\u${RED}@${BLUE}DEVIL ${YELLOW}\W${RED} ➜${RESET} "

# Devil Aliases
alias devil-mode='echo "😈 DEVIL MODE ACTIVATED!"'
alias matrix='cmatrix -b -C green'
alias hack='echo "Hacking the mainframe..." && sleep 2 && echo "Just kidding, $USER!"'
alias update-devil='sudo apt update && sudo apt upgrade -y'
alias clean-devil='sudo apt autoremove -y && sudo apt autoclean'
alias sys-info='neofetch --ascii_distro devil'

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
    for i in {1..100}; do
        echo -n $(tr -dc '01' </dev/urandom | head -c 100)
        echo
        sleep 0.05
    done
    echo -e "\033[0m"
}

# Devil Welcome Message
echo -e "${RED}"
echo '╔═══════════════════════════════════════════════════════╗'
echo '║                                                       ║'
echo -e "║      😈 WELCOME TO ${GREEN}IRFAN320${RED}'S ${BLUE}DEVIL UBUNTU${RED} 😈     ║"
echo '║                                                       ║'
echo -e "║     Type ${YELLOW}devil-mode${RED} to unleash the beast!        ║"
echo '║                                                       ║'
echo '╚═══════════════════════════════════════════════════════╝'
echo -e "${RESET}"

# Default bashrc
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
EOF
    
    # Configure GNOME Terminal profile
    TERMINAL_PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default | tr -d "'")
    
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$TERMINAL_PROFILE/ \
        background-color 'rgb(0,0,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$TERMINAL_PROFILE/ \
        foreground-color 'rgb(0,255,0)'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$TERMINAL_PROFILE/ \
        font 'Monospace 11'
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$TERMINAL_PROFILE/ \
        use-system-font false
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$TERMINAL_PROFILE/ \
        use-theme-colors false
    
    devil_progress "Terminal Setup" 2
}

# ============================================
# 🔄 SYSTEM TWEAKS & OPTIMIZATIONS
# ============================================

function apply_devil_tweaks() {
    echo -e "${D_CYAN}⚙️ Applying Devil System Tweaks...${RESET}"
    
    # Power settings for performance
    gsettings set org.gnome.settings-daemon.plugins.power power-button-action 'suspend'
    gsettings set org.gnome.desktop.session idle-delay 0  # Never idle
    
    # Privacy settings
    gsettings set org.gnome.desktop.privacy remember-recent-files false
    gsettings set org.gnome.desktop.privacy remove-old-temp-files true
    gsettings set org.gnome.desktop.privacy old-files-age 1
    
    # Interface tweaks
    gsettings set org.gnome.desktop.interface clock-show-date true
    gsettings set org.gnome.desktop.interface clock-show-seconds true
    gsettings set org.gnome.desktop.interface enable-hot-corners false
    
    # Window behavior
    gsettings set org.gnome.desktop.wm.preferences action-double-click-titlebar 'toggle-maximize'
    gsettings set org.gnome.desktop.wm.preferences button-layout 'appmenu:minimize,maximize,close'
    
    # Nautilus (Files) tweaks
    gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'
    gsettings set org.gnome.nautilus.preferences show-hidden-files true
    
    # Mouse and touchpad
    gsettings set org.gnome.desktop.peripherals.mouse speed -0.5
    gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true
    
    devil_progress "System Tweaks" 1
}

# ============================================
# 🎵 DEVIL SOUND THEME
# ============================================

function setup_devil_sounds() {
    echo -e "${D_CYAN}🎵 Configuring Devil Sounds...${RESET}"
    
    # Disable system sounds (evil is silent)
    gsettings set org.gnome.desktop.sound event-sounds false
    
    # Create custom login sound script
    cat > "$DEVIL_DIR/scripts/login-sound.sh" << 'EOF'
#!/bin/bash
# Play evil laugh on login
echo -e "\a"  # System beep
sleep 0.5
echo -e "\a"
echo "😈 Welcome back, $USER!"
EOF
    
    chmod +x "$DEVIL_DIR/scripts/login-sound.sh"
    
    # Add to bashrc
    echo -e '\n# Devil login sound\nif [ -f ~/.devil-ubuntu/scripts/login-sound.sh ]; then\n    . ~/.devil-ubuntu/scripts/login-sound.sh\nfi' >> ~/.bashrc
    
    devil_progress "Sound Setup" 1
}

# ============================================
# 🔐 SECURITY & MONITORING
# ============================================

function setup_devil_security() {
    echo -e "${D_CYAN}🔐 Setting up Devil Security...${RESET}"
    
    # Create security monitor script
    cat > "$DEVIL_DIR/scripts/security-monitor.sh" << 'EOF'
#!/bin/bash
# Devil Security Monitor
LOGFILE="$HOME/.irfan320-devil/security.log"

echo "================================" >> "$LOGFILE"
echo "DEVIL SECURITY SCAN - $(date)" >> "$LOGFILE"
echo "================================" >> "$LOGFILE"

# Check suspicious processes
echo "Checking processes..." >> "$LOGFILE"
ps aux | grep -E "(backdoor|malware|keylogger)" >> "$LOGFILE" 2>/dev/null || true

# Check network connections
echo -e "\nNetwork connections:" >> "$LOGFILE"
netstat -tunap | grep -v "127.0.0.1" >> "$LOGFILE"

# Check login attempts
echo -e "\nRecent logins:" >> "$LOGFILE"
last -n 10 >> "$LOGFILE"

echo -e "\nScan complete.\n" >> "$LOGFILE"
EOF
    
    chmod +x "$DEVIL_DIR/scripts/security-monitor.sh"
    
    # Create crontab entry for regular scanning
    (crontab -l 2>/dev/null; echo "0 */6 * * * $DEVIL_DIR/scripts/security-monitor.sh") | crontab -
    
    devil_progress "Security Setup" 1
}

# ============================================
# 📊 SYSTEM MONITOR WIDGET
# ============================================

function setup_devil_monitor() {
    echo -e "${D_CYAN}📊 Setting up Devil System Monitor...${RESET}"
    
    # Create system monitor script
    cat > "$DEVIL_DIR/scripts/system-monitor.sh" << 'EOF'
#!/bin/bash
# Devil System Monitor
while true; do
    clear
    echo -e "\033[38;5;196m╔══════════════════════════════════════════════╗"
    echo -e "║           😈 IRFAN320 DEVIL MONITOR          ║"
    echo -e "╚══════════════════════════════════════════════╗\033[0m"
    echo -e "\033[38;5;46m"
    echo "System:    $(uname -srm)"
    echo "Uptime:    $(uptime -p)"
    echo "CPU Temp:  $(sensors | grep 'Core 0' | awk '{print $3}')"
    echo "Memory:    $(free -h | awk '/^Mem:/ {print $3 "/" $2}')"
    echo "Disk:      $(df -h / | awk 'NR==2 {print $3 "/" $2}')"
    echo "IP Addr:   $(hostname -I | awk '{print $1}')"
    echo "Processes: $(ps aux | wc -l) running"
    echo -e "\033[0m"
    sleep 2
done
EOF
    
    chmod +x "$DEVIL_DIR/scripts/system-monitor.sh"
    
    # Create desktop shortcut
    cat > ~/Desktop/Devil-Monitor.desktop << EOF
[Desktop Entry]
Name=Devil System Monitor
Comment=Real-time system monitoring
Exec=gnome-terminal -- bash -c "$DEVIL_DIR/scripts/system-monitor.sh; exec bash"
Icon=utilities-system-monitor
Terminal=true
Type=Application
Categories=System;Monitor;
EOF
    
    chmod +x ~/Desktop/Devil-Monitor.desktop
    
    devil_progress "Monitor Setup" 1
}

# ============================================
# 🎮 GAMING OPTIMIZATIONS
# ============================================

function setup_gaming_mode() {
    echo -e "${D_CYAN}🎮 Setting up Devil Gaming Mode...${RESET}"
    
    # Create gaming performance script
    cat > "$DEVIL_DIR/scripts/gaming-mode.sh" << 'EOF'
#!/bin/bash
# Devil Gaming Mode
echo "😈 ACTIVATING GAMING MODE..."

# CPU Governor to performance
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Disable compositor for fullscreen performance
killall compton || true
killall picom || true

# Increase inotify watchers for gaming
echo 524288 | sudo tee /proc/sys/fs/inotify/max_user_watches
echo 512 | sudo tee /proc/sys/fs/inotify/max_user_instances

# Network optimization
sudo sysctl -w net.core.rmem_max=134217728
sudo sysctl -w net.core.wmem_max=134217728

echo "✅ Gaming Mode Activated!"
echo "Type 'devil-normal' to return to normal mode"
EOF
    
    cat > "$DEVIL_DIR/scripts/normal-mode.sh" << 'EOF'
#!/bin/bash
# Return to normal mode
echo "😇 Returning to normal mode..."

# CPU Governor back to ondemand
echo ondemand | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Restart compositor
picom --experimental-backends -b 2>/dev/null || compton -b 2>/dev/null || true

echo "✅ Normal Mode Restored!"
EOF
    
    chmod +x "$DEVIL_DIR/scripts/gaming-mode.sh"
    chmod +x "$DEVIL_DIR/scripts/normal-mode.sh"
    
    # Add aliases
    echo "alias gaming-mode='sudo $DEVIL_DIR/scripts/gaming-mode.sh'" >> ~/.bashrc
    echo "alias devil-normal='sudo $DEVIL_DIR/scripts/normal-mode.sh'" >> ~/.bashrc
    
    devil_progress "Gaming Setup" 1
}

# ============================================
# 🚀 FINAL SETUP & COMPLETION
# ============================================

function finalize_setup() {
    echo -e "${D_CYAN}🚀 Finalizing Devil Setup...${RESET}"
    
    # Update alternatives
    sudo update-alternatives --set x-terminal-emulator /usr/bin/gnome-terminal.wrapper
    
    # Refresh font cache
    sudo fc-cache -fv
    
    # Create uninstall script
    cat > "$DEVIL_DIR/uninstall-devil.sh" << EOF
#!/bin/bash
echo "😇 Uninstalling Devil Ubuntu..."
echo "Restoring backups from: $BACKUP_DIR"

# Restore bashrc
if [ -f "$BACKUP_DIR/bashrc.backup" ]; then
    cp "$BACKUP_DIR/bashrc.backup" ~/.bashrc
fi

# Restore GTK settings
if [ -f "$BACKUP_DIR/gtk-backup.txt" ]; then
    dconf load /org/gnome/desktop/interface/ < "$BACKUP_DIR/gtk-backup.txt"
fi

# Remove crontab entries
crontab -l | grep -v "security-monitor.sh" | crontab -

echo "✅ Devil theme removed. Reboot to complete."
EOF
    
    chmod +x "$DEVIL_DIR/uninstall-devil.sh"
    
    # Create devil info file
    cat > "$DEVIL_DIR/DEVIL-INFO.txt" << EOF
================================
IRFAN320 DEVIL UBUNTU v${VERSION}
================================
Installation Date: $(date)
Installation Directory: $DEVIL_DIR
Backup Directory: $BACKUP_DIR

Features Installed:
1. Devil GTK Theme
2. Custom Icons
3. Matrix Wallpapers
4. Devil Terminal
5. System Tweaks
6. Security Monitor
7. Gaming Mode

Commands Available:
- devil-mode      : Show welcome message
- gaming-mode     : Activate gaming optimizations
- devil-normal    : Return to normal mode
- matrix-rain     : Show matrix effect
- sys-info        : System information

To uninstall: Run $DEVIL_DIR/uninstall-devil.sh

Contact: $EMAIL
Website: https://github.com/irfan320/devil-ubuntu

😈 LONG LIVE THE DEVIL MODE! 😈
EOF
    
    devil_progress "Finalization" 2
}

function show_completion() {
    clear
    echo -e "${D_RED}"
    echo '╔═══════════════════════════════════════════════════════════════╗'
    echo '║                                                               ║'
    echo -e "║           ${D_GREEN}😈 TRANSFORMATION COMPLETE! 😈${D_RED}                ║"
    echo '║                                                               ║'
    echo -e "║   ${D_YELLOW}Your Ubuntu has been upgraded to DEVIL MODE${D_RED}         ║"
    echo '║                                                               ║'
    echo -e "║   ${D_CYAN}Reboot your system to see all changes${D_RED}                 ║"
    echo '║                                                               ║'
    echo '╠═══════════════════════════════════════════════════════════════╣'
    echo '║                                                               ║'
    echo -e "║   ${D_PURPLE}Available Commands:${D_RED}                                  ║"
    echo -e "║   ${D_GREEN}• devil-mode${D_RED}     - Show welcome message              ║"
    echo -e "║   ${D_GREEN}• gaming-mode${D_RED}    - Activate gaming optimizations     ║"
    echo -e "║   ${D_GREEN}• matrix-rain${D_RED}    - Show matrix effect                ║"
    echo -e "║   ${D_GREEN}• sys-info${D_RED}       - Display system information        ║"
    echo '║                                                               ║'
    echo -e "║   ${D_YELLOW}Uninstall: ${D_GREEN}$DEVIL_DIR/uninstall-devil.sh${D_RED}            ║"
    echo '║                                                               ║'
    echo -e "║   ${D_CYAN}Created with ❤️ by ${BOLD}IRFAN320${RESET}${D_RED}                      ║"
    echo '║                                                               ║'
    echo '╚═══════════════════════════════════════════════════════════════╝'
    echo -e "${RESET}"
    
    echo -e "\n${D_FIRE}🔥 Press Enter to reboot, or Ctrl+C to cancel...${RESET}"
    read -r
    sudo reboot
}

# ============================================
# 🎪 MAIN EXECUTION
# ============================================

function main() {
    show_devil_banner
    matrix_effect
    
    echo -e "${D_GREEN}Starting Devil Transformation...${RESET}"
    echo -e "${D_YELLOW}This will take approximately 2-3 minutes.${RESET}"
    echo -e "${D_RED}DO NOT INTERRUPT THE PROCESS!${RESET}\n"
    
    # Execute all setup functions
    check_system
    create_devil_dirs
    install_devil_theme
    install_devil_icons
    install_devil_wallpapers
    setup_devil_terminal
    apply_devil_tweaks
    setup_devil_sounds
    setup_devil_security
    setup_devil_monitor
    setup_gaming_mode
    finalize_setup
    
    show_completion
}

# ============================================
# 🚀 START TRANSFORMATION
# ============================================

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
