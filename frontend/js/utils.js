// Custom Notification System for KisanAI
function showNotification(message, type = 'success') {
    // Remove existing notifications
    const existing = document.querySelector('.kisan-notification');
    if (existing) {
        existing.remove();
    }

    // Create notification element
    const notification = document.createElement('div');
    notification.className = `kisan-notification ${type}`;
    
    // Icon based on type
    let icon = 'fa-check-circle';
    if (type === 'error') icon = 'fa-exclamation-circle';
    if (type === 'info') icon = 'fa-info-circle';

    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${icon}"></i>
            <div class="notification-text">
                <strong>KisanAI Says</strong>
                <p>${message}</p>
            </div>
        </div>
    `;

    document.body.appendChild(notification);

    // Animate in
    requestAnimationFrame(() => {
        notification.classList.add('show');
    });

    // Remove after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 4000);
}

// Profile Picture Handling
function handleProfilePicUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            // Update all profile images on the page
            const profileImgs = document.querySelectorAll('.profile-img');
            profileImgs.forEach(img => img.src = e.target.result);
            
            // Save to localStorage for persistence across pages (demo purpose)
            localStorage.setItem('profile_pic_data', e.target.result);
            
            showNotification('Profile picture updated successfully!');
        };
        reader.readAsDataURL(file);
    }
}

// Load saved profile pic on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedPic = localStorage.getItem('profile_pic_data');
    if (savedPic) {
        const profileImgs = document.querySelectorAll('.profile-img');
        profileImgs.forEach(img => img.src = savedPic);
    }
});

// Sidebar Toggle for Mobile
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    if (sidebar && overlay) {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }
}
