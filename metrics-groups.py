
prefix = '@GRP'

font = CurrentFont()

for groupname, content in font.groups.items():
	if groupname.startswith(prefix):
		baseglyph = content[0]
		leftright_id = groupname.split('_')[1]  # @GRP_L/R_name
		for glyphname in content[1:]:
			if leftright_id == 'L':
				font[glyphname].leftMargin = font[baseglyph].leftMargin
			if leftright_id == 'R':
				font[glyphname].rightMargin = font[baseglyph].rightMargin

