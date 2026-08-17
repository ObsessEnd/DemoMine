/**
 * Terramity Awakened Wiki - Procedural Web Audio Sound Engine (100% Offline)
 * Features:
 * - Minecraft UI Click & Pop sounds
 * - Boss Defeat & Level-Up Victorious Chime
 * - Modal Open Mystical Swoosh
 * - Ambient Dark Fantasy Drone & Chords Generator
 */

const AudioEngine = {
  ctx: null,
  isMuted: localStorage.getItem('wiki_audio_muted') === 'true',
  isAmbientPlaying: false,
  ambientNodes: [],
  masterGain: null,

  init() {
    // Audio Context is initialized on first user gesture to comply with browser autoplay policies
    const enableAudio = () => {
      if (!this.ctx) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (AudioCtx) {
          this.ctx = new AudioCtx();
          this.masterGain = this.ctx.createGain();
          this.masterGain.gain.value = this.isMuted ? 0 : 0.35;
          this.masterGain.connect(this.ctx.destination);
        }
      }
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume();
      }
      document.removeEventListener('click', enableAudio);
      document.removeEventListener('keydown', enableAudio);
    };

    document.addEventListener('click', enableAudio, { once: true });
    document.addEventListener('keydown', enableAudio, { once: true });

    this.attachUIEvents();
    this.updateAudioButtonState();
  },

  ensureContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.value = this.isMuted ? 0 : 0.35;
        this.masterGain.connect(this.ctx.destination);
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  },

  // 1. Minecraft UI Click / Wood Plink Sound
  playClick() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    const now = this.ctx.currentTime;

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(440, now);
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.04);
    osc.frequency.exponentialRampToValueAtTime(220, now + 0.08);

    gain.gain.setValueAtTime(0.3, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);

    osc.connect(gain);
    gain.connect(this.masterGain);

    osc.start(now);
    osc.stop(now + 0.09);
  },

  // 2. Mystical Modal Open Swoosh
  playModalOpen() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    const filter = this.ctx.createBiquadFilter();
    const now = this.ctx.currentTime;

    osc.type = 'sine';
    osc.frequency.setValueAtTime(260, now);
    osc.frequency.exponentialRampToValueAtTime(520, now + 0.18);

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, now);
    filter.frequency.linearRampToValueAtTime(2400, now + 0.18);

    gain.gain.setValueAtTime(0.01, now);
    gain.gain.linearRampToValueAtTime(0.25, now + 0.08);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.22);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(this.masterGain);

    osc.start(now);
    osc.stop(now + 0.23);
  },

  // 3. Victorious Boss Slain / Level-Up Chime (Major Arpeggio)
  playLevelUp() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    const now = this.ctx.currentTime;

    notes.forEach((freq, index) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const noteStart = now + index * 0.08;

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, noteStart);

      gain.gain.setValueAtTime(0, noteStart);
      gain.gain.linearRampToValueAtTime(0.3, noteStart + 0.03);
      gain.gain.exponentialRampToValueAtTime(0.001, noteStart + 0.45);

      osc.connect(gain);
      gain.connect(this.masterGain);

      osc.start(noteStart);
      osc.stop(noteStart + 0.46);
    });
  },

  // 4. Ambient Dark Fantasy Drone / Atmospheric Soundscape
  toggleAmbientMusic() {
    this.ensureContext();
    if (this.isAmbientPlaying) {
      this.stopAmbientMusic();
    } else {
      this.startAmbientMusic();
    }
  },

  startAmbientMusic() {
    if (!this.ctx) return;
    this.stopAmbientMusic();

    const rootFreq = 65.41; // C2 deep bass
    const chords = [rootFreq, rootFreq * 1.5, rootFreq * 1.88, rootFreq * 2.25]; // C, G, Bb, D (Mystical Dark Minor 9th)

    const ambientGain = this.ctx.createGain();
    ambientGain.gain.setValueAtTime(0.001, this.ctx.currentTime);
    ambientGain.gain.linearRampToValueAtTime(0.12, this.ctx.currentTime + 3); // Slow 3s fade in

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(450, this.ctx.currentTime);

    chords.forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      osc.type = i % 2 === 0 ? 'sine' : 'triangle';
      osc.frequency.setValueAtTime(freq + (Math.random() * 0.6 - 0.3), this.ctx.currentTime); // Subtle chorus detune

      osc.connect(filter);
      osc.start();
      this.ambientNodes.push(osc);
    });

    filter.connect(ambientGain);
    ambientGain.connect(this.masterGain);
    this.ambientNodes.push(ambientGain);
    this.isAmbientPlaying = true;
    this.updateAudioButtonState();
  },

  stopAmbientMusic() {
    if (this.ambientNodes.length > 0) {
      this.ambientNodes.forEach(node => {
        try {
          if (node.stop) node.stop();
          if (node.disconnect) node.disconnect();
        } catch (e) {}
      });
      this.ambientNodes = [];
    }
    this.isAmbientPlaying = false;
    this.updateAudioButtonState();
  },

  toggleMute() {
    this.isMuted = !this.isMuted;
    localStorage.setItem('wiki_audio_muted', this.isMuted);
    if (this.masterGain) {
      this.masterGain.gain.setValueAtTime(this.isMuted ? 0 : 0.35, this.ctx ? this.ctx.currentTime : 0);
    }
    if (this.isMuted && this.isAmbientPlaying) {
      this.stopAmbientMusic();
    }
    this.updateAudioButtonState();
    if (!this.isMuted) this.playClick();
  },

  updateAudioButtonState() {
    const btn = document.getElementById('audio-toggle-btn');
    if (btn) {
      if (this.isMuted) {
        btn.innerHTML = `<span>🔇</span> <span class="vi-text">Tắt Âm</span><span class="en-text">Muted</span>`;
        btn.style.borderColor = 'var(--border-subtle)';
        btn.style.color = 'var(--text-muted)';
      } else if (this.isAmbientPlaying) {
        btn.innerHTML = `<span>🎵</span> <span class="vi-text">Nhạc Bật</span><span class="en-text">Ambient ON</span>`;
        btn.style.borderColor = 'var(--accent-cyan)';
        btn.style.color = 'var(--accent-cyan)';
      } else {
        btn.innerHTML = `<span>🔊</span> <span class="vi-text">Hiệu Ứng</span><span class="en-text">SFX ON</span>`;
        btn.style.borderColor = 'var(--accent-gold)';
        btn.style.color = 'var(--accent-gold)';
      }
    }
  },

  attachUIEvents() {
    document.addEventListener('click', (e) => {
      const target = e.target.closest('button, .nav-link, .card, .item-card, .used-in-chip, .ingredient-chip, .select-filter, .stat-box');
      if (target && !target.id?.includes('audio-toggle')) {
        this.playClick();
      }
    });
  }
};

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  AudioEngine.init();
  const audioBtn = document.getElementById('audio-toggle-btn');
  if (audioBtn) {
    audioBtn.addEventListener('click', () => {
      if (AudioEngine.isMuted) {
        AudioEngine.toggleMute();
      } else if (!AudioEngine.isAmbientPlaying) {
        AudioEngine.startAmbientMusic();
      } else {
        AudioEngine.toggleMute();
      }
    });
  }
});
