import obspy
import sys
# Read in the data

file_name = sys.argv[1]
try:
	filter_str = sys.argv[2]
	filtering_condition = True
except:
	filtering_condition = False


class FilterTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def filtering(stream, filter):
	fil_type = filter[0:2]
	fil_low = float(filter.split(",")[0][2:])
	if fil_type == 'bp':
		fil_high = float(filter.split(",")[1])
	else:
		fil_high = fil_low
		
	if fil_type == 'lp':
		stream.filter("lowpass", freq = fil_low)
	elif fil_type == 'hp':
		stream.filter("highpass", freq = fil_high) 
	elif fil_type == 'bp':
		stream.filter("bandpass", freqmin=fil_low, freqmax=fil_high)
	else:
		raise FilterTypeError("Your filter type should be one of 'lp', 'bp', or 'hp' followed by values; like 'bp1,3' or 'lp2.6'")
	
	return stream


def plot_saving(file_name):
	WFs = obspy.read(f'data/{file_name}')
	#plotting the data
	new_ST = obspy.Stream()
	for wf in WFs:
			wf.stats.distance = int(str(wf.stats.seg2['RECEIVER_LOCATION']).split('.')[0])
			new_ST += wf
	if filtering_condition == True:
		new_ST = filtering(new_ST, filter_str)
	new_ST.plot(type='section', orientation='horizontal', recordlength=0.1, scale=4, fillcolors=('red', 'blue'), linewidth=0.25, grid_linewidth=0.25, show=False, outfile=file_name.split('.')[0] + '.png')


plot_saving(file_name)
#print(f"fil type: {fil_type}\nfil low: {fil_low}\nfilter high: {fil_high}")
