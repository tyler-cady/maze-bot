import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

if self.plot_mode == PlotOption.Spectrogram:
    spectr_data, spectr_extent = Processing.calcSpectrogram(packet)
    
    # Clear the current axes
    ax = Fig_h.get_axes()[2]
    ax.cla()
    
    # Plot the spectrogram with updated data and properties
    im = ax.imshow(spectr_data, cmap='magma', origin='lower', aspect='auto', extent=spectr_extent)
    
    # Normalize the colormap based on the new data range
    norm = mcolors.Normalize(vmin=spectr_data.min(), vmax=spectr_data.max())
    
    # Get the existing colorbar if it exists
    cbar_exists = False
    for child in ax.get_children():
        if isinstance(child, plt.colorbar):
            cbar = child
            cbar_exists = True
            break
    
    if not cbar_exists:
        # Add a colorbar to the spectrogram
        cbar = Fig_h.colorbar(cm.ScalarMappable(norm=norm, cmap='magma'), ax=ax)
    
    # Update the colorbar with the new normalization
    cbar.mappable.set_norm(norm)
    
    # Optionally, set a label for the colorbar
    cbar.set_label('Intensity')
    
    # Optionally, adjust the ticks or other properties of the colorbar if needed
    
    # Ensure the plot is updated
    plt.draw()