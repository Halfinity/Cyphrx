// CYPHRX - Cyber Ops Terminal
document.addEventListener('DOMContentLoaded', () => {
    console.log('%cCYPHRX v4.5 initialized', 'color:#00ff88; font-family:monospace');

    // Boot sequence
    const boot = document.getElementById('boot');
    const app = document.getElementById('app');

    setTimeout(() => {
        boot.classList.add('gone');
        setTimeout(() => {
            app.style.display = 'grid';
            initApp();
        }, 600);
    }, 1800);

    // Click to skip boot
    boot.addEventListener('click', () => {
        boot.classList.add('gone');
        setTimeout(() => app.style.display = 'grid', 400);
    });

    function initApp() {
        // Progress tracking
        let done = 0;
        const total = 42; // example
        document.getElementById('total').textContent = total;

        // Command cards example data (you can expand)
        const commands = [
            { id: 1, title: "Recon - Nmap Scan", code: "nmap -sV -sC -T4 <TARGET>" },
            // ... more can be added
        ];

        // Variable system
        window.vars = {
            LHOST: "10.10.13.37",
            LPORT: "4444",
            TARGET: "192.168.1.100"
        };

        // Live variable substitution (demo)
        console.log("Variables loaded:", window.vars);

        // Palette (Cmd/Ctrl + K)
        const palBg = document.getElementById('pal-bg');
        document.addEventListener('keydown', e => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                palBg.classList.add('open');
                document.getElementById('pal-input').focus();
            }
            if (e.key === 'Escape' && palBg.classList.contains('open')) {
                palBg.classList.remove('open');
            }
        });

        // Toast helper
        window.showToast = (msg = "COPIED TO CLIPBOARD") => {
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2200);
        };

        // Make copy buttons work (example)
        document.querySelectorAll('.act-btn').forEach(btn => {
            if (btn.textContent.includes('COPY')) {
                btn.addEventListener('click', () => {
                    window.showToast();
                });
            }
        });

        console.log('%cCYPHRX Terminal fully operational', 'color:#00ff88');
    }
});