#

"""
@author:˶marduk191
@title: marduk191 workflow settings
@nickname: marduk191 workflow settings
@version: "1.0"
@project: "marnodes",
@description: A node to set workflow settings.
"""

import comfy.samplers

class marselect:
    
    # dimensions sourced from: https://arxiv.org/abs/2307.01952
    # & https://github.com/Stability-AI/generative-models
    RATIO = [
        ("1:1___SD 512x512", 512, 512),
        ("4:3___SD 682x512", 682, 512),
        ("3:2___SD 768x512", 768, 512),
        ("16:9__SD 910x512", 910, 512),
        ("1:85:1 SD 952x512", 952, 512),
        ("2:1___SD 1024x512", 1024, 512),
        ("1:1_SV3D 576x576", 576, 576),
        ("16:9_SVD 576x1024", 1024, 576),
        ("1:1__SD2 768x768", 768, 768),
        ("1:1___XL 1024x1024", 1024, 1024),
        ("16:15_XL 1024x960", 1024, 960),
        ("17:15_XL 1088x960", 1088, 960),
        ("17:14_XL 1088x896", 1088, 896),
        ("4:3___XL 1152x896", 1152, 896),
        ("18:13_XL 1152x832", 1152, 832),
        ("3:2___XL 1216x832", 1216, 832),
        ("5:3___XL 1280x768", 1280, 768),
        ("7:4___XL 1344x768", 1344, 768),
        ("21:11_XL 1344x704", 1344, 704),
        ("2:1___XL 1408x704", 1408, 704),
        ("23:11_XL 1472x704", 1472, 704),
        ("21:9__XL 1536x640", 1536, 640),
        ("5:2___XL 1600x640", 1600, 640),
        ("26:9__XL 1664x576", 1664, 576),
        ("3:1___XL 1728x576", 1728, 576),
        ("28:9__XL 1792x576", 1792, 576),
        ("29:8__XL 1856x512", 1856, 512),
        ("15:4__XL 1920x512", 1920, 512),
        ("31:8__XL 1984x512", 1984, 512),
        ("4:1___XL 2048x512", 2048, 512),
    ]

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratio_titles = [title for title, res1, res2 in cls.RATIO]
        rotation = ("landscape", "portrait")
        
        return {
            "required": {
                "Aspect_Ratio": (aspect_ratio_titles,
                    {"default": ("1:1___XL 1024x1024")}),
                "rotation": (rotation,),
            },
            "optional": {
                "batch": ("INT", {
                         "default": 1,
                         "min": 1, 
                         "max": 10000,
                 }),
                "Pass_1_steps": ("INT", {
                         "default": 25, 
                         "min": 1, 
                         "max": 10000,
                 }),
                "Pass_2_steps": ("INT", {
                         "default": 25, 
                         "min": 1, 
                         "max": 10000,
                 }),
                "Pass_1_CFG": ("FLOAT",{
                         "default": 6.0,
                         "min": -10.0,
                         "max": 100.0,
                         "step": 0.1,
                         "round": 0.1,
                }),
                "Pass_2_CFG": ("FLOAT", {
                        "default": 6.0,
                        "min": -10.0,
                        "max": 100.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
                "Pass_2_denoise": ("FLOAT", {
                        "default": 0.500,
                        "min": -10.000,
                        "max": 100.000,
                        "step": 0.001,
                        "round": 0.01,
                 }),
                "scale_factor": ("FLOAT", {
                        "default": 1.5,
                        "min": 1.0,
                        "max": 10.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
                "sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,)
            }
        }   
    RETURN_TYPES = (
        "INT", "INT", "INT", "INT", "INT", "FLOAT",
        "FLOAT", "FLOAT", "FLOAT",comfy.samplers.KSampler.SAMPLERS,
        comfy.samplers.KSampler.SCHEDULERS,)
        
    RETURN_NAMES = (
        "WIDTH",
        "HEIGHT",
        "BATCH_SIZE",
        "Pass_1_steps",
        "Pass_2_steps",
        "Pass_1_CFG",
        "Pass_2_CFG",
        "Pass_2_denoise",
        "SCALE",
        "SAMPLER",
        "SCHEDULER",
    )
    FUNCTION = "marselect"
    CATEGORY = "marduk191/settings"

    def marselect(self, Aspect_Ratio, rotation, batch, Pass_1_steps, Pass_2_steps, Pass_1_CFG, Pass_2_CFG, Pass_2_denoise, scale_factor, sampler, scheduler):
        for title, width, height in self.RATIO:
            if title == Aspect_Ratio:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (width, height, batch, Pass_1_steps, Pass_2_steps, Pass_1_CFG, Pass_2_CFG, Pass_2_denoise, scale_factor, sampler, scheduler)
        return (None, None, batch, Pass_1_steps, Pass_2_steps, Pass_1_CFG, Pass_2_CFG, Pass_2_denoise, scale_factor, sampler, scheduler)  # In case the Aspect Ratio is not found

class tswitch:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 5}),
            },
            "optional": {
                "text1": ("STRING", {"forceInput": True}),
                "text2": ("STRING", {"forceInput": True}),
                "text3": ("STRING", {"forceInput": True}),
                "text4": ("STRING", {"forceInput": True}),  
                "text5": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("STRING", )
    FUNCTION = "tswitch"
    CATEGORY = "marduk191/text"

    def tswitch(self, Input, text1=None, text2=None, text3=None, text4=None, text5=None):
        if Input == 1:
            return (text1, )
        elif Input == 2:
            return (text2, )
        elif Input == 3:
            return (text3, )
        elif Input == 4:
            return (text4, )
        else:
            return (text5, )  
            
class tstring:
 
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": '', "multiline": False}),
            },
            "optional": {
                "text_b": ("STRING", {"default": '', "multiline": False}),
                "text_c": ("STRING", {"default": '', "multiline": False}),
                "text_d": ("STRING", {"default": '', "multiline": False}),
                "text_e": ("STRING", {"default": '', "multiline": False}),
            }
        }
    RETURN_TYPES = ("STRING","STRING","STRING","STRING","STRING", )
    RETURN_NAMES = ("STRING1","STRING2","STRING3","STRING4","STRING5", )
    FUNCTION = "tstring"
    CATEGORY = "marduk191/text"

    def tstring(self, text='', text_b='', text_c='', text_d='', text_e=''):

      return (text, text_b, text_c, text_d, text_e)
          
            
NODE_CLASS_MAPPINGS = { 
    "marduk191_workflow_settings": marselect, 
    "marduk191_5way_text_switch": tswitch, 
    "marduk191_5_text_string": tstring,
 }
NODE_DISPLAY_NAME_MAPPINGS = { 
    "marduk191_workflow_settings": "marduk191 workflow settings", 
    "marduk191_5way_text_switch": "marduk191's 5 way text switch", 
    "marduk191_5_text_string": "marduk191's 5 text strings",
 }