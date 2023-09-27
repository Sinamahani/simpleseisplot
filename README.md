# SimpleSeisPlot
![logo](https://github.com/Sinamahani/seis_simple_plot/blob/main/logo.png)

SimpleSeisPlot is a Python tool for plotting seismic waveforms from data files in familiar formats like seg2. This repository is designed to make it easy to visualize seismic data using Obspy, a powerful Python library for seismology.

## Requirements

Before you get started, make sure you have the following prerequisites installed:

- [Obspy](https://github.com/obspy/obspy): Obspy is a Python toolbox for seismology that provides many useful functionalities for working with seismic data.

## Getting Started

To use SimpleSeisPlot, follow these steps:

1. Clone this repository to your local machine.

```
git clone https://github.com/your-username/SimpleSeisPlot.git
```

2. Move your seismic data files into the "data" folder within the cloned repository.

3. Open your terminal or command prompt and navigate to the repository's directory.

```
cd SimpleSeisPlot
```

4. Run the `ssp.py` script with the name of your data file as an argument.

```
python3 main.py <file_name>
```

Replace `<file_name>` with the name of your seismic data file located in the "data" folder.

## Example

Here's an example of how to use SimpleSeisPlot:

```
python3 ssp.py example.seg2
```

This command will generate plots of the seismic waveforms from the `example.seg2` file located in the "data" folder.

## Contributing

If you would like to contribute to SimpleSeisPlot, feel free to open issues or pull requests. We welcome any contributions that can make this tool even better.

## Acknowledgments

- Thanks to the Obspy development team for providing a powerful library for working with seismic data.

Happy seismic waveform plotting with SimpleSeisPlot!
