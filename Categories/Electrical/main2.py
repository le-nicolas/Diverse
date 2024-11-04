import numpy as np
import matplotlib.pyplot as plt

# Define modulation schemes and coding rates
modulation_schemes = ['BPSK', 'QPSK', '16-QAM', '64-QAM']
coding_rates = [0.5, 0.75, 0.9]  # Fraction of data bits to total bits

# Define thresholds for SNR to switch modulation schemes
snr_thresholds = [5, 10, 20]  # SNR in dB to switch modulation

# Simulate random SNR variations over time
time = np.arange(0, 100)
snr_values = np.random.normal(15, 5, size=time.shape)  # Mean SNR = 15 dB, with some variation

# Function to choose modulation based on SNR
def choose_modulation(snr):
    if snr < snr_thresholds[0]:
        return modulation_schemes[0], coding_rates[0]  # BPSK, robust for low SNR
    elif snr < snr_thresholds[1]:
        return modulation_schemes[1], coding_rates[1]  # QPSK
    elif snr < snr_thresholds[2]:
        return modulation_schemes[2], coding_rates[2]  # 16-QAM
    else:
        return modulation_schemes[3], coding_rates[2]  # 64-QAM, high throughput for high SNR

# Simulate modulation and coding choices based on SNR over time
modulation_choices = []
coding_rate_choices = []
throughput = []

for snr in snr_values:
    modulation, coding_rate = choose_modulation(snr)
    modulation_choices.append(modulation)
    coding_rate_choices.append(coding_rate)
    
    # Assuming higher modulation schemes provide more throughput
    if modulation == 'BPSK':
        throughput.append(1 * coding_rate)  # Low throughput for BPSK
    elif modulation == 'QPSK':
        throughput.append(2 * coding_rate)
    elif modulation == '16-QAM':
        throughput.append(4 * coding_rate)
    elif modulation == '64-QAM':
        throughput.append(6 * coding_rate)

# Plot the SNR and modulation scheme over time
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(time, snr_values, label="SNR (dB)")
ax1.axhline(snr_thresholds[0], color='r', linestyle='--', label=f'SNR {snr_thresholds[0]} dB')
ax1.axhline(snr_thresholds[1], color='g', linestyle='--', label=f'SNR {snr_thresholds[1]} dB')
ax1.axhline(snr_thresholds[2], color='b', linestyle='--', label=f'SNR {snr_thresholds[2]} dB')
ax1.set_title("SNR Variations Over Time")
ax1.set_ylabel("SNR (dB)")
ax1.legend()
ax1.grid(True)

# Plot modulation scheme selections
ax2.plot(time, throughput, label="Throughput (units)", color='purple')
ax2.set_title("Throughput Based on Modulation & Coding Rate")
ax2.set_ylabel("Throughput")
ax2.set_xlabel("Time")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
