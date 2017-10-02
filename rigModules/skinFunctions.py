import maya.cmds as cmds

from Jenks.scripts.rigModules import fileFunctions as fileFn

def getSkinValues(obj, tol=0.001):
    vtxList, skinCls = getSkinInfo(obj)
    if not vtxList or not skinCls:
        return False
    skinInfluences = {}
    for each in skinCls:
        influences = {}
        influences['joints'] = cmds.skinCluster(each, q=1, inf=1)
        influences['weights'] = {}
        for vtx in vtxList:
            influenceVals = cmds.skinPercent(each, vtx, ib=tol, q=1, value=1)
            infulenceNames = cmds.skinPercent(each, vtx, ib=tol, q=1, transform=None)
            influences['weights'][vtx] = zip(infulenceNames, influenceVals)
        skinInfluences[each] = influences
    return skinInfluences

def getSkinInfo(obj):
    ## skin cluster(s)
    shapes = cmds.listRelatives(obj, s=1)
    if not shapes:
        return False, False
    skinCls = []
    for each in shapes:
        cls = cmds.listConnections(each, type='skinCluster')
        if cls:
            skinCls.extend(cls)
    ## vertices
    vtxList = []
    for x in cmds.getAttr('{}.vrts'.format(obj), multiIndices=1):
        vtxList.append('{}.vtx[{}]'.format(obj, x))
    return vtxList, skinCls

def loadSkin(geo, assetName=None, prompt=False, override=False):
    if prompt:
        assetName = assetNamePrompt()
    if not assetName:
        assetName = getAssetName()
    if not assetName:
        print 'Asset Name not specified.'
        return False
    path = fileFn.getAssetDir()
    fileName = fileFn.getLatestVersion(assetName, path, 'rig/WIP/skin', name=geo)
    if not fileName:
        return False
    skinData = fileFn.loadJson(fileOverride=fileName)
    print 'Loading Skin Data: {}'.format(fileName)
    # do stuff with skin data
    vtxList, skinCls = getSkinInfo(geo)
    if skinCls:
        if override:
            cmds.skinCluster(skinCls, e=1, unbind=1)
        else:
            return False
    for clusterName in skinData.keys():
        for jnt in skinData[clusterName]['joints']:
            if not cmds.objExists(jnt):
                cmds.warning('{} from {} cluster not found.'.format(jnt, clusterName))
                return False
        cmds.skinCluster(geo, skinData[clusterName]['joints'])
        for vtx in skinData[clusterName]['weights']:
            cmds.skinPercent(clusterName, vtx, tv=skinData[clusterName]['weights'][vtx])
            cmds.select(cl=1)
    return True

def saveSkin(geo, assetName=None, prompt=False):
    if prompt:
        assetName = fileFn.assetNamePrompt()
    if not assetName:
        assetName = fileFn.getAssetName()
    if not assetName:
        print 'Asset Name not specified.'
        return False
    path = fileFn.getAssetDir()
    skinData = getSkinValues(geo)
    if skinData:
        skinFile = fileFn.getLatestVersion(assetName, path, 'rig/WIP/skin', new=True, name=geo)
        status = fileFn.saveJson(skinData, fileOverride=[skinFile])
        return status
    else:
        return False

def saveAllSkin(assetName=None, prompt=False):
    if prompt:
        assetName = fileFn.assetNamePrompt()
    if not assetName:
        assetName = fileFn.getAssetName()
    if not assetName:
        print 'Asset Name not specified.'
        return False
    geo = cmds.listRelatives('C_geometry_GRP', ad=1, type='transform')
    if geo:
        for each in geo:
            saveSkin(assetName, each)
        return True
    else:
        return False

def loadAllSkin(assetName=None, prompt=False):
    if prompt:
        assetName = fileFn.assetNamePrompt()
    if not assetName:
        assetName = fileFn.getAssetName()
    if not assetName:
        print 'Asset Name not specified.'
        return False
    print 'Starting Skinning From Saved Files.'
    geo = cmds.ls(type='transform')
    if geo:
        for each in geo:
            loadSkin(each, assetName)
        print 'Finished Skinning From Saved Files.'
        return True
    else:
        print 'Skinning From Saved Files FAILED.'
        return False