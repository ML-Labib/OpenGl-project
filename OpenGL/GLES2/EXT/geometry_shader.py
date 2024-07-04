'''OpenGL extension EXT.geometry_shader

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.geometry_shader to provide a more 
Python-friendly API

Overview (from the spec)
	
	EXT_geometry_shader defines a new shader type available to be run on the
	GPU, called a geometry shader. Geometry shaders are run after vertices are
	transformed, but prior to color clamping, flatshading and clipping.
	
	A geometry shader begins with a single primitive (point, line,
	triangle). It can read the attributes of any of the vertices in the
	primitive and use them to generate new primitives. A geometry shader has a
	fixed output primitive type (point, line strip, or triangle strip) and
	emits vertices to define a new primitive. A geometry shader can emit
	multiple disconnected primitives. The primitives emitted by the geometry
	shader are clipped and then processed like an equivalent primitive
	specified by the application.
	
	Furthermore, EXT_geometry_shader provides four additional primitive
	types: lines with adjacency, line strips with adjacency, separate
	triangles with adjacency, and triangle strips with adjacency.  Some of the
	vertices specified in these new primitive types are not part of the
	ordinary primitives, instead they represent neighboring vertices that are
	adjacent to the two line segment end points (lines/strips) or the three
	triangle edges (triangles/tstrips). These vertices can be accessed by
	geometry shaders and used to match up the vertices emitted by the geometry
	shader with those of neighboring primitives.
	
	Since geometry shaders expect a specific input primitive type, an error
	will occur if the application presents primitives of a different type.
	For example, if a geometry shader expects points, an error will occur at
	drawing time if a primitive mode of TRIANGLES is specified.
	
	This extension also adds the notion of layered framebuffer attachments
	and framebuffers that can be used in conjunction with geometry shaders
	to allow programs to direct primitives to a face of a cube map or layer
	of a three-dimensional texture or two-dimensional array texture. The
	layer used for rendering can be selected by the geometry shader at run
	time. The framebuffer layer count present in GL 4.x and removed from
	ES 3.1 is restored.
	
	Not all geometry shader implementations have the ability to write the
	point size from a geometry shader. Thus a second extension string and
	shading language enable are provided for implementations which do
	support geometry shader point size.
	
	This extension relies on the EXT_shader_io_blocks extension to provide
	the required functionality for declaring input and output blocks and
	interfacing between shaders.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/geometry_shader.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.geometry_shader import *
from OpenGL.raw.GLES2.EXT.geometry_shader import _EXTENSION_NAME

def glInitGeometryShaderEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION