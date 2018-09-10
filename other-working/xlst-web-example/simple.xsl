<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/breakfast_menu">
<html>
<head>
</head>
<body>
<xsl:for-each select="food">
 <h1> <xsl:value-of select="name"/></h1>
 <h2> <xsl:value-of select="price"/></h2>
 <h2> <xsl:value-of select="description"/></h2>
 <h2> <xsl:value-of select="calories"/></h2>
 </xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>