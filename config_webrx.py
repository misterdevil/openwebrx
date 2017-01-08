# -*- coding: utf-8 -*-

"""
config_webrx: configuration options for OpenWebRX

	This file is part of OpenWebRX,
	an open-source SDR receiver software with a web UI.
	Copyright (c) 2013-2015 by Andras Retzler <randras@sdr.hu>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	In addition, as a special exception, the copyright holders
	state that config_rtl.py and config_webrx.py are not part of the
	Corresponding Source defined in GNU AGPL version 3 section 1.

	(It means that you do not have to redistribute config_rtl.py and
	config_webrx.py if you make any changes to these two configuration files,
	and use them for running your web service with OpenWebRX.)
"""

# NOTE: you can find additional information about configuring OpenWebRX in the Wiki:
#       https://github.com/simonyiszk/openwebrx/wiki

# ==== Server settings ====
web_port=8078
server_hostname="localhost"
 # If this contains an incorrect value, the web UI may freeze on load (it can't open websocket)
max_clients=5

# ==== Web GUI configuration ====
receiver_name="Mister Digital"
receiver_location="Bandung, indonesia"
receiver_qra="JN97ML"
receiver_asl=200
receiver_ant="Longwire"
receiver_device="RTL-SDR 820T2"
receiver_admin="dimaspramudyanto94@gmail.com"
receiver_gps=(47.000000,19.000000)
photo_height=350
photo_title=""
photo_desc="""
You can add your own background photo and receiver information.<br />
Receiver is operated by: <a href="mailto:%[RX_ADMIN]">%[RX_ADMIN]</a><br/>
Device: %[RX_DEVICE]<br />
Antenna: %[RX_ANT]<br />
Website: <a href="http://localhost" target="_blank">http://localhost</a>
"""

# ==== sdr.hu listing ====
# If you want your ham receiver to be listed publicly on sdr.hu, then take the following steps:
# 1. Register at: http://sdr.hu/register
# 2. You will get an unique key by email. Copy it and paste here:
sdrhu_key = "56f3a3f2d5a5eda10e87cb1ec224a"
# 3. Set this setting to True to enable listing:
sdrhu_public_listing = False

# ==== DSP/RX settings ====
dsp_plugin="csdr"
fft_fps=5
fft_size=8192
fft_voverlap_factor=0.3 #If it is above 0, multiple FFTs will be used for creating a line on the diagram.
samp_rate = 2400000 #default tidak bisa diganti saat ini 
center_freq = 89700000
rf_gain = 40 #in dB. For an RTL-SDR, rf_gain=0 will set the tuner to auto gain mode, else it will be in manual gain mode.
ppm = 0

audio_compression="adpcm" #valid values: "adpcm", "none"
fft_compression="adpcm" #valid values: "adpcm", "none"

start_rtl_thread=True

start_rtl_command="rtl_sdr -s {samp_rate} -f {center_freq} -p {ppm} -g {rf_gain} -".format(rf_gain=rf_gain, center_freq=center_freq, samp_rate=samp_rate, ppm=ppm)
format_conversion="csdr convert_u8_f"


shown_center_freq = center_freq #you can change this if you use an upconverter

client_audio_buffer_size = 7
#increasing client_audio_buffer_size will:
# - also increase the latency
# - decrease the chance of audio underruns

start_freq = center_freq
start_mod = "wfm" #khusus wfm mode

iq_server_port = 4951 #TCP port for ncat to listen on. It will send I/Q data over its connections, for internal use in OpenWebRX. It is only accessible from the localhost by default.

#access_log = "~/openwebrx_access.log"

# ==== Color themes ====

#A guide is available to help you set these values: https://github.com/simonyiszk/openwebrx/wiki/Calibrating-waterfall-display-levels

### default theme by teejez:
waterfall_colors = "[0x00FFFFFF,0x000066FF,0x00FFCC00,0x0000CC00,0x00009933,0x00FF0000,0x00FF0000,0x00FF0000]"
waterfall_min_level = -88 #in dB
waterfall_max_level = -20
waterfall_auto_level_margin = (5, 40)


csdr_dynamic_bufsize = False # This allows you to change the buffering mode of csdr.
csdr_print_bufsizes = False  # This prints the buffer sizes used for csdr processes.
csdr_through = False # Setting this True will print out how much data is going into the DSP chains.


print "[openwebrx-config] Detecting external IP address..."
import urllib2
server_hostname=urllib2.urlopen("http://icanhazip.com").read()[:-1]
print "[openwebrx-config] External IP address detected:", server_hostname

