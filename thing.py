import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

if self.plot_mode == PlotOption.Spectrogram:
    spectr_data, spectr_extent = Processing.calcSpectrogram(packet)
    ax = Fig_h.get_axes()[2]
    
    # Clear the current axes
    ax.cla()
    
    # Remove the existing colorbar if it exists
    if hasattr(ax, 'colorbar') and ax.colorbar:
        ax.colorbar.remove()
    
    # Plot the spectrogram
    im = ax.imshow(spectr_data, cmap='magma', origin='lower', aspect='auto', extent=spectr_extent)
    
    # Normalize the colormap
    norm = mcolors.Normalize(vmin=spectr_data.min(), vmax=spectr_data.max())
    
    # Add a new colorbar to the spectrogram
    cbar = Fig_h.colorbar(im, ax=ax, orientation='vertical')
    
    # Store the colorbar in the axes object
    ax.colorbar = cbar
    
    # Ensure the layout is adjusted properly
    plt.draw()