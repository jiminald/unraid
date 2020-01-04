"""Constants used in the Unraid components."""

DOMAIN = "unraid"
HOSTS = "host"

ENDPOINTS = {
    # Array
    "array": "array { "+
            "previousState "+
            "pendingState "+
            "state "+
            "capacity { "+
                "bytes { "+
                    "free "+
                    "used "+
                    "total "+
                "} "+
                "disks { "+
                    "free "+
                    "used "+
                    "total "+
                "} "+
            "} "+
            "boot { "+
                "slot "+
                "name "+
                "device "+
                "id "+
                "size "+
                "status "+
                "rotational "+
                "format "+
                "temp "+
                "numReads "+
                "numWrites "+
                "numErrors "+
                "type "+
                "color "+
                "fsStatus "+
                "luksState "+
                "comment "+
                "exportable "+
                "fsType "+
                "fsColor "+
                "fsSize "+
                "fsFree "+
                "spindownDelay "+
                "spinupGroup "+
                "deviceSb "+
                "idSb "+
                "sizeSb "+
            "} "+
            "parities { "+
                "slot "+
                "name "+
                "device "+
                "id "+
                "size "+
                "status "+
                "rotational "+
                "format "+
                "temp "+
                "numReads "+
                "numWrites "+
                "numErrors "+
                "type "+
                "color "+
                "fsStatus "+
                "luksState "+
                "comment "+
                "exportable "+
                "fsType "+
                "fsColor "+
                "fsSize "+
                "fsFree "+
                "spindownDelay "+
                "spinupGroup "+
                "deviceSb "+
                "idSb "+
                "sizeSb "+
            "} "+
            "disks { "+
                "slot "+
                "name "+
                "device "+
                "id "+
                "size "+
                "status "+
                "rotational "+
                "format "+
                "temp "+
                "numReads "+
                "numWrites "+
                "numErrors "+
                "type "+
                "color "+
                "fsStatus "+
                "luksState "+
                "comment "+
                "exportable "+
                "fsType "+
                "fsColor "+
                "fsSize "+
                "fsFree "+
                "spindownDelay "+
                "spinupGroup "+
                "deviceSb "+
                "idSb "+
                "sizeSb "+
            "} "+
            "caches { "+
                "slot "+
                "name "+
                "device "+
                "id "+
                "size "+
                "status "+
                "rotational "+
                "format "+
                "temp "+
                "numReads "+
                "numWrites "+
                "numErrors "+
                "type "+
                "color "+
                "fsStatus "+
                "luksState "+
                "comment "+
                "exportable "+
                "fsType "+
                "fsColor "+
                "fsSize "+
                "fsFree "+
                "spindownDelay "+
                "spinupGroup "+
                "deviceSb "+
                "idSb "+
                "sizeSb "+
            "} "+
        "} ",

    "parityHistory": "parityHistory { "+
        "date "+
        "duration "+
        "speed "+
        "status "+
        "errors "+
    "} ",

    # Devices
    "devices": "devices { "+
        "id "+
        "tag "+
        "device "+
        "sectors "+
        "sectorSize "+
    "}",

    # Disks
    "disks": "disks { "+
            "device "+
            "type "+
            "name "+
            "vendor "+
            "size "+
            "bytesPerSector "+
            "totalCylinders "+
            "totalHeads "+
            "totalSectors "+
            "totalTracks "+
            "tracksPerCylinder "+
            "sectorsPerTrack "+
            "firmwareRevision "+
            "serialNum "+
            # "interfaceType "+
            "smartStatus "+
            "temperature "+
            "partitions { "+
                "name "+
                # "fsType "+
                "size "+
            "} "+
        "} ",

    # Docker
    "dockerContainers": "dockerContainers { "+
        "id "+
        "names "+
        "image "+
        "imageId "+
        "command "+
        "created "+
        "ports { "+
            "ip "+
            "privatePort "+
            "publicPort "+
            "type "+
        "} "+
        "sizeRootFs "+
        "labels "+
        "state "+
        "status "+
        "hostConfig { "+
            "networkMode "+
        "} "+
        "networkSettings "+
        "mounts "+
        "autoStart "+
    "} ",

    "dockerNetworks": "dockerNetworks { "+
        "name "+
        "id "+
        "created "+
        "scope "+
        "driver "+
        "enableIPv6 "+
        "ipam "+
        "internal "+
        "attachable "+
        "ingress "+
        "configFrom "+
        "configOnly "+
        "containers "+
        "options "+
        "labels "+
    "} ",

    # Info
    "info": "info { "+
        "apps { "+
            "installed "+
            "started "+
        "} "+
        "baseboard { "+
            "manufacturer "+
            "model "+
            "version "+
            "serial "+
            "assetTag "+
        "} "+
        "cpu {"+
            "manufacturer "+
            "brand "+
            "vendor "+
            "family "+
            "model "+
            "stepping "+
            "revision "+
            "voltage "+
            "speed "+
            "speedmin "+
            "speedmax "+
            "threads "+
            "cores "+
            "processors "+
            "socket "+
            "cache "+
            "flags "+
        "} "+
        "display { "+
            "date "+
            "number "+
            "scale "+
            "tabs "+
            "users "+
            "resize "+
            "wwn "+
            "total "+
            "usage "+
            "banner "+
            "dashapps "+
            "theme "+
            "text "+
            "unit "+
            "warning "+
            "critical "+
            "hot "+
            "max "+
        "} "+
        "memory { "+
            "max "+
            "total "+
            "free "+
            "used "+
            "active "+
            "available "+
            "buffcache "+
            "swaptotal "+
            "swapused "+
            "swapfree "+
            "layout { "+
                "size "+
                "bank "+
                "type "+
                "clockSpeed "+
                "formFactor "+
                "manufacturer "+
                "partNum "+
                "serialNum "+
                "voltageConfigured "+
                "voltageMin "+
                "voltageMax "+
            "} "+
        "} "+
        "os { "+
            "platform "+
            "distro "+
            "release "+
            "codename "+
            "kernel "+
            "arch "+
            "hostname "+
            "codepage "+
            "logofile "+
            "serial "+
            "build "+
        "} "+
        # "system { "+
        #     "manufacturer "+
        #     "model "+
        #     "version "+
        #     "serial "+
        #     "uuid "+
        #     "sku "+
        # "} "+
        "versions { "+
            "kernel "+
            "openssl "+
            "systemOpenssl "+
            "systemOpensslLib "+
            "node "+
            "v8 "+
            "npm "+
            "yarn "+
            "pm2 "+
            "gulp "+
            "grunt "+
            "git "+
            "tsc "+
            "mysql "+
            "redis "+
            "mongodb "+
            "apache "+
            "nginx "+
            "php "+
            "docker "+
            "postfix "+
            "postgresql "+
            "perl "+
            "python "+
            "gcc "+
            "unraid "+
        "} "+
    "} ",

    # Plugins
    "plugins": "plugins { "+
        "name "+
        "isActive "+
        "disabled "+
        "modules { "+
            "name "+
            "filePath "+
            "isActive "+
        "} "+
    "} ",

    # Services
    "services": "services { "+
        "name "+
        "online "+
        "uptime "+
        "version "+
    "} ",

    # Shares
    "shares": "shares { "+
        "name "+
        "free "+
        "size "+
        "include "+
        "exclude "+
        "cache "+
        "nameOrig "+
        "comment "+
        "allocator "+
        "splitLevel "+
        "floor "+
        "cow "+
        "color "+
        "luksStatus "+
    "} ",

    # Variables
    "vars": "vars {"+
        "version "+
        "maxArraysz "+
        "maxCachesz "+
        "name "+
        "timeZone "+
        "comment "+
        "security "+
        "workgroup "+
        "domain "+
        "domainShort "+
        "hideDotFiles "+
        "localMaster "+
        "enableFruit "+
        "useNtp "+
        "ntpServer1 "+
        "ntpServer2 "+
        "ntpServer3 "+
        "ntpServer4 "+
        "domainLogin "+
        "sysModel "+
        "sysArraySlots "+
        "sysCacheSlots "+
        "sysFlashSlots "+
        "useSsl "+
        "port "+
        "portssl "+
        "localTld "+
        "bindMgt "+
        "useTelnet "+
        "porttelnet "+
        "useSsh "+
        "portssh "+
        "startPage "+
        "startArray "+
        "spindownDelay "+
        "queueDepth "+
        "spinupGroups "+
        "defaultFormat "+
        "defaultFsType "+
        "shutdownTimeout "+
        "luksKeyfile "+
        "pollAttributes "+
        "pollAttributesDefault "+
        "pollAttributesStatus "+
        "nrRequests "+
        "nrRequestsDefault "+
        "nrRequestsStatus "+
        "mdNumStripes "+
        "mdNumStripesDefault "+
        "mdNumStripesStatus "+
        "mdSyncWindow "+
        "mdSyncWindowDefault "+
        "mdSyncWindowStatus "+
        "mdSyncThresh "+
        "mdSyncThreshDefault "+
        "mdSyncThreshStatus "+
        "mdWriteMethod "+
        "mdWriteMethodDefault "+
        "mdWriteMethodStatus "+
        "shareDisk "+
        "shareUser "+
        "shareUserInclude "+
        "shareUserExclude "+
        "shareSmbEnabled "+
        "shareNfsEnabled "+
        "shareAfpEnabled "+
        "shareInitialOwner "+
        "shareInitialGroup "+
        "shareCacheEnabled "+
        "shareCacheFloor "+
        "shareMoverSchedule "+
        "shareMoverLogging "+
        "fuseRemember "+
        "fuseRememberDefault "+
        "fuseRememberStatus "+
        "fuseDirectio "+
        "fuseDirectioDefault "+
        "fuseDirectioStatus "+
        "shareAvahiEnabled "+
        "shareAvahiSmbName "+
        "shareAvahiSmbModel "+
        "shareAvahiAfpName "+
        "shareAvahiAfpModel "+
        "safeMode "+
        "startMode "+
        "configValid "+
        "joinStatus "+
        "deviceCount "+
        "flashGuid "+
        "flashProduct "+
        "flashVendor "+
        "regCheck "+
        "regFile "+
        "regGuid "+
        "regTy "+
        "regTo "+
        "regTm "+
        "regTm2 "+
        "regGen "+
        "sbName "+
        "sbVersion "+
        "sbUpdated "+
        "sbEvents "+
        "sbState "+
        "sbClean "+
        "sbSynced "+
        "sbSyncErrs "+
        "sbSynced2 "+
        "sbSyncExit "+
        "sbNumDisks "+
        "mdColor "+
        "mdNumDisks "+
        "mdNumDisabled "+
        "mdNumInvalid "+
        "mdNumMissing "+
        "mdNumNew "+
        "mdNumErased "+
        "mdResync "+
        "mdResyncCorr "+
        "mdResyncPos "+
        "mdResyncDb "+
        "mdResyncDt "+
        "mdResyncAction "+
        "mdResyncSize "+
        "mdState "+
        "mdVersion "+
        "cacheNumDevices "+
        "cacheSbNumDisks "+
        "fsState "+
        "fsProgress "+
        "fsCopyPrcnt "+
        "fsNumMounted "+
        "fsNumUnmountable "+
        "fsUnmountableMask "+
        "shareCount "+
        "shareSmbCount "+
        "shareNfsCount "+
        "shareAfpCount "+
        "shareMoverActive "+
        "csrfToken "+
        "uptime "+
    "} ",

    # Virtual Machines
    "vms": "vms { "+
        "domains { "+
            "uuid "+
            "osType "+
            "autostart "+
            "maxMemory "+
            "schedulerType "+
            "schedulerParameters { "+
                "cpu_shares "+
                "vcpu_period "+
                "vcpu_quota "+
                "emulator_period "+
                "emulator_quota "+
                "global_period "+
                "global_quota "+
                "iothread_period "+
                "iothread_quota "+
            "} "+
            "securityLabel { "+
                "label "+
                "enforcing "+
            "} "+
            "name "+
            "state "+
            "memory "+
            "vcpus "+
            "cpuTime "+
        "} "+
    "} ",
}

SENSOR_LIST = list(ENDPOINTS)
SENSOR_STATE = {
    "array": {"field": "state", "action": "none"},
    "parityHistory": { "field": "errors", "action": "latest" },
    "devices": { "field": "", "action": "none" },
    "disks": { "field": "", "action": "count" },
    "dockerContainers": { "field": "", "action": "count" },
    "dockerNetworks": { "field": "", "action": "count" },
    "info": { "field": "versions_unraid", "action": "none" },
    "plugins": { "field": "", "action": "count" },
    "services": { "field": "", "action": "count" },
    "shares": { "field": "", "action": "count" },
    "vars": { "field": "uptime", "action": "none"},
    "vms": { "field": "domains", "action": "count" }
}
