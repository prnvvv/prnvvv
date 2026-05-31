<div align="center">

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- NEURAL NETWORK HEADER — AI COMMAND CENTER                                -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<svg viewBox="0 0 1000 460" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg-glow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#0a1628"/>
      <stop offset="50%" stop-color="#080e1a"/>
      <stop offset="100%" stop-color="#05080f"/>
    </radialGradient>
    <radialGradient id="center-glow" cx="50%" cy="45%" r="35%">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="text-glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff"/>
      <stop offset="50%" stop-color="#4a9eff"/>
      <stop offset="100%" stop-color="#00d4ff"/>
    </linearGradient>
    <linearGradient id="status-gradient" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#4a9eff" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.8"/>
    </linearGradient>
    <radialGradient id="node-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#00d4ff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="node-blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4a9eff" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#4a9eff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#4a9eff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="node-purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#a855f7" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0"/>
    </radialGradient>

    <style>
      @keyframes nn-pulse-1 { 0%,100%{ opacity:0.3; r:3 } 50%{ opacity:1; r:6 } }
      @keyframes nn-pulse-2 { 0%,100%{ opacity:0.2; r:2 } 50%{ opacity:0.8; r:5 } }
      @keyframes nn-pulse-3 { 0%,100%{ opacity:0.25; r:2.5 } 50%{ opacity:0.9; r:5.5 } }
      @keyframes nn-flow { 0%{ stroke-dashoffset:300 } 100%{ stroke-dashoffset:0 } }
      @keyframes nn-flow-rev { 0%{ stroke-dashoffset:-300 } 100%{ stroke-dashoffset:0 } }
      @keyframes glitch { 0%,90%,94%,100%{ opacity:1; transform:translate(0) }
                          91%{ opacity:0.8; transform:translate(-2px,1px) }
                          93%{ opacity:0.9; transform:translate(2px,-1px) } }
      @keyframes scanline { 0%{ transform:translateY(-460px) }
                            100%{ transform:translateY(460px) } }
      @keyframes blink { 0%,100%{ opacity:1 } 50%{ opacity:0 } }
      @keyframes status-pulse { 0%,100%{ opacity:0.4 } 50%{ opacity:1 } }
      @keyframes border-flicker { 0%,100%{ opacity:0.15 } 50%{ opacity:0.3 } }
      @keyframes typing { from{ width:0 } to{ width:580px } }
      @keyframes caret { 0%,100%{ opacity:1 } 50%{ opacity:0 } }
      
      .node-1 { animation: nn-pulse-1 3s ease-in-out infinite }
      .node-2 { animation: nn-pulse-2 4s ease-in-out infinite }
      .node-3 { animation: nn-pulse-3 2.5s ease-in-out infinite }
      .node-4 { animation: nn-pulse-1 3.5s ease-in-out infinite; animation-delay:1s }
      .node-5 { animation: nn-pulse-2 2.8s ease-in-out infinite; animation-delay:0.5s }
      
      .edge-fwd { stroke-dasharray:6; animation: nn-flow 3s linear infinite }
      .edge-rev { stroke-dasharray:4; animation: nn-flow-rev 4s linear infinite }
      .edge-fwd-2 { stroke-dasharray:3; animation: nn-flow 2.5s linear infinite; animation-delay:0.5s }
      .edge-rev-2 { stroke-dasharray:5; animation: nn-flow-rev 3.5s linear infinite; animation-delay:1s }

      .glitch-text { animation: glitch 5s ease-in-out infinite }
      .scanlines { animation: scanline 4s linear infinite }
      .status-dot { animation: status-pulse 2s ease-in-out infinite }
      .border-line { animation: border-flicker 3s ease-in-out infinite }
      
      .typewriter { overflow:hidden; white-space:nowrap; animation: typing 3s steps(40) 0.5s both }
      .caret { animation: caret 0.8s step-end infinite }
    </style>

    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-strong">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="1000" height="460" fill="url(#bg-glow)"/>
  <rect width="1000" height="460" fill="url(#center-glow)"/>

  <g class="scanlines" opacity="0.04">
    <line x1="0" y1="0" x2="1000" y2="0" stroke="#00d4ff" stroke-width="460"/>
    <line x1="0" y1="2" x2="1000" y2="2" stroke="#000" stroke-width="458"/>
  </g>

  <rect x="0" y="0" width="1000" height="1" fill="#00d4ff" opacity="0.3" class="border-line"/>
  <rect x="0" y="0" width="1000" height="2" fill="url(#status-gradient)" opacity="0.15"/>

  <!-- NEURAL NETWORK EDGES -->
  <g opacity="0.3">
    <line x1="80" y1="80" x2="180" y2="65" stroke="#00d4ff" stroke-width="0.8" class="edge-fwd"/>
    <line x1="180" y1="65" x2="280" y2="90" stroke="#4a9eff" stroke-width="0.6" class="edge-rev"/>
    <line x1="280" y1="90" x2="400" y2="60" stroke="#00d4ff" stroke-width="0.7" class="edge-fwd"/>
    <line x1="400" y1="60" x2="520" y2="85" stroke="#4a9eff" stroke-width="0.5" class="edge-rev-2"/>
    <line x1="520" y1="85" x2="640" y2="55" stroke="#00d4ff" stroke-width="0.8" class="edge-fwd"/>
    <line x1="640" y1="55" x2="760" y2="75" stroke="#a855f7" stroke-width="0.6" class="edge-fwd-2"/>
    <line x1="760" y1="75" x2="880" y2="50" stroke="#00d4ff" stroke-width="0.7" class="edge-rev"/>
    <line x1="880" y1="50" x2="950" y2="80" stroke="#4a9eff" stroke-width="0.5" class="edge-fwd"/>
    <line x1="50" y1="160" x2="160" y2="145" stroke="#00d4ff" stroke-width="0.7" class="edge-rev"/>
    <line x1="160" y1="145" x2="300" y2="170" stroke="#4a9eff" stroke-width="0.6" class="edge-fwd-2"/>
    <line x1="300" y1="170" x2="430" y2="140" stroke="#a855f7" stroke-width="0.5" class="edge-rev"/>
    <line x1="430" y1="140" x2="570" y2="165" stroke="#00d4ff" stroke-width="0.7" class="edge-fwd"/>
    <line x1="570" y1="165" x2="700" y2="135" stroke="#4a9eff" stroke-width="0.6" class="edge-rev-2"/>
    <line x1="700" y1="135" x2="830" y2="155" stroke="#00d4ff" stroke-width="0.5" class="edge-fwd"/>
    <line x1="830" y1="155" x2="940" y2="130" stroke="#a855f7" stroke-width="0.7" class="edge-rev"/>
    <line x1="180" y1="65" x2="160" y2="145" stroke="#00d4ff" stroke-width="0.4" class="edge-rev-2"/>
    <line x1="280" y1="90" x2="300" y2="170" stroke="#4a9eff" stroke-width="0.4" class="edge-fwd"/>
    <line x1="400" y1="60" x2="430" y2="140" stroke="#00d4ff" stroke-width="0.4" class="edge-rev"/>
    <line x1="520" y1="85" x2="570" y2="165" stroke="#a855f7" stroke-width="0.4" class="edge-fwd-2"/>
    <line x1="640" y1="55" x2="700" y2="135" stroke="#00d4ff" stroke-width="0.4" class="edge-rev"/>
    <line x1="760" y1="75" x2="830" y2="155" stroke="#4a9eff" stroke-width="0.4" class="edge-fwd"/>
    <line x1="100" y1="320" x2="210" y2="340" stroke="#00d4ff" stroke-width="0.7" class="edge-fwd"/>
    <line x1="210" y1="340" x2="350" y2="310" stroke="#4a9eff" stroke-width="0.6" class="edge-rev"/>
    <line x1="350" y1="310" x2="480" y2="345" stroke="#a855f7" stroke-width="0.5" class="edge-fwd-2"/>
    <line x1="480" y1="345" x2="620" y2="315" stroke="#00d4ff" stroke-width="0.7" class="edge-rev"/>
    <line x1="620" y1="315" x2="750" y2="340" stroke="#4a9eff" stroke-width="0.6" class="edge-fwd"/>
    <line x1="750" y1="340" x2="880" y2="310" stroke="#00d4ff" stroke-width="0.5" class="edge-rev-2"/>
    <line x1="880" y1="310" x2="960" y2="345" stroke="#a855f7" stroke-width="0.7" class="edge-fwd"/>
    <line x1="160" y1="145" x2="210" y2="340" stroke="#00d4ff" stroke-width="0.35" class="edge-rev"/>
    <line x1="300" y1="170" x2="350" y2="310" stroke="#4a9eff" stroke-width="0.35" class="edge-fwd"/>
    <line x1="570" y1="165" x2="620" y2="315" stroke="#00d4ff" stroke-width="0.35" class="edge-rev-2"/>
    <line x1="700" y1="135" x2="750" y2="340" stroke="#a855f7" stroke-width="0.35" class="edge-fwd"/>
    <line x1="830" y1="155" x2="880" y2="310" stroke="#00d4ff" stroke-width="0.35" class="edge-rev"/>
  </g>

  <!-- NEURAL NETWORK NODES -->
  <circle cx="80" cy="80" r="8" fill="url(#node-cyan)" class="node-1"/>
  <circle cx="180" cy="65" r="6" fill="url(#node-blue)" class="node-2"/>
  <circle cx="280" cy="90" r="7" fill="url(#node-purple)" class="node-3"/>
  <circle cx="400" cy="60" r="5" fill="url(#node-cyan)" class="node-4"/>
  <circle cx="520" cy="85" r="8" fill="url(#node-blue)" class="node-5"/>
  <circle cx="640" cy="55" r="6" fill="url(#node-purple)" class="node-1"/>
  <circle cx="760" cy="75" r="7" fill="url(#node-cyan)" class="node-2"/>
  <circle cx="880" cy="50" r="5" fill="url(#node-blue)" class="node-3"/>
  <circle cx="950" cy="80" r="6" fill="url(#node-purple)" class="node-4"/>
  <circle cx="50" cy="160" r="6" fill="url(#node-blue)" class="node-2"/>
  <circle cx="160" cy="145" r="7" fill="url(#node-cyan)" class="node-5"/>
  <circle cx="300" cy="170" r="5" fill="url(#node-purple)" class="node-1"/>
  <circle cx="430" cy="140" r="7" fill="url(#node-blue)" class="node-3"/>
  <circle cx="570" cy="165" r="6" fill="url(#node-cyan)" class="node-4"/>
  <circle cx="700" cy="135" r="5" fill="url(#node-purple)" class="node-2"/>
  <circle cx="830" cy="155" r="7" fill="url(#node-blue)" class="node-5"/>
  <circle cx="940" cy="130" r="6" fill="url(#node-cyan)" class="node-1"/>
  <circle cx="100" cy="320" r="7" fill="url(#node-purple)" class="node-3"/>
  <circle cx="210" cy="340" r="5" fill="url(#node-cyan)" class="node-4"/>
  <circle cx="350" cy="310" r="6" fill="url(#node-blue)" class="node-2"/>
  <circle cx="480" cy="345" r="7" fill="url(#node-purple)" class="node-5"/>
  <circle cx="620" cy="315" r="5" fill="url(#node-cyan)" class="node-1"/>
  <circle cx="750" cy="340" r="6" fill="url(#node-blue)" class="node-3"/>
  <circle cx="880" cy="310" r="7" fill="url(#node-purple)" class="node-4"/>
  <circle cx="960" cy="345" r="5" fill="url(#node-cyan)" class="node-2"/>
  <circle cx="30" cy="40" r="4" fill="url(#node-blue)" class="node-2"/>
  <circle cx="970" cy="35" r="4" fill="url(#node-cyan)" class="node-5"/>
  <circle cx="40" cy="400" r="4" fill="url(#node-purple)" class="node-1"/>
  <circle cx="965" cy="420" r="4" fill="url(#node-blue)" class="node-3"/>

  <!-- CENTER CONTENT -->
  <text x="500" y="195" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="42" font-weight="900" fill="url(#text-glow)" filter="url(#glow-strong)" class="glitch-text">
    PRANNAVAKHANTH A
  </text>

  <rect x="250" y="213" width="500" height="1" fill="#00d4ff" opacity="0.3"/>
  <text x="500" y="235" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="11" fill="#4a9eff" opacity="0.8" letter-spacing="4">
    AI ENGINEER  //  COMPUTER VISION  //  LLM SYSTEMS  //  RESEARCH
  </text>
  <rect x="250" y="245" width="500" height="1" fill="#4a9eff" opacity="0.2"/>

  <!-- Typing effect -->
  <text x="500" y="272" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="13" fill="#6b7280">
    <tspan class="typewriter">
      <tspan fill="#00d4ff">$</tspan> <tspan fill="#8b949e">./identity --profile engineer --focus "AI Systems" --status active</tspan>
    </tspan>
    <tspan class="caret" fill="#00d4ff">▌</tspan>
  </text>

  <!-- SYSTEM STATUS BAR -->
  <g transform="translate(0, 420)">
    <rect x="0" y="0" width="1000" height="40" fill="#05080f" opacity="0.8"/>
    <line x1="0" y1="0" x2="1000" y2="0" stroke="#00d4ff" opacity="0.2"/>
    <circle cx="20" cy="20" r="4" fill="#10b981" class="status-dot"/>
    <text x="30" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">SYSTEM ONLINE</text>
    <line x1="130" y1="10" x2="130" y2="30" stroke="#1f2937" stroke-width="1"/>
    <text x="145" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">UPTIME: <tspan fill="#4a9eff">731d</tspan></text>
    <line x1="250" y1="10" x2="250" y2="30" stroke="#1f2937" stroke-width="1"/>
    <text x="265" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">REPOS: <tspan fill="#00d4ff">32</tspan></text>
    <text x="500" y="24" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#4a9eff" opacity="0.6">[ AI COMMAND CENTER v2.0 // ENGINEERING PORTFOLIO ]</text>
    <text x="735" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">STREAK: <tspan fill="#f59e0b">---</tspan></text>
    <line x1="820" y1="10" x2="820" y2="30" stroke="#1f2937" stroke-width="1"/>
    <text x="835" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">CONTRIB: <tspan fill="#10b981">2,340+</tspan></text>
    <line x1="930" y1="10" x2="930" y2="30" stroke="#1f2937" stroke-width="1"/>
    <circle cx="950" cy="20" r="4" fill="#00d4ff" class="status-dot"/>
    <text x="960" y="24" font-family="'Courier New',Courier,monospace" font-size="10" fill="#00d4ff">IDLE</text>
  </g>
</svg>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CONTACT GATEWAY                                                        -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<br>

<a href="https://www.linkedin.com/in/prannavakhanth-a-59b98228a/">
  <img src="https://img.shields.io/badge/LINKEDIN-0a0a0f?style=for-the-badge&logo=linkedin&logoColor=00d4ff&labelColor=0a1628&color=0d1117" alt="LinkedIn"/>
</a>&nbsp;
<a href="mailto:prannavakhanth12@gmail.com">
  <img src="https://img.shields.io/badge/CONTACT-0a0a0f?style=for-the-badge&logo=gmail&logoColor=4a9eff&labelColor=0a1628&color=0d1117" alt="Email"/>
</a>&nbsp;
<a href="https://kaggle.com/prnvkhanth">
  <img src="https://img.shields.io/badge/KAGGLE-0a0a0f?style=for-the-badge&logo=kaggle&logoColor=a855f7&labelColor=0a1628&color=0d1117" alt="Kaggle"/>
</a>&nbsp;
<a href="https://www.leetcode.com/prnv12__">
  <img src="https://img.shields.io/badge/LEETCODE-0a0a0f?style=for-the-badge&logo=leetcode&logoColor=f59e0b&labelColor=0a1628&color=0d1117" alt="LeetCode"/>
</a>&nbsp;
<a href="https://github.com/prnvvv">
  <img src="https://img.shields.io/badge/GITHUB-0a0a0f?style=for-the-badge&logo=github&logoColor=10b981&labelColor=0a1628&color=0d1117" alt="GitHub"/>
</a>

<br><br>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CIRCUIT DIVIDER                                                          -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<svg viewBox="0 0 1000 70" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="circuit-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="20%" stop-color="#00d4ff" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#a855f7" stop-opacity="0.4"/>
      <stop offset="80%" stop-color="#4a9eff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <style>
      @keyframes circuit-pulse { 0%,100%{ opacity:0.3 } 50%{ opacity:1 } }
      @keyframes circuit-flow { 0%{ stroke-dashoffset:200 } 100%{ stroke-dashoffset:0 } }
      .c-pulse { animation: circuit-pulse 2.5s ease-in-out infinite }
      .c-flow { stroke-dasharray:4; animation: circuit-flow 2s linear infinite }
    </style>
  </defs>
  <rect x="0" y="0" width="1000" height="70" fill="#05080f" opacity="0.5"/>
  <g fill="none" stroke="url(#circuit-grad)" stroke-width="1.5" opacity="0.6">
    <polyline points="0,35 120,35 140,20 260,20 280,35 350,35" class="c-flow"/>
    <polyline points="650,35 720,35 740,20 860,20 880,35 1000,35" class="c-flow" style="animation-delay:1s"/>
    <line x1="120" y1="35" x2="140" y2="20"/>
    <line x1="260" y1="20" x2="280" y2="35"/>
    <line x1="720" y1="35" x2="740" y2="20"/>
    <line x1="860" y1="20" x2="880" y2="35"/>
    <polyline points="350,35 370,50 490,50 510,35 600,35 620,50 650,50 650,35" class="c-flow" style="animation-delay:0.5s"/>
  </g>
  <circle cx="120" cy="35" r="3" fill="#00d4ff" class="c-pulse"/>
  <circle cx="280" cy="35" r="3" fill="#4a9eff" class="c-pulse" style="animation-delay:0.5s"/>
  <circle cx="350" cy="35" r="3" fill="#a855f7" class="c-pulse" style="animation-delay:1s"/>
  <circle cx="600" cy="35" r="3" fill="#00d4ff" class="c-pulse" style="animation-delay:1.5s"/>
  <circle cx="720" cy="35" r="3" fill="#4a9eff" class="c-pulse" style="animation-delay:0.8s"/>
  <circle cx="880" cy="35" r="3" fill="#a855f7" class="c-pulse" style="animation-delay:1.2s"/>
  <g stroke="#00d4ff" stroke-width="1" opacity="0.2">
    <polyline points="15,55 15,15 25,15" fill="none"/>
    <polyline points="985,55 985,15 975,15" fill="none"/>
  </g>
</svg>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- SECTION 1 :: SYSTEM PROFILE                                              -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes hdr-flicker { 0%,100%{ opacity:0.9 } 50%{ opacity:0.5 } }
    .hdr-pulse { animation: hdr-flicker 4s ease-in-out infinite }
  </style>
  <rect x="0" y="12" width="400" height="2" fill="#00d4ff" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#4a9eff" letter-spacing="6" class="hdr-pulse">⏣ SYSTEM PROFILE</text>
  <rect x="0" y="14" width="400" height="2" fill="#00d4ff" opacity="0.15"/>
</svg>

<br>

<table align="center" width="860">
  <tr>
    <td width="280" valign="top">

<svg viewBox="0 0 270 230" width="270" height="230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="term-header" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="270" height="230" rx="4" fill="#0a0a0f" stroke="#00d4ff" stroke-width="0.8" opacity="0.6"/>
  <rect x="0" y="0" width="270" height="24" rx="4" fill="url(#term-header)"/>
  <circle cx="12" cy="12" r="3" fill="#ef4444" opacity="0.8"/>
  <circle cx="24" cy="12" r="3" fill="#f59e0b" opacity="0.8"/>
  <circle cx="36" cy="12" r="3" fill="#10b981" opacity="0.8"/>
  <text x="136" y="16" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">IDENTITY.SYS</text>
  <text x="14" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#00d4ff">$</text>
  <text x="26" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#8b949e">cat /etc/profile</text>
  <text x="14" y="66" font-family="'Courier New',Courier,monospace" font-size="10" fill="#4a9eff">───────────────</text>
  <text x="14" y="86" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Name:</text>
  <text x="80" y="86" font-family="'Courier New',Courier,monospace" font-size="10" fill="#00d4ff">Prannavakhanth A</text>
  <text x="14" y="104" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Role:</text>
  <text x="80" y="104" font-family="'Courier New',Courier,monospace" font-size="10" fill="#4a9eff">AI Engineer</text>
  <text x="14" y="122" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Education:</text>
  <text x="80" y="122" font-family="'Courier New',Courier,monospace" font-size="10" fill="#8b949e">B.Tech CSE</text>
  <text x="14" y="140" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Inst:</text>
  <text x="80" y="140" font-family="'Courier New',Courier,monospace" font-size="10" fill="#8b949e">VIT Chennai</text>
  <text x="14" y="158" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">CGPA:</text>
  <text x="80" y="158" font-family="'Courier New',Courier,monospace" font-size="10" fill="#10b981">9.02 / 10.0</text>
  <text x="14" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Status:</text>
  <text x="80" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#10b981">Active ██</text>
  <text x="14" y="194" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Focus:</text>
  <text x="80" y="194" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7">CV · LLM · AgML</text>
  <text x="14" y="216" font-family="'Courier New',Courier,monospace" font-size="10" fill="#4a9eff">───────────────</text>
</svg>

    </td>
    <td width="280" valign="top">

<svg viewBox="0 0 270 230" width="270" height="230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="term-hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="270" height="230" rx="4" fill="#0a0a0f" stroke="#a855f7" stroke-width="0.8" opacity="0.6"/>
  <rect x="0" y="0" width="270" height="24" rx="4" fill="url(#term-hdr)"/>
  <circle cx="12" cy="12" r="3" fill="#ef4444" opacity="0.8"/>
  <circle cx="24" cy="12" r="3" fill="#f59e0b" opacity="0.8"/>
  <circle cx="36" cy="12" r="3" fill="#10b981" opacity="0.8"/>
  <text x="136" y="16" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">RESEARCH.SYS</text>
  <text x="14" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7">$</text>
  <text x="26" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#8b949e">cat research.log</text>
  <text x="14" y="66" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7">───────────────</text>
  <text x="14" y="86" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Position:</text>
  <text x="90" y="86" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7">Project Intern</text>
  <text x="14" y="104" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Institution:</text>
  <text x="90" y="104" font-family="'Courier New',Courier,monospace" font-size="10" fill="#c084fc">IIT Ropar</text>
  <text x="14" y="122" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Domain:</text>
  <text x="90" y="122" font-family="'Courier New',Courier,monospace" font-size="10" fill="#818cf8">Agricultural ML</text>
  <text x="14" y="140" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Output:</text>
  <text x="90" y="140" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">Patent Published</text>
  <text x="14" y="158" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">System:</text>
  <text x="90" y="158" font-family="'Courier New',Courier,monospace" font-size="10" fill="#00d4ff">CropCore AI</text>
  <text x="14" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Focus:</text>
  <text x="90" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#c084fc">Smart Automation</text>
  <text x="14" y="194" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Status:</text>
  <text x="90" y="194" font-family="'Courier New',Courier,monospace" font-size="10" fill="#10b981">Research Active</text>
  <text x="14" y="216" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7">───────────────</text>
</svg>

    </td>
    <td width="300" valign="top">

<svg viewBox="0 0 280 230" width="280" height="230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="achieve-hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="280" height="230" rx="4" fill="#0a0a0f" stroke="#f59e0b" stroke-width="0.8" opacity="0.6"/>
  <rect x="0" y="0" width="280" height="24" rx="4" fill="url(#achieve-hdr)"/>
  <circle cx="12" cy="12" r="3" fill="#ef4444" opacity="0.8"/>
  <circle cx="24" cy="12" r="3" fill="#f59e0b" opacity="0.8"/>
  <circle cx="36" cy="12" r="3" fill="#10b981" opacity="0.8"/>
  <text x="141" y="16" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">ACHIEVEMENTS.LOG</text>
  <text x="14" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">$</text>
  <text x="26" y="44" font-family="'Courier New',Courier,monospace" font-size="10" fill="#8b949e">cat milestones.log | head -5</text>
  <text x="14" y="66" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">───</text>
  <text x="14" y="88" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">[01]</text>
  <text x="52" y="88" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">HackHub'25 Winner</text>
  <text x="190" y="88" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">IEEE · GitHub</text>
  <text x="14" y="110" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">[02]</text>
  <text x="52" y="110" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Patent Published</text>
  <text x="190" y="110" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">CropCore AI</text>
  <text x="14" y="132" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">[03]</text>
  <text x="52" y="132" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Research Intern</text>
  <text x="190" y="132" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">IIT Ropar</text>
  <text x="14" y="154" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">[04]</text>
  <text x="52" y="154" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Chairperson</text>
  <text x="190" y="154" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">OSPC, VITC</text>
  <text x="14" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">[05]</text>
  <text x="52" y="176" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">State Athlete</text>
  <text x="190" y="176" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">TNCA Cricket</text>
  <text x="14" y="216" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b">───</text>
</svg>

    </td>
  </tr>
</table>

<br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- HOLOGRAPHIC DIVIDER                                                      -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<svg viewBox="0 0 1000 80" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="holographic" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="25%" stop-color="#4a9eff" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#a855f7" stop-opacity="0.35"/>
      <stop offset="75%" stop-color="#ec4899" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="holo-line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00d4ff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <style>
      @keyframes holo-shift { 0%{ opacity:0.1; transform:translateX(0) }
                              50%{ opacity:0.3; transform:translateX(10px) }
                              100%{ opacity:0.1; transform:translateX(0) } }
      @keyframes holo-glow { 0%,100%{ opacity:0.15 } 50%{ opacity:0.4 } }
      .holo-move { animation: holo-shift 6s ease-in-out infinite }
      .holo-glow { animation: holo-glow 3s ease-in-out infinite }
    </style>
  </defs>
  <rect x="0" y="0" width="1000" height="80" fill="#05080f" opacity="0.3"/>
  <g opacity="0.15">
    <line x1="0" y1="20" x2="1000" y2="20" stroke="#00d4ff" stroke-width="0.5"/>
    <line x1="0" y1="40" x2="1000" y2="40" stroke="#4a9eff" stroke-width="0.5"/>
    <line x1="0" y1="60" x2="1000" y2="60" stroke="#a855f7" stroke-width="0.5"/>
    <line x1="250" y1="0" x2="250" y2="80" stroke="#00d4ff" stroke-width="0.3"/>
    <line x1="500" y1="0" x2="500" y2="80" stroke="#4a9eff" stroke-width="0.3"/>
    <line x1="750" y1="0" x2="750" y2="80" stroke="#a855f7" stroke-width="0.3"/>
  </g>
  <rect x="0" y="38" width="1000" height="4" fill="url(#holographic)" class="holo-glow"/>
  <text x="500" y="48" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff" opacity="0.4" letter-spacing="3" class="holo-move">◈ TECHNOLOGY ECOSYSTEM ◈</text>
  <g stroke="#00d4ff" stroke-width="1" opacity="0.15">
    <polyline points="10,70 10,10 20,10" fill="none"/>
    <polyline points="990,70 990,10 980,10" fill="none"/>
  </g>
</svg>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- SECTION 2 :: TECHNOLOGY ECOSYSTEM                                        -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<!-- INTELLIGENCE LAYER -->
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="14" width="860" height="1" fill="#00d4ff" opacity="0.15"/>
  <rect x="340" y="6" width="180" height="20" rx="10" fill="#00d4ff" opacity="0.08"/>
  <text x="430" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#00d4ff" letter-spacing="2">◈ INTELLIGENCE LAYER — AI / ML ◈</text>
</svg>

<br><br>

<a href="https://python.org">
  <img src="https://img.shields.io/badge/Python-0a1628?style=for-the-badge&logo=python&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="Python"/>
</a>&nbsp;
<a href="https://tensorflow.org">
  <img src="https://img.shields.io/badge/TensorFlow-0a1628?style=for-the-badge&logo=tensorflow&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="TensorFlow"/>
</a>&nbsp;
<a href="https://pytorch.org">
  <img src="https://img.shields.io/badge/PyTorch-0a1628?style=for-the-badge&logo=pytorch&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="PyTorch"/>
</a>&nbsp;
<a href="https://scikit-learn.org">
  <img src="https://img.shields.io/badge/Scikit--Learn-0a1628?style=for-the-badge&logo=scikitlearn&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="Scikit-learn"/>
</a>&nbsp;
<a href="https://opencv.org">
  <img src="https://img.shields.io/badge/OpenCV-0a1628?style=for-the-badge&logo=opencv&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="OpenCV"/>
</a>&nbsp;
<a href="https://huggingface.co">
  <img src="https://img.shields.io/badge/Transformers-0a1628?style=for-the-badge&logo=huggingface&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="HuggingFace"/>
</a>&nbsp;
<a href="https://mediapipe.dev">
  <img src="https://img.shields.io/badge/MediaPipe-0a1628?style=for-the-badge&logo=google&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="MediaPipe"/>
</a>&nbsp;
<a href="https://ultralytics.com/yolo">
  <img src="https://img.shields.io/badge/YOLO-0a1628?style=for-the-badge&logo=ultralytics&logoColor=00d4ff&labelColor=0a0a0f&color=0d1117" alt="YOLO"/>
</a>

<br><br>

<!-- DATA LAYER -->
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="14" width="860" height="1" fill="#10b981" opacity="0.15"/>
  <rect x="370" y="6" width="120" height="20" rx="10" fill="#10b981" opacity="0.08"/>
  <text x="430" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#10b981" letter-spacing="2">◈ DATA LAYER — ANALYTICS ◈</text>
</svg>

<br><br>

<a href="https://pandas.pydata.org">
  <img src="https://img.shields.io/badge/Pandas-052e16?style=for-the-badge&logo=pandas&logoColor=10b981&labelColor=0a0a0f&color=0d1117" alt="Pandas"/>
</a>&nbsp;
<a href="https://numpy.org">
  <img src="https://img.shields.io/badge/NumPy-052e16?style=for-the-badge&logo=numpy&logoColor=10b981&labelColor=0a0a0f&color=0d1117" alt="NumPy"/>
</a>&nbsp;
<a href="https://plotly.com">
  <img src="https://img.shields.io/badge/Plotly-052e16?style=for-the-badge&logo=plotly&logoColor=10b981&labelColor=0a0a0f&color=0d1117" alt="Plotly"/>
</a>&nbsp;
<a href="https://mysql.com">
  <img src="https://img.shields.io/badge/MySQL-052e16?style=for-the-badge&logo=mysql&logoColor=10b981&labelColor=0a0a0f&color=0d1117" alt="MySQL"/>
</a>&nbsp;
<a href="https://r-project.org">
  <img src="https://img.shields.io/badge/R-052e16?style=for-the-badge&logo=r&logoColor=10b981&labelColor=0a0a0f&color=0d1117" alt="R"/>
</a>

<br><br>

<!-- SYSTEMS LAYER -->
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="14" width="860" height="1" fill="#a855f7" opacity="0.15"/>
  <rect x="370" y="6" width="120" height="20" rx="10" fill="#a855f7" opacity="0.08"/>
  <text x="430" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#a855f7" letter-spacing="2">◈ SYSTEMS LAYER — BACKEND ◈</text>
</svg>

<br><br>

<a href="https://fastapi.tiangolo.com">
  <img src="https://img.shields.io/badge/FastAPI-1e0a29?style=for-the-badge&logo=fastapi&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="FastAPI"/>
</a>&nbsp;
<a href="https://docker.com">
  <img src="https://img.shields.io/badge/Docker-1e0a29?style=for-the-badge&logo=docker&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="Docker"/>
</a>&nbsp;
<a href="https://aws.amazon.com">
  <img src="https://img.shields.io/badge/AWS-1e0a29?style=for-the-badge&logo=amazonwebservices&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="AWS"/>
</a>&nbsp;
<a href="https://java.com">
  <img src="https://img.shields.io/badge/Java-1e0a29?style=for-the-badge&logo=openjdk&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="Java"/>
</a>&nbsp;
<a href="https://isocpp.org">
  <img src="https://img.shields.io/badge/C++-1e0a29?style=for-the-badge&logo=cplusplus&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="C++"/>
</a>&nbsp;
<a href="https://en.wikipedia.org/wiki/C_(programming_language)">
  <img src="https://img.shields.io/badge/C-1e0a29?style=for-the-badge&logo=c&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="C"/>
</a>&nbsp;
<a href="https://postgresql.org">
  <img src="https://img.shields.io/badge/PostgreSQL-1e0a29?style=for-the-badge&logo=postgresql&logoColor=a855f7&labelColor=0a0a0f&color=0d1117" alt="PostgreSQL"/>
</a>

<br><br>

<!-- INTERFACE LAYER -->
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="14" width="860" height="1" fill="#f59e0b" opacity="0.15"/>
  <rect x="370" y="6" width="120" height="20" rx="10" fill="#f59e0b" opacity="0.08"/>
  <text x="430" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b" letter-spacing="2">◈ INTERFACE LAYER — FRONTEND ◈</text>
</svg>

<br><br>

<a href="https://reactjs.org">
  <img src="https://img.shields.io/badge/React-2e1a00?style=for-the-badge&logo=react&logoColor=f59e0b&labelColor=0a0a0f&color=0d1117" alt="React"/>
</a>&nbsp;
<a href="https://javascript.com">
  <img src="https://img.shields.io/badge/JavaScript-2e1a00?style=for-the-badge&logo=javascript&logoColor=f59e0b&labelColor=0a0a0f&color=0d1117" alt="JavaScript"/>
</a>&nbsp;
<a href="https://html.spec.whatwg.org">
  <img src="https://img.shields.io/badge/HTML5-2e1a00?style=for-the-badge&logo=html5&logoColor=f59e0b&labelColor=0a0a0f&color=0d1117" alt="HTML5"/>
</a>&nbsp;
<a href="https://w3.org/Style/CSS/">
  <img src="https://img.shields.io/badge/CSS3-2e1a00?style=for-the-badge&logo=css3&logoColor=f59e0b&labelColor=0a0a0f&color=0d1117" alt="CSS3"/>
</a>

<br><br>

</div>
<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- NEURAL DIVIDER                                                           -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<svg viewBox="0 0 1000 90" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="neural-div" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="30%" stop-color="#00d4ff" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#4a9eff" stop-opacity="0.3"/>
      <stop offset="70%" stop-color="#a855f7" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <style>
      @keyframes wave-pulse { 0%,100%{ opacity:0.15 } 50%{ opacity:0.35 } }
      .wave-p { animation: wave-pulse 4s ease-in-out infinite }
      .wave-p-2 { animation: wave-pulse 5s ease-in-out infinite; animation-delay:1s }
    </style>
  </defs>
  <rect x="0" y="0" width="1000" height="90" fill="#05080f" opacity="0.3"/>

  <g opacity="0.2">
    <path d="M0,45 Q100,25 200,45 T400,45 T600,45 T800,45 T1000,45" fill="none" stroke="#00d4ff" stroke-width="0.8" class="wave-p"/>
    <path d="M0,55 Q100,35 200,55 T400,55 T600,55 T800,55 T1000,55" fill="none" stroke="#4a9eff" stroke-width="0.6" class="wave-p-2"/>
  </g>

  <g transform="translate(500,45)">
    <circle cx="0" cy="0" r="20" fill="none" stroke="#00d4ff" stroke-width="0.5" opacity="0.15">
      <animate attributeName="r" values="20;25;20" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.15;0.05;0.15" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="8" fill="#00d4ff" opacity="0.2">
      <animate attributeName="r" values="8;10;8" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.2;0.4;0.2" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="3" fill="#00d4ff" opacity="0.6"/>
  </g>

  <text x="500" y="78" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280" opacity="0.5" letter-spacing="4">MISSION FILES  //  ACTIVE PROJECTS</text>
</svg>

<br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- SECTION 3 :: PROJECT DASHBOARD                                           -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="12" width="400" height="2" fill="#4a9eff" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#4a9eff" letter-spacing="6">⏣ PROJECT DASHBOARD</text>
  <rect x="0" y="14" width="400" height="2" fill="#4a9eff" opacity="0.15"/>
</svg>

<br>

<!-- Status Legend -->
<svg viewBox="0 0 500 28" width="500" height="28" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="14" r="4" fill="#10b981"/>
  <text x="60" y="18" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">DEPLOYED</text>
  <circle cx="150" cy="14" r="4" fill="#f59e0b"/>
  <text x="160" y="18" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">ACTIVE DEV</text>
  <circle cx="255" cy="14" r="4" fill="#a855f7"/>
  <text x="265" y="18" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">PATENT PUB</text>
  <circle cx="365" cy="14" r="4" fill="#4a9eff"/>
  <text x="375" y="18" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">COMPLETED</text>
</svg>

<br>

</div>

<!-- FILE 001 — AUTCORE -->
<details>
<summary>
<b>
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:4px">
  <circle cx="16" cy="16" r="5" fill="#10b981">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="28" y="21" font-family="'Courier New',Courier,monospace" font-size="13" fill="#00d4ff" font-weight="bold">AUTCORE</text>
  <text x="110" y="21" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">AI Autism Screening System</text>
  <rect x="720" y="10" width="65" height="14" rx="3" fill="#10b981" opacity="0.15"/>
  <text x="752" y="21" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#10b981">LIVE</text>
</svg>
</b>
</summary>

<br>

<svg viewBox="0 0 860 1" width="860" height="1" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="860" y2="0" stroke="#00d4ff" opacity="0.1"/>
</svg>

<br>

<table width="860" align="center">
  <tr>
    <td width="200" valign="top">

<svg viewBox="0 0 190 120" width="190" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="190" height="120" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASSIFICATION</text>
  <text x="10" y="36" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff">Computer Vision</text>
  <text x="10" y="52" font-family="'Courier New',Courier,monospace" font-size="9" fill="#4a9eff">Multimodal AI</text>
  <text x="10" y="74" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DOMAIN</text>
  <text x="10" y="92" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Healthcare Diagnostics</text>
</svg>

    </td>
    <td width="640" valign="top">

<svg viewBox="0 0 640 120" width="640" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="640" height="120" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">PROBLEM STATEMENT</text>
  <text x="10" y="38" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Early autism screening in India is bottlenecked by specialist</text>
  <text x="10" y="54" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">availability. Families in Tier-2/3 cities wait months for clinical</text>
  <text x="10" y="70" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">assessment. Dual-modality pipeline using CV and speech analysis.</text>
  <text x="10" y="92" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="10" y="108" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff">Python · TensorFlow · OpenCV · FastAPI · Speech Analysis</text>
</svg>

    </td>
  </tr>
</table>

<br>

<table width="860" align="center">
  <tr>
    <td width="860" align="center">
      <svg viewBox="0 0 840 100" width="840" height="100" xmlns="http://www.w3.org/2000/svg">
        <style>
          @keyframes arch-flow { 0%{ stroke-dashoffset:200 } 100%{ stroke-dashoffset:0 } }
          .arch-edge { stroke-dasharray:4; animation: arch-flow 2s linear infinite }
        </style>
        <rect x="10" y="35" width="110" height="30" rx="4" fill="#0a1628" stroke="#00d4ff" stroke-width="0.8"/>
        <text x="65" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff">Camera Input</text>
        <line x1="120" y1="50" x2="155" y2="50" stroke="#4a9eff" stroke-width="1" class="arch-edge"/>
        <rect x="155" y="35" width="120" height="30" rx="4" fill="#0a1628" stroke="#4a9eff" stroke-width="0.8"/>
        <text x="215" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#4a9eff">OpenCV Pipeline</text>
        <line x1="275" y1="50" x2="305" y2="30" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <line x1="275" y1="50" x2="305" y2="70" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <rect x="305" y="15" width="120" height="30" rx="4" fill="#0a1628" stroke="#a855f7" stroke-width="0.8"/>
        <text x="365" y="34" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#a855f7">Gaze Estimator</text>
        <rect x="305" y="55" width="120" height="30" rx="4" fill="#0a1628" stroke="#ec4899" stroke-width="0.8"/>
        <text x="365" y="74" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#ec4899">Speech Analyzer</text>
        <line x1="425" y1="30" x2="455" y2="50" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <line x1="425" y1="70" x2="455" y2="50" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <rect x="455" y="35" width="130" height="30" rx="4" fill="#0a1628" stroke="#00d4ff" stroke-width="0.8"/>
        <text x="520" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff">TF Classifier</text>
        <line x1="585" y1="50" x2="620" y2="50" stroke="#4a9eff" stroke-width="1" class="arch-edge"/>
        <rect x="620" y="35" width="100" height="30" rx="4" fill="#0a1628" stroke="#10b981" stroke-width="0.8"/>
        <text x="670" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#10b981">FastAPI REST</text>
        <line x1="720" y1="50" x2="755" y2="50" stroke="#f59e0b" stroke-width="1" class="arch-edge"/>
        <rect x="755" y="35" width="75" height="30" rx="4" fill="#0a1628" stroke="#f59e0b" stroke-width="0.8"/>
        <text x="792" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#f59e0b">Result</text>
      </svg>
    </td>
  </tr>
</table>

<br>
</details>

<svg viewBox="0 0 860 1" width="860" height="1" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="860" y2="0" stroke="#00d4ff" opacity="0.05"/>
</svg>

<br>

<!-- FILE 002 — CROPCORE -->
<details>
<summary>
<b>
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:4px">
  <circle cx="16" cy="16" r="5" fill="#a855f7"/>
  <text x="28" y="21" font-family="'Courier New',Courier,monospace" font-size="13" fill="#00d4ff" font-weight="bold">CROPCORE</text>
  <text x="125" y="21" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">AI Farming Assistant</text>
  <rect x="700" y="10" width="95" height="14" rx="3" fill="#a855f7" opacity="0.15"/>
  <text x="747" y="21" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#a855f7">PATENT PUB</text>
</svg>
</b>
</summary>

<br>

<svg viewBox="0 0 860 1" width="860" height="1" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="860" y2="0" stroke="#a855f7" opacity="0.1"/>
</svg>

<br>

<table width="860" align="center">
  <tr>
    <td width="200" valign="top">

<svg viewBox="0 0 190 120" width="190" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="190" height="120" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASSIFICATION</text>
  <text x="10" y="36" font-family="'Courier New',Courier,monospace" font-size="9" fill="#a855f7">Computer Vision</text>
  <text x="10" y="52" font-family="'Courier New',Courier,monospace" font-size="9" fill="#c084fc">Conversational AI</text>
  <text x="10" y="74" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DOMAIN</text>
  <text x="10" y="92" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">AgriTech / Food Security</text>
</svg>

    </td>
    <td width="640" valign="top">

<svg viewBox="0 0 640 120" width="640" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="640" height="120" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">PROBLEM STATEMENT</text>
  <text x="10" y="38" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Crop disease spreads silently. Smallholder farmers lose</text>
  <text x="10" y="54" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">significant yields annually. YOLO detection + conversational</text>
  <text x="10" y="70" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">assistant for real-time field-level recommendations.</text>
  <text x="10" y="92" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="10" y="108" font-family="'Courier New',Courier,monospace" font-size="9" fill="#a855f7">PyTorch · YOLO · OpenCV · React · FastAPI</text>
</svg>

    </td>
  </tr>
</table>

<br>

<table width="860" align="center">
  <tr>
    <td width="860" align="center">
      <svg viewBox="0 0 840 100" width="840" height="100" xmlns="http://www.w3.org/2000/svg">
        <style>
          @keyframes arch-flow { 0%{ stroke-dashoffset:200 } 100%{ stroke-dashoffset:0 } }
          .arch-edge { stroke-dasharray:4; animation: arch-flow 2s linear infinite }
        </style>
        <rect x="10" y="35" width="120" height="30" rx="4" fill="#0a1628" stroke="#a855f7" stroke-width="0.8"/>
        <text x="70" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#a855f7">Field Photo</text>
        <line x1="130" y1="50" x2="165" y2="50" stroke="#c084fc" stroke-width="1" class="arch-edge"/>
        <rect x="165" y="35" width="140" height="30" rx="4" fill="#0a1628" stroke="#c084fc" stroke-width="0.8"/>
        <text x="235" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#c084fc">YOLO Detection Engine</text>
        <line x1="305" y1="50" x2="335" y2="35" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <line x1="305" y1="50" x2="335" y2="65" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <rect x="335" y="20" width="120" height="30" rx="4" fill="#0a1628" stroke="#00d4ff" stroke-width="0.8"/>
        <text x="395" y="39" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#00d4ff">Disease Class.</text>
        <rect x="335" y="50" width="120" height="30" rx="4" fill="#0a1628" stroke="#10b981" stroke-width="0.8"/>
        <text x="395" y="69" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#10b981">Location Map</text>
        <line x1="455" y1="35" x2="485" y2="50" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <line x1="455" y1="65" x2="485" y2="50" stroke="#6b7280" stroke-width="0.8" class="arch-edge"/>
        <rect x="485" y="35" width="140" height="30" rx="4" fill="#0a1628" stroke="#f59e0b" stroke-width="0.8"/>
        <text x="555" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#f59e0b">Recommendation Engine</text>
        <line x1="625" y1="50" x2="660" y2="50" stroke="#f59e0b" stroke-width="1" class="arch-edge"/>
        <rect x="660" y="30" width="100" height="50" rx="4" fill="#0a1628" stroke="#10b981" stroke-width="0.8" stroke-dasharray="3"/>
        <text x="710" y="50" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">React</text>
        <text x="710" y="65" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="7" fill="#6b7280">Low-BW Optimized</text>
      </svg>
    </td>
  </tr>
</table>

<br>
</details>

<br>

<!-- FILE 003 — CAREERTRACK -->
<details>
<summary>
<b>
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:4px">
  <circle cx="16" cy="16" r="5" fill="#f59e0b">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="28" y="21" font-family="'Courier New',Courier,monospace" font-size="13" fill="#00d4ff" font-weight="bold">CAREERTRACK</text>
  <text x="145" y="21" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">AI Career Intelligence Platform</text>
  <rect x="700" y="10" width="100" height="14" rx="3" fill="#f59e0b" opacity="0.15"/>
  <text x="750" y="21" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#f59e0b">ACTIVE DEV</text>
</svg>
</b>
</summary>

<br>

<svg viewBox="0 0 860 1" width="860" height="1" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="860" y2="0" stroke="#f59e0b" opacity="0.1"/>
</svg>

<br>

<table width="860" align="center">
  <tr>
    <td width="200" valign="top">
      <svg viewBox="0 0 190 100" width="190" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="190" height="100" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
        <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASSIFICATION</text>
        <text x="10" y="36" font-family="'Courier New',Courier,monospace" font-size="9" fill="#f59e0b">NLP / LLM Systems</text>
        <text x="10" y="58" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DOMAIN</text>
        <text x="10" y="76" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Career Technology</text>
      </svg>
    </td>
    <td width="640" valign="top">
      <svg viewBox="0 0 640 100" width="640" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="640" height="100" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
        <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">PROBLEM STATEMENT</text>
        <text x="10" y="38" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Resume-to-JD misalignment is the primary reason qualified</text>
        <text x="10" y="54" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">candidates fail ATS screening. LLM-powered semantic matching</text>
        <text x="10" y="70" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">pipeline with gap analysis and targeted recommendations.</text>
        <text x="10" y="90" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
        <text x="10" y="104" font-family="'Courier New',Courier,monospace" font-size="9" fill="#f59e0b">Python · LLMs · Transformers · NLP · FastAPI</text>
      </svg>
    </td>
  </tr>
</table>
<br>
</details>

<br>

<!-- FILE 004 — CLOUDGUARD -->
<details>
<summary>
<b>
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:4px">
  <circle cx="16" cy="16" r="5" fill="#4a9eff">
    <animate attributeName="opacity" values="1;0.3;1" dur="3s" repeatCount="indefinite"/>
  </circle>
  <text x="28" y="21" font-family="'Courier New',Courier,monospace" font-size="13" fill="#00d4ff" font-weight="bold">CLOUDGUARD</text>
  <text x="145" y="21" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">ML Intrusion Detection System</text>
  <rect x="710" y="10" width="85" height="14" rx="3" fill="#4a9eff" opacity="0.15"/>
  <text x="752" y="21" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#4a9eff">IN PROG</text>
</svg>
</b>
</summary>

<br>

<svg viewBox="0 0 860 1" width="860" height="1" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="860" y2="0" stroke="#4a9eff" opacity="0.1"/>
</svg>

<br>

<table width="860" align="center">
  <tr>
    <td width="200" valign="top">
      <svg viewBox="0 0 190 100" width="190" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="190" height="100" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
        <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASSIFICATION</text>
        <text x="10" y="36" font-family="'Courier New',Courier,monospace" font-size="9" fill="#4a9eff">Anomaly Detection</text>
        <text x="10" y="52" font-family="'Courier New',Courier,monospace" font-size="9" fill="#3b82f6">Cybersecurity ML</text>
        <text x="10" y="74" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DOMAIN</text>
        <text x="10" y="92" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Cloud Security</text>
      </svg>
    </td>
    <td width="640" valign="top">
      <svg viewBox="0 0 640 100" width="640" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="640" height="100" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
        <text x="10" y="18" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">ENGINEERING APPROACH</text>
        <text x="10" y="38" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Behavioral feature engineering from AWS access logs.</text>
        <text x="10" y="54" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Ensemble classifiers score anomalous patterns. Designed to</text>
        <text x="10" y="70" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">catch novel attack vectors signature-based systems miss.</text>
        <text x="10" y="90" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
        <text x="10" y="104" font-family="'Courier New',Courier,monospace" font-size="9" fill="#4a9eff">Python · Scikit-learn · AWS · Ensemble ML</text>
      </svg>
    </td>
  </tr>
</table>
<br>
</details>

<br>

<!-- FILES 005-008 — remaining projects -->
<details>
<summary>
<b>
<svg viewBox="0 0 860 32" width="860" height="32" xmlns="http://www.w3.org/2000/svg" style="vertical-align:middle;margin-right:4px">
  <text x="16" y="21" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">EXPAND: Vision Systems · Stock Analyzer · Deadlock Analyzer · AI Chatbot</text>
  <text x="780" y="21" font-family="'Courier New',Courier,monospace" font-size="8" fill="#4a9eff">4 more ▾</text>
</svg>
</b>
</summary>

<br>

<table width="860" align="center">
  <tr>
    <td width="410" valign="top">

<svg viewBox="0 0 400 105" width="400" height="105" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="400" height="105" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <circle cx="16" cy="18" r="4" fill="#10b981"/>
  <text x="26" y="22" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff" font-weight="bold">VISION SYSTEMS</text>
  <text x="156" y="22" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">COMPLETED</text>
  <text x="10" y="42" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASS</text>
  <text x="50" y="42" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Computer Vision / HCI</text>
  <text x="10" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DESC</text>
  <text x="50" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">Real-time face/hand/pose detection suite</text>
  <text x="50" y="75" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">MediaPipe · sub-50ms latency</text>
  <text x="10" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="50" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#00d4ff">MediaPipe · OpenCV · Python</text>
</svg>

<br>

<svg viewBox="0 0 400 105" width="400" height="105" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="400" height="105" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <circle cx="16" cy="18" r="4" fill="#10b981"/>
  <text x="26" y="22" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff" font-weight="bold">STOCK ANALYZER</text>
  <text x="175" y="22" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">COMPLETED</text>
  <text x="10" y="42" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASS</text>
  <text x="50" y="42" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Time Series ML / Financial Analytics</text>
  <text x="10" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DESC</text>
  <text x="50" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">Market analysis & price modeling pipeline</text>
  <text x="50" y="75" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">Plotly dashboards · backtesting</text>
  <text x="10" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="50" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#00d4ff">Python · Pandas · Scikit-learn · Plotly</text>
</svg>

    </td>
    <td width="440" valign="top">

<svg viewBox="0 0 430 105" width="430" height="105" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="430" height="105" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <circle cx="16" cy="18" r="4" fill="#10b981"/>
  <text x="26" y="22" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff" font-weight="bold">DEADLOCK ANALYZER</text>
  <text x="175" y="22" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">COMPLETED</text>
  <text x="10" y="42" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASS</text>
  <text x="50" y="42" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">Systems Engineering / DB Theory</text>
  <text x="10" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DESC</text>
  <text x="50" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">Graph-theoretic deadlock detection for</text>
  <text x="50" y="75" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">transactional databases · cycle detection</text>
  <text x="10" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="50" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#00d4ff">Java · Graph Algorithms · DB Theory</text>
</svg>

<br>

<svg viewBox="0 0 430 105" width="430" height="105" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="430" height="105" rx="3" fill="#0a0a0f" stroke="#1f2937" stroke-width="0.5"/>
  <circle cx="16" cy="18" r="4" fill="#10b981">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="26" y="22" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff" font-weight="bold">AI CHATBOT</text>
  <text x="135" y="22" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">LIVE</text>
  <text x="10" y="42" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">CLASS</text>
  <text x="50" y="42" font-family="'Courier New',Courier,monospace" font-size="9" fill="#8b949e">NLP / Transformer Architecture</text>
  <text x="10" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">DESC</text>
  <text x="50" y="60" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">Multi-turn conversational system with</text>
  <text x="50" y="75" font-family="'Courier New',Courier,monospace" font-size="8" fill="#8b949e">persistent context · REST API</text>
  <text x="10" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#6b7280">STACK</text>
  <text x="50" y="94" font-family="'Courier New',Courier,monospace" font-size="8" fill="#00d4ff">Transformers · NLP · Python · FastAPI</text>
</svg>

    </td>
  </tr>
</table>

<br>
</details>

<br>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- QUANTUM DIVIDER                                                          -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<svg viewBox="0 0 1000 80" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="quantum-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0"/>
      <stop offset="25%" stop-color="#8b5cf6" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.3"/>
      <stop offset="75%" stop-color="#8b5cf6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0"/>
    </linearGradient>
    <style>
      @keyframes quantum-pulse { 0%,100%{ opacity:0.3; r:3 } 50%{ opacity:1; r:6 } }
      .q-node { animation: quantum-pulse 3s ease-in-out infinite }
      .q-node-2 { animation: quantum-pulse 3.5s ease-in-out infinite; animation-delay:0.7s }
      .q-node-3 { animation: quantum-pulse 2.8s ease-in-out infinite; animation-delay:1.2s }
    </style>
  </defs>
  <rect x="0" y="0" width="1000" height="80" fill="#05080f" opacity="0.3"/>
  <path d="M0,40 Q100,20 200,40 T400,40 T600,40 T800,40 T1000,40" fill="none" stroke="url(#quantum-grad)" stroke-width="1" opacity="0.3"/>
  <path d="M0,50 Q100,30 200,50 T400,50 T600,50 T800,50 T1000,50" fill="none" stroke="#8b5cf6" stroke-width="0.5" opacity="0.15"/>
  <g>
    <circle cx="100" cy="30" r="3" fill="#8b5cf6" class="q-node"/>
    <circle cx="300" cy="25" r="2.5" fill="#3b82f6" class="q-node-2"/>
    <circle cx="500" cy="35" r="3" fill="#8b5cf6" class="q-node-3"/>
    <circle cx="700" cy="20" r="2.5" fill="#3b82f6" class="q-node-2"/>
    <circle cx="900" cy="30" r="3" fill="#8b5cf6" class="q-node"/>
  </g>
  <text x="500" y="68" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280" opacity="0.5" letter-spacing="4">SYSTEM METRICS  //  ANALYTICS DASHBOARD</text>
</svg>

<br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- SECTION 4 :: ANALYTICS COMMAND CENTER                                    -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="12" width="400" height="2" fill="#8b5cf6" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#8b5cf6" letter-spacing="6">⏣ ANALYTICS COMMAND CENTER</text>
  <rect x="0" y="14" width="400" height="2" fill="#8b5cf6" opacity="0.15"/>
</svg>

<br>

<!-- Metrics Dashboard -->
<svg viewBox="0 0 860 72" width="860" height="72" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="6" width="200" height="60" rx="4" fill="#00d4ff05" stroke="#00d4ff" stroke-width="0.5" opacity="0.5"/>
  <text x="110" y="28" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">TOTAL CONTRIBUTIONS</text>
  <text x="110" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="20" fill="#00d4ff" font-weight="bold">2,340+</text>
  <rect x="220" y="6" width="200" height="60" rx="4" fill="#a855f705" stroke="#a855f7" stroke-width="0.5" opacity="0.5"/>
  <text x="320" y="28" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">ACTIVE REPOSITORIES</text>
  <text x="320" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="20" fill="#a855f7" font-weight="bold">32</text>
  <rect x="430" y="6" width="200" height="60" rx="4" fill="#4a9eff05" stroke="#4a9eff" stroke-width="0.5" opacity="0.5"/>
  <text x="530" y="28" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">PATENTS FILED</text>
  <text x="530" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="20" fill="#4a9eff" font-weight="bold">1</text>
  <rect x="640" y="6" width="210" height="60" rx="4" fill="#10b98105" stroke="#10b981" stroke-width="0.5" opacity="0.5"/>
  <text x="745" y="28" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#6b7280">HACKATHON WINS</text>
  <text x="745" y="54" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="20" fill="#10b981" font-weight="bold">1</text>
</svg>

<br><br>

<img src="https://github-readme-stats.vercel.app/api?username=prnvvv&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=0a0a0f&title_color=00d4ff&icon_color=4a9eff&text_color=8b949e&ring_color=00d4ff&border_radius=6&locale=en" height="170"/>
&nbsp;&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs?username=prnvvv&layout=compact&langs_count=8&hide_border=true&bg_color=0a0a0f&title_color=00d4ff&text_color=8b949e&border_radius=6" height="170"/>

<br><br>

<img src="https://streak-stats.demolab.com/?user=prnvvv&hide_border=true&background=0a0a0f&ring=00d4ff&fire=4a9eff&currStreakLabel=00d4ff&sideLabels=8b949e&dates=4a4a6a&stroke=1a1a2e&border_radius=6"/>

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=prnvvv&bg_color=0a0a0f&color=00d4ff&line=00d4ff&point=ffffff&area=true&area_color=00d4ff15&hide_border=true&custom_title=COMMIT%20FREQUENCY%20/%20CONTRIBUTION%20HEATMAP&radius=6"/>

<br><br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- CONTRIBUTION SNAKE                                                       -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="12" width="400" height="2" fill="#10b981" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#10b981" letter-spacing="6">⏣ CONTRIBUTION MAP</text>
  <rect x="0" y="14" width="400" height="2" fill="#10b981" opacity="0.15"/>
</svg>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/prnvvv/prnvvv/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/prnvvv/prnvvv/output/github-snake.svg" />
  <img alt="Contribution grid snake animation" src="https://raw.githubusercontent.com/prnvvv/prnvvv/output/github-snake.svg" />
</picture>

<br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- RECOGNITION LOG                                                          -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="12" width="400" height="2" fill="#f59e0b" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b" letter-spacing="6">⏣ RECOGNITION LOG</text>
  <rect x="0" y="14" width="400" height="2" fill="#f59e0b" opacity="0.15"/>
</svg>

<br>

<svg viewBox="0 0 700 215" width="700" height="215" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="700" height="215" rx="6" fill="#0a0a0f" stroke="#f59e0b" stroke-width="0.5" opacity="0.5"/>
  <rect x="0" y="0" width="700" height="28" rx="6" fill="#f59e0b06"/>
  <text x="350" y="19" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="10" fill="#f59e0b" letter-spacing="3">◆ ACHIEVEMENT UNLOCKED ◆</text>
  <g transform="translate(0, 40)">
    <text x="30" y="12" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b">01</text>
    <text x="60" y="12" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">HackHub'25 Winner</text>
    <text x="300" y="12" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">IEEE &amp; GitHub Hackathon</text>
    <rect x="580" y="2" width="90" height="14" rx="3" fill="#f59e0b12"/>
    <text x="625" y="13" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#f59e0b">COMPETITION</text>
  </g>
  <line x1="30" y1="68" x2="670" y2="68" stroke="#1f2937" stroke-width="0.5"/>
  <g transform="translate(0, 75)">
    <text x="30" y="12" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b">02</text>
    <text x="60" y="12" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Patent Published</text>
    <text x="300" y="12" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">CropCore AI Farming System</text>
    <rect x="580" y="2" width="90" height="14" rx="3" fill="#a855f712"/>
    <text x="625" y="13" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#a855f7">PATENT</text>
  </g>
  <line x1="30" y1="103" x2="670" y2="103" stroke="#1f2937" stroke-width="0.5"/>
  <g transform="translate(0, 110)">
    <text x="30" y="12" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b">03</text>
    <text x="60" y="12" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Research Intern</text>
    <text x="300" y="12" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">IIT Ropar · Agricultural ML</text>
    <rect x="580" y="2" width="90" height="14" rx="3" fill="#00d4ff12"/>
    <text x="625" y="13" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#00d4ff">RESEARCH</text>
  </g>
  <line x1="30" y1="138" x2="670" y2="138" stroke="#1f2937" stroke-width="0.5"/>
  <g transform="translate(0, 145)">
    <text x="30" y="12" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b">04</text>
    <text x="60" y="12" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">Chairperson</text>
    <text x="300" y="12" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">OSPC · VIT Chennai</text>
    <rect x="580" y="2" width="90" height="14" rx="3" fill="#10b98112"/>
    <text x="625" y="13" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#10b981">LEADERSHIP</text>
  </g>
  <line x1="30" y1="173" x2="670" y2="173" stroke="#1f2937" stroke-width="0.5"/>
  <g transform="translate(0, 180)">
    <text x="30" y="12" font-family="'Courier New',Courier,monospace" font-size="12" fill="#f59e0b">05</text>
    <text x="60" y="12" font-family="'Courier New',Courier,monospace" font-size="10" fill="#e2e8f0">State Athlete</text>
    <text x="300" y="12" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">TNCA Cricket · U-14 &amp; U-16</text>
    <rect x="580" y="2" width="90" height="14" rx="3" fill="#f59e0b12"/>
    <text x="625" y="13" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#f59e0b">ATHLETICS</text>
  </g>
</svg>

<br><br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- SECTION 5 :: CONTACT GATEWAY                                             -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
<br>

<svg viewBox="0 0 400 28" width="400" height="28" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="12" width="400" height="2" fill="#00d4ff" opacity="0.15"/>
  <text x="200" y="20" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="12" fill="#00d4ff" letter-spacing="6">⏣ CONTACT GATEWAY</text>
  <rect x="0" y="14" width="400" height="2" fill="#00d4ff" opacity="0.15"/>
</svg>

<br>

<svg viewBox="0 0 600 110" width="600" height="110" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes cont-blink { 0%,100%{ opacity:1 } 50%{ opacity:0 } }
    .cont-caret { animation: cont-blink 1s step-end infinite }
  </style>
  <rect x="0" y="0" width="600" height="110" rx="6" fill="#0a0a0f" stroke="#00d4ff" stroke-width="0.5" opacity="0.5"/>
  <rect x="0" y="0" width="600" height="24" rx="6" fill="#00d4ff06"/>
  <circle cx="14" cy="12" r="3" fill="#ef4444" opacity="0.8"/>
  <circle cx="26" cy="12" r="3" fill="#f59e0b" opacity="0.8"/>
  <circle cx="38" cy="12" r="3" fill="#10b981" opacity="0.8"/>
  <text x="300" y="16" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280">CONTACT — GATEWAY.TERM</text>
  <text x="20" y="48" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff">$</text>
  <text x="36" y="48" font-family="'Courier New',Courier,monospace" font-size="11" fill="#8b949e">./connect.sh --purpose collaboration</text>
  <text x="20" y="72" font-family="'Courier New',Courier,monospace" font-size="11" fill="#6b7280">OPEN TO:  Research Collaborations · AI/ML Engineering · Open Source</text>
  <text x="20" y="96" font-family="'Courier New',Courier,monospace" font-size="11" fill="#4a9eff">▸</text>
  <text x="36" y="96" font-family="'Courier New',Courier,monospace" font-size="11" fill="#8b949e">Ready to receive transmissions</text>
  <text x="280" y="96" font-family="'Courier New',Courier,monospace" font-size="11" fill="#10b981">█</text>
  <text class="cont-caret" x="288" y="96" font-family="'Courier New',Courier,monospace" font-size="11" fill="#00d4ff">▌</text>
</svg>

<br><br>

<a href="mailto:prannavakhanth12@gmail.com">
  <img src="https://img.shields.io/badge/INITIATE_CONTACT-prannavakhanth12@gmail.com-0a0a0f?style=for-the-badge&logo=gmail&logoColor=00d4ff&labelColor=0a1628&color=0d1117" alt="Email"/>
</a>&nbsp;
<a href="https://www.linkedin.com/in/prannavakhanth-a-59b98228a/">
  <img src="https://img.shields.io/badge/LINKEDIN_CONNECT-Prannavakhanth_A-0a0a0f?style=for-the-badge&logo=linkedin&logoColor=4a9eff&labelColor=0a1628&color=0d1117" alt="LinkedIn"/>
</a>

<br><br>

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- FOOTER — NEURAL NETWORK WAVE                                             -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<svg viewBox="0 0 1000 120" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footer-wave" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.15"/>
      <stop offset="30%" stop-color="#4a9eff" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="#a855f7" stop-opacity="0.12"/>
      <stop offset="70%" stop-color="#4a9eff" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0.15"/>
    </linearGradient>
    <style>
      @keyframes footer-pulse { 0%,100%{ opacity:0.15 } 50%{ opacity:0.35 } }
      @keyframes footer-glow { 0%,100%{ opacity:0.08 } 50%{ opacity:0.2 } }
      @keyframes footer-float { 0%,100%{ transform:translateY(0) } 50%{ transform:translateY(-8px) } }
      @keyframes footer-drift { 0%,100%{ transform:translateX(0) } 50%{ transform:translateX(15px) } }
      .f-wave { animation: footer-pulse 4s ease-in-out infinite }
      .f-glow { animation: footer-glow 3s ease-in-out infinite }
      .f-float { animation: footer-float 5s ease-in-out infinite }
      .f-drift { animation: footer-drift 7s ease-in-out infinite }
    </style>
  </defs>
  <rect x="0" y="0" width="1000" height="120" fill="#05080f" opacity="0.8"/>
  <rect x="0" y="0" width="1000" height="2" fill="url(#footer-wave)" class="f-glow"/>
  <g opacity="0.15">
    <path d="M0,80 Q100,40 200,60 T400,40 T600,60 T800,40 T1000,60" fill="none" stroke="#00d4ff" stroke-width="1" class="f-wave"/>
    <path d="M0,90 Q100,60 200,80 T400,55 T600,75 T800,50 T1000,70" fill="none" stroke="#4a9eff" stroke-width="0.8" class="f-wave" style="animation-delay:1s"/>
    <path d="M0,100 Q100,75 200,90 T400,70 T600,85 T800,65 T1000,80" fill="none" stroke="#a855f7" stroke-width="0.6" class="f-wave" style="animation-delay:2s"/>
  </g>
  <g>
    <circle cx="150" cy="60" r="3" fill="#00d4ff" opacity="0.3" class="f-float"/>
    <circle cx="350" cy="50" r="2.5" fill="#4a9eff" opacity="0.25" class="f-drift"/>
    <circle cx="500" cy="65" r="3.5" fill="#a855f7" opacity="0.3" class="f-float" style="animation-delay:0.5s"/>
    <circle cx="650" cy="45" r="2.5" fill="#00d4ff" opacity="0.25" class="f-drift" style="animation-delay:1s"/>
    <circle cx="850" cy="55" r="3" fill="#4a9eff" opacity="0.3" class="f-float" style="animation-delay:1.5s"/>
  </g>
  <text x="500" y="38" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="9" fill="#6b7280" opacity="0.6" letter-spacing="2">prnvvv / Prannavakhanth A</text>
  <text x="500" y="55" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="8" fill="#4a9eff" opacity="0.4" letter-spacing="3">AI ENGINEERING PORTFOLIO</text>
  <g transform="translate(460, 82)" opacity="0.2">
    <rect x="0" y="-10" width="3" height="10" fill="#00d4ff">
      <animate attributeName="height" values="10;20;10" dur="1s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-10;-20;-10" dur="1s" repeatCount="indefinite"/>
    </rect>
    <rect x="7" y="-15" width="3" height="15" fill="#4a9eff">
      <animate attributeName="height" values="15;8;15" dur="1.2s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-15;-8;-15" dur="1.2s" repeatCount="indefinite"/>
    </rect>
    <rect x="14" y="-12" width="3" height="12" fill="#a855f7">
      <animate attributeName="height" values="12;18;12" dur="0.8s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-12;-18;-12" dur="0.8s" repeatCount="indefinite"/>
    </rect>
    <rect x="21" y="-8" width="3" height="8" fill="#4a9eff">
      <animate attributeName="height" values="8;14;8" dur="1.1s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-8;-14;-8" dur="1.1s" repeatCount="indefinite"/>
    </rect>
    <rect x="28" y="-14" width="3" height="14" fill="#00d4ff">
      <animate attributeName="height" values="14;7;14" dur="0.9s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-14;-7;-14" dur="0.9s" repeatCount="indefinite"/>
    </rect>
    <rect x="35" y="-10" width="3" height="10" fill="#a855f7">
      <animate attributeName="height" values="10;16;10" dur="1.3s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-10;-16;-10" dur="1.3s" repeatCount="indefinite"/>
    </rect>
    <rect x="42" y="-6" width="3" height="6" fill="#4a9eff">
      <animate attributeName="height" values="6;12;6" dur="0.7s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-6;-12;-6" dur="0.7s" repeatCount="indefinite"/>
    </rect>
    <rect x="49" y="-12" width="3" height="12" fill="#00d4ff">
      <animate attributeName="height" values="12;9;12" dur="1s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-12;-9;-12" dur="1s" repeatCount="indefinite"/>
    </rect>
    <rect x="56" y="-9" width="3" height="9" fill="#a855f7">
      <animate attributeName="height" values="9;15;9" dur="0.9s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-9;-15;-9" dur="0.9s" repeatCount="indefinite"/>
    </rect>
    <rect x="63" y="-11" width="3" height="11" fill="#4a9eff">
      <animate attributeName="height" values="11;6;11" dur="1.1s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-11;-6;-11" dur="1.1s" repeatCount="indefinite"/>
    </rect>
    <rect x="70" y="-14" width="3" height="14" fill="#00d4ff">
      <animate attributeName="height" values="14;20;14" dur="0.8s" repeatCount="indefinite"/>
      <animate attributeName="y" values="-14;-20;-14" dur="0.8s" repeatCount="indefinite"/>
    </rect>
  </g>
  <text x="500" y="113" text-anchor="middle" font-family="'Courier New',Courier,monospace" font-size="7" fill="#4a9eff" opacity="0.25" letter-spacing="6">◆ END TRANSMISSION ◆</text>
</svg>

</div>