
How to use format convert script?

First, open the mod's .ini file and check the format, if IB file's format is
DXGI_FORMAT_R16_UINT, you need to set dxgi_format = DXGI_FORMAT_R16_UINT,
if it is DXGI_FORMAT_R32_UINT, you need to set dxgi_format = DXGI_FORMAT_R32_UINT
 in reverse.ini

Second check .buf file's stride and set the correct suffix and stride for
every .buf file in ModReverse.py 's category_stride_dict:

Example:category_stride_dict = {"Position": 40, "Texcoord": 20, "Blend": 32}


Actually, you need to set every attribute in reverse.ini
here is a example:
```
element_list = POSITION,NORMAL,TANGENT,COLOR,TEXCOORD,TEXCOORD1,BLENDWEIGHT,BLENDINDICES
;dxgi_format = DXGI_FORMAT_R32_UINT
dxgi_format = DXGI_FORMAT_R16_UINT
reverse_mod_path = C:/Users/Administrator/Desktop/textureslightfishnets/
ib_category_list = Head,Body,Dress
vb_category_list = Position,Texcoord,Blend
mod_name = Kokomi
```

And if it's needed, set the correct format in vertex_attr.ini,normally
you won't need to set this,but sometimes need to do, for example: weapon mod.