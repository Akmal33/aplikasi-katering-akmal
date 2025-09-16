// app.js - JavaScript untuk PWA Keuangan Katering

// Variabel global
let deferredPrompt;

// Event listener untuk saat DOM siap
document.addEventListener('DOMContentLoaded', function() {
    // Set tanggal hari ini sebagai default
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('incomeDate').value = today;
    document.getElementById('expenseDate').value = today;
    
    // Event listener untuk form pemasukan
    document.getElementById('incomeForm').addEventListener('submit', handleIncomeSubmit);
    
    // Event listener untuk form pengeluaran
    document.getElementById('expenseForm').addEventListener('submit', handleExpenseSubmit);
    
    // Event listener untuk tombol tutup modal
    document.querySelectorAll('.close').forEach(button => {
        button.addEventListener('click', closeModal);
    });
    
    // Event listener untuk klik di luar modal
    window.addEventListener('click', function(event) {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (event.target === modal) {
                closeModal.call(modal.querySelector('.close'));
            }
        });
    });
    
    // Event listener untuk install prompt
    window.addEventListener('beforeinstallprompt', (e) => {
        // Mencegah browser menampilkan prompt install secara otomatis
        e.preventDefault();
        // Simpan event agar bisa digunakan nanti
        deferredPrompt = e;
        // Tampilkan prompt install custom
        showInstallPrompt();
    });
    
    // Registrasi service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch(error => {
                console.log('Service Worker registration failed:', error);
            });
    }
});

// Handler untuk submit form pemasukan
function handleIncomeSubmit(e) {
    e.preventDefault();
    
    const date = document.getElementById('incomeDate').value;
    const description = document.getElementById('incomeDescription').value;
    const amount = document.getElementById('incomeAmount').value;
    
    if (!date || !description || !amount) {
        showToast('Harap isi semua field', 'error');
        return;
    }
    
    if (amount <= 0) {
        showToast('Jumlah harus lebih besar dari 0', 'error');
        return;
    }
    
    // Tampilkan spinner loading
    showLoading(true);
    
    // Kirim data ke server
    fetch('/add_income', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            date: date,
            description: description,
            amount: parseFloat(amount)
        })
    })
    .then(response => response.json())
    .then(data => {
        showLoading(false);
        if (data.status === 'success') {
            showToast(data.message, 'success');
            // Reset form
            document.getElementById('incomeForm').reset();
            document.getElementById('incomeDate').value = new Date().toISOString().split('T')[0];
            // Refresh data
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            showToast(data.message || 'Terjadi kesalahan', 'error');
        }
    })
    .catch(error => {
        showLoading(false);
        showToast('Terjadi kesalahan: ' + error.message, 'error');
    });
}

// Handler untuk submit form pengeluaran
function handleExpenseSubmit(e) {
    e.preventDefault();
    
    const date = document.getElementById('expenseDate').value;
    const description = document.getElementById('expenseDescription').value;
    const amount = document.getElementById('expenseAmount').value;
    
    if (!date || !description || !amount) {
        showToast('Harap isi semua field', 'error');
        return;
    }
    
    if (amount <= 0) {
        showToast('Jumlah harus lebih besar dari 0', 'error');
        return;
    }
    
    // Tampilkan spinner loading
    showLoading(true);
    
    // Kirim data ke server
    fetch('/add_expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            date: date,
            description: description,
            amount: parseFloat(amount)
        })
    })
    .then(response => response.json())
    .then(data => {
        showLoading(false);
        if (data.status === 'success') {
            showToast(data.message, 'success');
            // Reset form
            document.getElementById('expenseForm').reset();
            document.getElementById('expenseDate').value = new Date().toISOString().split('T')[0];
            // Refresh data
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            showToast(data.message || 'Terjadi kesalahan', 'error');
        }
    })
    .catch(error => {
        showLoading(false);
        showToast('Terjadi kesalahan: ' + error.message, 'error');
    });
}

// Fungsi untuk menampilkan toast notification
function showToast(message, type) {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    // Tampilkan toast
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    // Sembunyikan toast setelah 3 detik
    setTimeout(() => {
        toast.classList.remove('show');
        // Hapus toast dari DOM setelah animasi selesai
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 3000);
}

// Fungsi untuk menampilkan atau menyembunyikan loading spinner
function showLoading(show) {
    const spinner = document.querySelector('.spinner');
    if (spinner) {
        if (show) {
            spinner.classList.add('show');
        } else {
            spinner.classList.remove('show');
        }
    }
}

// Fungsi untuk menampilkan modal
function showModal(title, content) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalBody').innerHTML = content;
    document.getElementById('messageModal').classList.add('show');
}

// Fungsi untuk menyembunyikan modal
function closeModal() {
    document.getElementById('messageModal').classList.remove('show');
}

// Fungsi untuk menampilkan prompt install PWA
function showInstallPrompt() {
    const prompt = document.getElementById('pwaInstallPrompt');
    if (prompt) {
        prompt.classList.add('show');
    }
}

// Fungsi untuk menginstall PWA
function installPWA() {
    if (deferredPrompt) {
        // Tampilkan prompt install browser
        deferredPrompt.prompt();
        // Tunggu user merespon prompt
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the install prompt');
            } else {
                console.log('User dismissed the install prompt');
            }
            deferredPrompt = null;
            // Sembunyikan prompt custom
            document.getElementById('pwaInstallPrompt').classList.remove('show');
        });
    }
}

// Fungsi untuk menutup prompt install
function closeInstallPrompt() {
    document.getElementById('pwaInstallPrompt').classList.remove('show');
}

// Fungsi untuk format angka ke format Rupiah
function formatRupiah(number) {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0
    }).format(number);
}