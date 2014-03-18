from mojo.roboFont import *

list_of_fonts = AllFonts()

font_PTsans = list_of_fonts.getFontsByFamilyNameStyleName( 'PT Sans', 'Regular' )
font_MYfont = list_of_fonts.getFontsByFamilyNameStyleName( 'MY FONT NAME', 'Regular' )

def getUnicodeByNameGlyph(font, glyphname):
	return font[glyphname].unicode

def getNameGlyphByUnicode(font, ucode):
	dic = font.getCharacterMapping()
	return dic[ucode][0]

for glyphPT in font_PTsans:
	if len( glyphPT.components ) != 0:
		name_Of_New_Glyph = glyphPT.name
		font_MYfont.newGlyph( name_Of_New_Glyph )
		font_MYfont[name_Of_New_Glyph].width = 500
		for index, component in enumerate(glyphPT.components):
			PT_baseGlyph = component.baseGlyph
			PT_unicode_component = getUnicodeByNameGlyph( font_PTsans , PT_baseGlyph )
			if PT_unicode_component != None:
				MY_component_name = getNameGlyphByUnicode(font_MYfont, PT_unicode_component )
				xmin, ymin, xmax, ymin = glyphPT.box
				offsetX = (xmax - xmin)/2
				font_MYfont[name_Of_New_Glyph].appendComponent( MY_component_name )
				if index == 0:
					font_MYfont[name_Of_New_Glyph].leftMargin = font_MYfont[MY_component_name].leftMargin
					font_MYfont[name_Of_New_Glyph].rightMargin = font_MYfont[MY_component_name].rightMargin
				else:
					Xmove = (font_MYfont[name_Of_New_Glyph].width /2) -  offsetX + font_MYfont[name_Of_New_Glyph].leftMargin

					font_MYfont[name_Of_New_Glyph].components[index].move((Xmove,0))
		font_MYfont[name_Of_New_Glyph].mark = (0, 0.3, 0, 0.25)



