#! /usr/bin/python

import plistlib
import collections
import sys

def main():
    args  = sys.argv
    
    lines = []
    path  = args[1]
    base  = plistlib.readPlist(path)
    bomb  = collections.defaultdict(lambda: 0)
    for k in base.keys():
        bomb[k] = base[k]
    lines.append("const char* dirname = \"%s\";" % path)
    lines.append("CCParticleSystemQuad::initWithTotalParticles(%s);" % bomb["maxParticles"])
    lines.append("m_fAngle = %s;" % bomb["angle"])
    lines.append("m_fAngleVar = %s;" % bomb["angleVariance"])
    lines.append("m_fDuration = %s;" % bomb["duration"])
    lines.append("m_tBlendFunc.src = %s;" % bomb["blendFuncSource"])
    lines.append("m_tBlendFunc.dst = %s;" % bomb["blendFuncDestination"])
    lines.append("m_tStartColor.r = %s;" % bomb["startColorRed"])
    lines.append("m_tStartColor.g = %s;" % bomb["startColorGreen"])
    lines.append("m_tStartColor.b = %s;" % bomb["startColorBlue"])
    lines.append("m_tStartColor.a = %s;" % bomb["startColorAlpha"])
    lines.append("m_tStartColorVar.r = %s;" % bomb["startColorVarianceRed"])
    lines.append("m_tStartColorVar.g = %s;" % bomb["startColorVarianceGreen"])
    lines.append("m_tStartColorVar.b = %s;" % bomb["startColorVarianceBlue"])
    lines.append("m_tStartColorVar.a = %s;" % bomb["startColorVarianceAlpha"])
    lines.append("m_tEndColor.r = %s;" % bomb["finishColorRed"])
    lines.append("m_tEndColor.g = %s;" % bomb["finishColorGreen"])
    lines.append("m_tEndColor.b = %s;" % bomb["finishColorBlue"])
    lines.append("m_tEndColor.a = %s;" % bomb["finishColorAlpha"])
    lines.append("m_tEndColorVar.r = %s;" % bomb["finishColorVarianceRed"])
    lines.append("m_tEndColorVar.g = %s;" % bomb["finishColorVarianceGreen"])
    lines.append("m_tEndColorVar.b = %s;" % bomb["finishColorVarianceBlue"])
    lines.append("m_tEndColorVar.a = %s;" % bomb["finishColorVarianceAlpha"])
    lines.append("m_fStartSize = %s;" % bomb["startParticleSize"])
    lines.append("m_fStartSizeVar = %s;" % bomb["startParticleSizeVariance"])
    lines.append("m_fEndSize = %s;" % bomb["finishParticleSize"])
    lines.append("m_fEndSizeVar = %s;" % bomb["finishParticleSizeVariance"])
    lines.append("this->setPosition( ccp(%d, %d) );" % (bomb["sourcePositionx"], bomb["sourcePositiony"]))
    lines.append("m_tPosVar.x = %s;" % bomb["sourcePositionVariancex"])
    lines.append("m_tPosVar.y = %s;" % bomb["sourcePositionVariancey"])
    lines.append("m_fStartSpin = %s;" % bomb["rotationStart"])
    lines.append("m_fStartSpinVar = %s;" % bomb["rotationStartVariance"])
    lines.append("m_fEndSpin = %s;" % bomb["rotationEnd"])
    lines.append("m_fEndSpinVar = %s;" % bomb["rotationEndVariance"])
    lines.append("m_nEmitterMode = %d;" % bomb["emitterType"])
    
    if bomb["emitterType"] == 0:
        lines.append("modeA.gravity.x = %s;" % bomb["gravityx"])
        lines.append("modeA.gravity.y = %s;" % bomb["gravityy"])
        lines.append("modeA.speed = %s;" % bomb["speed"])
        lines.append("modeA.speedVar = %s;" % bomb["speedVariance"])
        lines.append("modeA.radialAccel = %s;" % bomb["radialAcceleration"])
        lines.append("modeA.radialAccelVar = %s;" % bomb["radialAccelVariance"])
        lines.append("modeA.tangentialAccel = %s;" % bomb["tangentialAcceleration"])
        lines.append("modeA.tangentialAccelVar = %s;" % bomb["tangentialAccelVariance"])
        lines.append("modeA.rotationIsDir = %s;" %  ('true' if bomb["rotationIsDir"] else "false"))
    elif bomb["emitterType"] == 1:
        lines.append("modeB.startRadius = %s;" % bomb["maxRadius"])
        lines.append("modeB.startRadiusVar = %s;" % bomb["maxRadiusVariance"])
        lines.append("modeB.endRadius = %s;" % bomb["minRadius"])
        lines.append("modeB.endRadiusVar = 0.0f;")
        lines.append("modeB.rotatePerSecond = %s;" % bomb["rotatePerSecond"])
        lines.append("modeB.rotatePerSecondVar = %s;" % bomb["rotatePerSecondVariance"])
    
    lines.append("m_fLife = %s;" % bomb["particleLifespan"])
    lines.append("m_fLifeVar = %s;" % bomb["particleLifespanVariance"])
    lines.append("m_fEmissionRate = m_uTotalParticles / m_fLife;")
    
    lines.append("if (!m_pBatchNode) {")
    lines.append("    m_bOpacityModifyRGB = false;")
    lines.append("    std::string textureName = \"%s\";" % bomb["textureFileName"])
    lines.append("    size_t rPos = textureName.rfind('/');")
    lines.append("    if (rPos != string::npos) {")
    lines.append("        string textureDir = textureName.substr(0, rPos + 1);")
    lines.append("        if (dirname != NULL && textureDir != dirname) {")
    lines.append("            textureName = textureName.substr(rPos+1);")
    lines.append("            textureName = string(dirname) + textureName;")
    lines.append("        }")
    lines.append("    } else {")
    lines.append("        if (dirname != NULL) {")
    lines.append("            textureName = string(dirname) + textureName;")
    lines.append("        }")
    lines.append("    }")
    lines.append("    CCTexture2D *tex = NULL;")
    lines.append("    if (textureName.length() > 0) {")
    lines.append("        bool bNotify = CCFileUtils::sharedFileUtils()->isPopupNotify();")
    lines.append("        CCFileUtils::sharedFileUtils()->setPopupNotify(false);")
    lines.append("        tex = CCTextureCache::sharedTextureCache()->addImage(textureName.c_str());")
    lines.append("        CCFileUtils::sharedFileUtils()->setPopupNotify(bNotify);")
    lines.append("    }")
    lines.append("    if (tex) {")
    lines.append("        setTexture(tex);")
    lines.append("    } else {")
    lines.append("        const char *textureData = \"%s\";" % bomb["textureImageData"])
    lines.append("        int dataLen = strlen(textureData);")
    lines.append("        if (dataLen != 0) {")
    lines.append("            int decodeLen = base64Decode((unsigned char*)textureData, (unsigned int)dataLen, &buffer);")
    lines.append("            CC_BREAK_IF(!buffer);")
    lines.append("            int deflatedLen = ZipUtils::ccInflateMemory(buffer, decodeLen, &deflated);")
    lines.append("            CC_BREAK_IF(!deflated);")
    lines.append("            image = new CCImage();")
    lines.append("            bool isOK = image->initWithImageData(deflated, deflatedLen);")
    lines.append("            CC_BREAK_IF(!isOK);")
    lines.append("            setTexture(CCTextureCache::sharedTextureCache()->addUIImage(image, textureName.c_str()));")
    lines.append("            image->release();")
    lines.append("       }")
    lines.append("    }")
    lines.append("}")
    
    print "bool bRet = false;"
    print "unsigned char *buffer = NULL;"
    print "unsigned char *deflated = NULL;"
    print "CCImage *image = NULL;"
    
    print "do {"
    print "\n".join(lines)
    print "} while(0);"
    print "CC_SAFE_DELETE_ARRAY(buffer);"
    print "CC_SAFE_DELETE_ARRAY(deflated);"

if len(sys.argv) == 2:
    main()
else:
    print "./convert_plist.py [plist file path]"
    print "[ex] ./convert_plist.py Resources/particleTexture.plist"