
NAME = "Image Background Remove Tool"
MODELS_NAMES = ["u2netp", "xception_model"]
PREPROCESS_METHODS = ["bbd-fastrcnn", "bbmd-maskrcnn", "None"]
POSTPROCESS_METHODS = ["rtb-bnb", "rtb-bnb2", "No"]
DESCRIPTION = "A tool to remove a background from image using Neural Networks"
LICENSE = "Apache License 2.0"
ARGS_HELP = """
{}
{}
License: {}
Running the script:
python3 main.py -i <input_path> -o <output_path> -m <model_type> -prep <preprocessing_method> -postp <postprocessing_method>
Explanation of args:
-i <input_path> - path to input file or dir.
-o <output_path> - path to output file or dir.
-prep <preprocessing_method> - Preprocessing method. Can be {} . `bbd-fastrcnn` is better to use.
-postp <postprocessing_method> - Postprocessing method. Can be {} . `rtb-bnb` is better to use.
-m <model_type> - can be {}. u2net is better to use. 
DeepLab models (xception_model or mobile_net_model) are outdated 
and designed to remove the background from PORTRAIT photos or PHOTOS WITH ANIMALS! 
""".format(NAME, DESCRIPTION, LICENSE,
           ' or '.join(MODELS_NAMES),
           ' or '.join(PREPROCESS_METHODS),
           ' or '.join(POSTPROCESS_METHODS))
