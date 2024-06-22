def make_mask(ds, poly, crs):
    '''
    Function to make a mask from a dataset and a polygon.
    '''
    import xarray as xr
    import rioxarray
    import numpy as np
    from shapely.geometry import mapping
    
    mask = xr.DataArray(
                data = np.ones((ds.sizes['y'], ds.sizes['x'])),
                dims = {'y':ds.dims['y'], 'x':ds.dims['x']},
                coords = {'y':ds['y'], 'x':ds['x'],},
                attrs = ds.attrs
    )
    
    mask.name = 'mask'
    
    # Make sure the mask and polygon have the same crs
    poly = poly.to_crs(crs)
    mask = mask.rio.write_crs(crs)
    
    # Clip the mask using the polygon
    mask = mask.rio.clip(poly.geometry.apply(mapping), poly.crs, drop=False)
    
    # Set all masked values to nan and all non-masked values to 1
    mask = mask.where(mask != -999, np.nan)
    mask = mask.where(mask.isnull(), 1)
    
    return mask

##############################################################################

def remove_labels_ticks(ax):
    '''
    Remove axis labels and ticks from subplots.
    '''
    ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
    ax.set_xlabel('')
    ax.set_ylabel('')