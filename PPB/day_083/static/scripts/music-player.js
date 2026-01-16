// static/scripts/music-player.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('Music player script loaded');

    // Elements
    const musicToggle = document.getElementById('music-toggle');
    const volumeSlider = document.getElementById('volume-slider');
    const backgroundMusic = document.getElementById('background-music');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const shuffleBtn = document.getElementById('shuffle-btn');
    const songTitle = document.querySelector('.song-title');
    const volumeLevel = document.querySelector('.volume-level');

    // Check if elements exist
    if (!musicToggle || !volumeSlider || !backgroundMusic) {
        console.error('Music player elements not found');
        return;
    }

    const musicIcon = musicToggle.querySelector('i');

    // Playlist configuration
    const playlist = [
        { title: "Track 1", file: "1.mp3" },
        { title: "Track 2", file: "2.mp3" },
        { title: "Track 3", file: "3.mp3" }
    ];

    // State variables
    let currentTrackIndex = 0;
    let shuffledPlaylist = [];
    let isShuffled = localStorage.getItem('musicShuffled') === 'true';
    let isPlaying = localStorage.getItem('musicPlaying') === 'true';
    let savedVolume = localStorage.getItem('musicVolume') || 30;

    // Initialize player
    function initPlayer() {
        console.log('Initializing music player');

        // Set initial volume
        backgroundMusic.volume = savedVolume / 100;
        volumeSlider.value = savedVolume;

        // Update volume display
        if (volumeLevel) {
            volumeLevel.textContent = `${savedVolume}%`;
            volumeSlider.style.setProperty('--volume-width', `${savedVolume}%`);
        }

        // Initialize playlist
        shufflePlaylist();

        // Load first track
        loadTrack(currentTrackIndex);

        // Set initial state
        if (isPlaying) {
            setTimeout(() => {
                backgroundMusic.play().then(() => {
                    console.log('Music autoplay successful');
                    musicToggle.classList.add('playing');
                    updateVolumeIcon(savedVolume); // Update with correct color
                    updateNowPlaying();
                }).catch(e => {
                    console.log('Autoplay prevented:', e.message);
                    musicToggle.classList.remove('playing');
                    updateVolumeIcon(savedVolume); // Update with paused color
                    updateNowPlaying();
                });
            }, 1000);
        } else {
            musicToggle.classList.remove('playing');
            updateVolumeIcon(savedVolume); // Update with paused color
            updateNowPlaying();
        }

        // Update shuffle button state
        if (shuffleBtn) {
            if (isShuffled) {
                shuffleBtn.classList.add('active');
            } else {
                shuffleBtn.classList.remove('active');
            }
        }
    }

    // Shuffle playlist function
    function shufflePlaylist() {
        if (isShuffled) {
            // Create shuffled playlist
            shuffledPlaylist = [...playlist];
            for (let i = shuffledPlaylist.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [shuffledPlaylist[i], shuffledPlaylist[j]] = [shuffledPlaylist[j], shuffledPlaylist[i]];
            }
            console.log('Playlist shuffled:', shuffledPlaylist);
        } else {
            // Use original order
            shuffledPlaylist = [...playlist];
            console.log('Playlist in original order');
        }
    }

    // Load a track
    function loadTrack(index) {
        if (index < 0 || index >= shuffledPlaylist.length) {
            console.error('Invalid track index:', index);
            return;
        }

        currentTrackIndex = index;
        const track = shuffledPlaylist[currentTrackIndex];

        // Update audio source
        backgroundMusic.src = `/static/music/${track.file}`;

        // Update UI
        updateNowPlaying();

        console.log(`Loading track: ${track.title} (${track.file})`);

        // Save current track to localStorage
        localStorage.setItem('currentTrack', currentTrackIndex);

        // Load the track
        backgroundMusic.load();

        // If we were playing, continue playing
        if (isPlaying) {
            setTimeout(() => {
                backgroundMusic.play().catch(e => {
                    console.log('Could not autoplay next track:', e.message);
                });
            }, 100);
        }
    }

    // Play next track
    function playNext() {
        let nextIndex = currentTrackIndex + 1;
        if (nextIndex >= shuffledPlaylist.length) {
            nextIndex = 0; // Loop back to beginning
        }
        loadTrack(nextIndex);

        // Add animation feedback
        if (songTitle) {
            songTitle.style.animation = 'slideInRight 0.3s ease';
            setTimeout(() => {
                songTitle.style.animation = '';
            }, 300);
        }
    }

    // Play previous track
    function playPrev() {
        let prevIndex = currentTrackIndex - 1;
        if (prevIndex < 0) {
            prevIndex = shuffledPlaylist.length - 1; // Loop to end
        }
        loadTrack(prevIndex);
    }

    // Update now playing display
    function updateNowPlaying() {
        if (songTitle && shuffledPlaylist[currentTrackIndex]) {
            songTitle.textContent = shuffledPlaylist[currentTrackIndex].title;

            // Add pulsing animation if playing
            if (!backgroundMusic.paused) {
                songTitle.style.animation = 'pulse 2s infinite';
            } else {
                songTitle.style.animation = '';
            }
        }
    }

    // Update volume icon
    function updateVolumeIcon(volume) {
        if (!musicIcon) return;

        const isPaused = backgroundMusic.paused;
        const iconColor = isPaused ? 'var(--light-gray70)' : 'var(--orange-yellow-crayola)';

        if (volume == 0) {
            musicIcon.className = 'fas fa-volume-mute';
        } else if (volume < 20) {
            musicIcon.className = 'fas fa-volume-off';
        } else if (volume < 50) {
            musicIcon.className = 'fas fa-volume-low';
        } else {
            musicIcon.className = 'fas fa-volume-high';
        }

        // Always set color based on play state
        musicIcon.style.color = iconColor;
    }

    // Toggle play/pause
    musicToggle.addEventListener('click', function() {
        if (backgroundMusic.paused) {
            backgroundMusic.play().then(() => {
                console.log('Music started playing');
                musicToggle.classList.add('playing');
                localStorage.setItem('musicPlaying', 'true');
                isPlaying = true;
                updateVolumeIcon(volumeSlider.value); // Update icon color
                updateNowPlaying();
            }).catch(e => {
                console.log('Could not play music:', e.message);
                // Still update icon to show paused state
                updateVolumeIcon(volumeSlider.value);
            });
        } else {
            backgroundMusic.pause();
            console.log('Music paused');
            musicToggle.classList.remove('playing');
            localStorage.setItem('musicPlaying', 'false');
            isPlaying = false;
            updateVolumeIcon(volumeSlider.value); // Update icon color
            updateNowPlaying();
        }
    });

    // Volume control
    volumeSlider.addEventListener('input', function() {
        const volume = this.value;
        backgroundMusic.volume = volume / 100;
        localStorage.setItem('musicVolume', volume);

        // Update volume width
        volumeSlider.style.setProperty('--volume-width', `${volume}%`);

        // Update volume level display
        if (volumeLevel) {
            volumeLevel.textContent = `${volume}%`;
        }

        // Update icon
        updateVolumeIcon(volume);
    });

    // Next button
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            playNext();
            // Add button feedback
            this.style.animation = 'pulse 0.3s ease';
            setTimeout(() => {
                this.style.animation = '';
            }, 300);
        });
    }

    // Previous button
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            playPrev();
            // Add button feedback
            this.style.animation = 'pulse 0.3s ease';
            setTimeout(() => {
                this.style.animation = '';
            }, 300);
        });
    }

    // Shuffle button
    if (shuffleBtn) {
        shuffleBtn.addEventListener('click', function() {
            isShuffled = !isShuffled;
            localStorage.setItem('musicShuffled', isShuffled);

            if (isShuffled) {
                this.classList.add('active');
                showMusicNotification('Shuffle: ON');
            } else {
                this.classList.remove('active');
                showMusicNotification('Shuffle: OFF');
            }

            // Re-shuffle playlist
            shufflePlaylist();

            // If playing, continue with new order from current position
            if (!backgroundMusic.paused) {
                // Find current track in new shuffled order
                const currentTrackFile = playlist[currentTrackIndex].file;
                const newIndex = shuffledPlaylist.findIndex(track => track.file === currentTrackFile);
                if (newIndex !== -1) {
                    currentTrackIndex = newIndex;
                }
                updateNowPlaying();
            }
        });
    }

    // Handle track ending
    backgroundMusic.addEventListener('ended', function() {
        console.log('Track ended, playing next');
        playNext();
    });

    // Handle audio errors
    backgroundMusic.addEventListener('error', function(e) {
        console.error('Audio error:', e);
        console.error('Audio error details:', backgroundMusic.error);
        showMusicNotification('Error loading track, skipping...');
        setTimeout(playNext, 1000);
    });

    // Handle audio loading
    backgroundMusic.addEventListener('loadeddata', function() {
        console.log('Audio loaded successfully:', backgroundMusic.src);
    });

    // Handle play event
    backgroundMusic.addEventListener('play', function() {
        console.log('Track started playing');
        updateNowPlaying();
        updateVolumeIcon(volumeSlider.value); // Update icon when play starts
    });

    // Handle pause event
    backgroundMusic.addEventListener('pause', function() {
        console.log('Track paused');
        updateNowPlaying();
        updateVolumeIcon(volumeSlider.value); // Update icon when paused
    });

    // Handle page visibility change
    document.addEventListener('visibilitychange', function() {
        if (document.hidden && !backgroundMusic.paused) {
            localStorage.setItem('musicPlaying', 'true');
        }
    });

    // Auto-pause when navigating away
    window.addEventListener('beforeunload', function() {
        if (!backgroundMusic.paused) {
            localStorage.setItem('musicPlaying', 'true');
        }
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Space bar to play/pause
        if (e.code === 'Space' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
            e.preventDefault();
            musicToggle.click();
        }
        // Right arrow for next track
        else if (e.code === 'ArrowRight' && (e.ctrlKey || e.metaKey)) {
            e.preventDefault();
            if (nextBtn) nextBtn.click();
        }
        // Left arrow for previous track
        else if (e.code === 'ArrowLeft' && (e.ctrlKey || e.metaKey)) {
            e.preventDefault();
            if (prevBtn) prevBtn.click();
        }
    });

    // Initialize the player
    initPlayer();

    // Function to show notification
    function showMusicNotification(message) {
        // Remove existing notification if any
        const existingNotification = document.querySelector('.music-notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        const notification = document.createElement('div');
        notification.className = 'music-notification';
        notification.innerHTML = `<p>${message}</p>`;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 2000);
    }

    // Add mobile music controls to navbar if needed
    function addMobileMusicControls() {
        const navbar = document.querySelector('.navbar-list');
        if (window.innerWidth <= 580 && navbar && !document.getElementById('mobile-music-toggle')) {
            const musicControls = document.createElement('li');
            musicControls.className = 'navbar-music-controls';
            musicControls.innerHTML = `
                <button class="navbar-music-btn" id="mobile-music-toggle" title="Toggle Music">
                    <i class="fas fa-volume-up"></i>
                </button>
            `;
            navbar.appendChild(musicControls);

            const mobileToggle = document.getElementById('mobile-music-toggle');
            const mobileIcon = mobileToggle.querySelector('i');

            function updateMobileButton() {
                 const isPaused = backgroundMusic.paused;
                if (!isPaused) {
                    mobileToggle.style.background = 'var(--orange-yellow-crayola)';
                    mobileToggle.style.color = 'var(--smoky-black)';
                    mobileIcon.className = 'fas fa-volume-up';
                } else {
                    mobileToggle.style.background = 'var(--jet)';
                    mobileIcon.style.color = 'var(--light-gray70)'; // Grey when paused
                    mobileIcon.className = 'fas fa-volume-mute';
                }
            }

            updateMobileButton();

            mobileToggle.addEventListener('click', function() {
                musicToggle.click();
                updateMobileButton();
            });

            musicToggle.addEventListener('click', updateMobileButton);
        }
    }

    addMobileMusicControls();

    // Add CSS animations for notification if not already present
    if (!document.querySelector('#music-notification-styles')) {
        const style = document.createElement('style');
        style.id = 'music-notification-styles';
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes slideOut {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
});