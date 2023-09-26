import obspy
import sys
# Read in the data

file_name = sys.argv[1]

def plot_saving(file_name):
	WFs = obspy.read(f'data/{file_name}')
	#plotting the data
	new_ST = obspy.Stream()
	for wf in WFs:
			wf.stats.distance = int(str(wf.stats.seg2['RECEIVER_LOCATION']).split('.')[0])
			new_ST += wf
	new_ST.plot(type='section', orientation='horizontal', recordlength=0.1, scale=4, fillcolors=('red', 'blue'), linewidth=0.25, grid_linewidth=0.25, show=False, outfile=file_name.split('.')[0] + '.png')


plot_saving(file_name)
