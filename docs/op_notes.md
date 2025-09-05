# Operational Notes – Short-Range SDR Field Deployment

## 1. Setup

- Ensure SDR hardware is properly calibrated before deployment.
- Confirm antenna alignment for intended frequency ranges (144–470 MHz).
- Power supply check: maintain stable 5V input to SDR module; voltage fluctuations may affect waveform fidelity.
- Connect to host laptop using USB 3.0 interface; confirm driver version >= 0.6.0.
- Verify Python environment: dependencies include `numpy`, `scipy`, `matplotlib`, `pyrtlsdr`.

## 2. Pre-Operation Configuration

- Load `sdr_config.yaml` with desired archetype frequencies.
- Confirm waveform generation parameters:
  - Sample rate: 48 kHz
  - Signal duration: 10–60 seconds per sweep

## 3. Signal Generation

- Execute `generate_waveform.py` specifying target archetype frequency:
`python src/generate_waveform.py --frequency 145.25 --output data/waveforms/shadow_waveform.wav`
- Validate waveform visually using `analyze_waveform.py`.
- Adjust amplitude and phase parameters to avoid clipping.
- For multi-frequency sweeps, use an automated pipeline script if available to sequence multiple waveforms.

## 4. Capture and Analysis

- Place SDR module in intended observation location; minimize interference from nearby electronics.
- Analyze waveform data using FFT plots:
`python src/analyze_waveform.py --input data/waveforms/shadow_waveform.wav`
- Compare observed spectrum to expected archetype frequency; adjust modulation if deviation >5%.

## 5. Logging and Documentation

- Maintain field logs in `docs/field_notes.md`.
- Record operator ID, location, timestamp, and environmental notes.
- Include screenshots of waveform plots and FFT spectra for archival.
- Annotate any anomalies or unexpected resonance phenomena.

## 6. Safety and Compliance

- All frequencies are experimental and synthetic; do not transmit on licensed RF bands. 
- Ensure SDR module is powered down when not in use.
- Avoid physical proximity to antennas during active sweeps (>1m recommended).
- Store sensitive config files in encrypted storage.

## 7. Maintenance

- Periodically clean antenna connectors and USB interfaces.
- Update Python dependencies as needed:
`pip install -r requirements.txt --upgrade`
- Backup operator logs after each session.
- Archive old waveform files in `data/` to prevent accidental reuse.

---

*End of Operational Notes – Short-Range SDR Deployment*
