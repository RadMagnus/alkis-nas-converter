from osgeo import gdal

def convert(input_file, output_file, format_name, source_crs):
    """
    Converts an ALKIS file in NAS format to your geospatial file format of choice.
    Recommended is file format GeoPackage (GPKG)
    Args:
        input_file (str): filepath of the NAS-ALKIS file
        output_file (str): filepath of the converted file
        format_name (str): output_file format, recommended: "GPKG"
        source_crs (str): CRS of ALKIS file in "EPSG:25832" notation
    """
    gdal.VectorTranslate(
        output_file,
        input_file,
        options= f"-f {format_name} -a_srs {source_crs}",
        )
    
def main():
    input_file = "alkis_file.xml"  
    output_file = "alkis_file.gpkg"
    format_name = "GPKG"
    source_crs = "EPSG:25832"

    convert(input_file, output_file, format_name, source_crs)