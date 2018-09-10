<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/channel">
<html>
<head>
</head>
<body>
<xsl:for-each select="item">
 <h1> <xsl:value-of select="link"/></h1>

 </xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>