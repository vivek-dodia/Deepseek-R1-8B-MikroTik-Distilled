# Repository Information
Name: terraform-mikrotik

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/sshqcruss/terraform-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: dashboard.yaml
================================================
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: mikrotik-mktxp-exporter
  namespace: monitoring
  labels:
    app: grafana
    env: home-lab
    stream: sre
    owner: sre
    product: observability
    temporary: "false"
    deleteAfter: "false"
    grafana_dashboard: ""
data:
  mikrotik-mktxp-exporter-overview.json: |
    {
      "annotations": {
        "list": [
          {
            "builtIn": 1,
            "datasource": {
              "type": "datasource",
              "uid": "grafana"
            },
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "target": {
              "limit": 100,
              "matchAny": false,
              "tags": [],
              "type": "dashboard"
            },
            "type": "dashboard"
          }
        ]
      },
      "description": "Mikrotik MKTXP Exporter metrics",
      "editable": true,
      "fiscalYearStartMonth": 0,
      "gnetId": 13679,
      "graphTooltip": 0,
      "id": 1,
      "links": [
        {
          "asDropdown": false,
          "icon": "external link",
          "includeVars": false,
          "keepTime": false,
          "tags": [
            "mikrotik",
            "loki"
          ],
          "targetBlank": false,
          "title": "Mikrotik Loki Logs ",
          "tooltip": "",
          "type": "dashboards",
          "url": ""
        },
        {
          "asDropdown": true,
          "icon": "external link",
          "includeVars": false,
          "keepTime": false,
          "tags": [
            "system"
          ],
          "targetBlank": false,
          "title": "System Overview",
          "tooltip": "",
          "type": "dashboards",
          "url": ""
        }
      ],
      "liveNow": false,
      "panels": [
        {
          "collapsed": false,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 0
          },
          "id": 10,
          "panels": [],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "System",
          "type": "row"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "fixed"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 0,
            "y": 1
          },
          "id": 72,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_identity_info{routerboard_name=\"$node\"}  ",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "B"
            }
          ],
          "title": "Identity",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "fixed"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 3,
            "x": 2,
            "y": 1
          },
          "id": 6,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_uptime{routerboard_name=\"$node\"}",
              "instant": true,
              "interval": "",
              "legendFormat": "{{board_name}}",
              "refId": "B"
            }
          ],
          "title": "Routerboard HW",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "dtdurations"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "displayName",
                    "value": "enabled"
                  },
                  {
                    "id": "mappings",
                    "value": [
                      {
                        "options": {
                          "false": {
                            "color": "green",
                            "index": 0,
                            "text": "Yes"
                          },
                          "true": {
                            "color": "red",
                            "index": 1,
                            "text": "No"
                          }
                        },
                        "type": "value"
                      }
                    ]
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 80
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 5,
            "x": 5,
            "y": 1
          },
          "id": 94,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_installed_packages_info{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Installed Packages",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true,
                  "version": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 10,
                  "__name__": 1,
                  "build_time": 6,
                  "disabled": 5,
                  "instance": 2,
                  "job": 3,
                  "name": 4,
                  "routerboard_address": 7,
                  "routerboard_name": 8,
                  "version": 9
                },
                "renameByName": {
                  "disabled": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "decimals": 1,
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0.1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "rgba(50, 172, 45, 0.97)",
                    "value": null
                  },
                  {
                    "color": "rgba(237, 129, 40, 0.89)",
                    "value": 70
                  },
                  {
                    "color": "rgba(245, 54, 54, 0.9)",
                    "value": 90
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 4,
            "x": 10,
            "y": 1
          },
          "id": 14,
          "maxDataPoints": 100,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Memory"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "(1 - mktxp_system_free_memory{routerboard_name=\"$node\"} / mktxp_system_total_memory{routerboard_name=\"$node\"})*100",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Used memory"
              },
              "legendFormat": "Used RAM Memory",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_cpu_load{routerboard_name=\"$node\"}",
              "instant": true,
              "interval": "",
              "legendFormat": "CPU Load",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "(1 - mktxp_system_free_hdd_space{routerboard_name=\"$node\"} / mktxp_system_total_hdd_space{routerboard_name=\"$node\"})*100",
              "instant": true,
              "interval": "",
              "legendFormat": "HDD Utilization",
              "refId": "B"
            }
          ],
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "symlog"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 5,
            "x": 14,
            "y": 1
          },
          "id": 16,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "CPU"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_cpu_load{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "CPU 1 load"
              },
              "legendFormat": "{{cpu}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "CPU load",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "hertz"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Total memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#E24D42",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Used memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#1F78C1",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Total memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#E24D42",
                      "mode": "fixed"
                    }
                  },
                  {
                    "id": "custom.fillOpacity",
                    "value": 20
                  },
                  {
                    "id": "custom.lineWidth",
                    "value": 0
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Used memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#1F78C1",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 5,
            "x": 19,
            "y": 1
          },
          "id": 115,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.2.5",
          "targets": [
            {
              "application": {
                "filter": "Memory"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_cpu_frequency{routerboard_name=\"$node\"}*1000000",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Used memory"
              },
              "legendFormat": "{{cpu}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "CPU Frequency",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "hertz"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 3,
            "x": 2,
            "y": 3
          },
          "id": 116,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "value_and_name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "mktxp_system_cpu_frequency{routerboard_name=\"$node\"}*1000000",
              "instant": true,
              "interval": "",
              "legendFormat": "{{cpu}} ",
              "range": false,
              "refId": "B"
            }
          ],
          "title": "CPU",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "mappings": [],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "green",
                    "value": 30
                  },
                  {
                    "color": "yellow",
                    "value": 40
                  },
                  {
                    "color": "orange",
                    "value": 60
                  },
                  {
                    "color": "red",
                    "value": 70
                  }
                ]
              },
              "unit": "celsius"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 2,
            "x": 0,
            "y": 4
          },
          "id": 59,
          "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showThresholdLabels": false,
            "showThresholdMarkers": true,
            "sizing": "auto",
            "text": {}
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_routerboard_temperature{routerboard_name=\"$node\"}  ",
              "instant": true,
              "interval": "",
              "legendFormat": "__auto",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_cpu_temperature{routerboard_name=\"$node\"}  ",
              "hide": false,
              "legendFormat": "__auto",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Temperature",
          "type": "gauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "fixed"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 3,
            "x": 2,
            "y": 5
          },
          "id": 120,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "General"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_uptime{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "System version and hw"
              },
              "legendFormat": "Current: {{version}} ",
              "mode": 2,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_update_available{routerboard_name=\"$node\"}",
              "hide": false,
              "instant": false,
              "legendFormat": "Latest available: {{newest_version}}",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "System version",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "fixed"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "dtdurations"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 3,
            "x": 2,
            "y": 8
          },
          "id": 12,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "General"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_uptime{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "System uptime"
              },
              "legendFormat": "",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "System uptime",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "dtdurations"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "displayName",
                    "value": "enabled"
                  },
                  {
                    "id": "mappings",
                    "value": [
                      {
                        "options": {
                          "false": {
                            "color": "green",
                            "index": 0,
                            "text": "Yes"
                          },
                          "true": {
                            "color": "red",
                            "index": 1,
                            "text": "No"
                          }
                        },
                        "type": "value"
                      }
                    ]
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 80
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 9,
            "x": 5,
            "y": 8
          },
          "id": 98,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": false,
                "displayName": "name"
              }
            ]
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_active_users_info{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Active Users",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true,
                  "version": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 8,
                  "__name__": 1,
                  "address": 9,
                  "group": 5,
                  "instance": 2,
                  "job": 3,
                  "name": 4,
                  "routerboard_address": 6,
                  "routerboard_name": 7,
                  "via": 10,
                  "when": 11
                },
                "renameByName": {
                  "disabled": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "decbytes"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Total memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#E24D42",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Used memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#1F78C1",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Total memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#E24D42",
                      "mode": "fixed"
                    }
                  },
                  {
                    "id": "custom.fillOpacity",
                    "value": 20
                  },
                  {
                    "id": "custom.lineWidth",
                    "value": 0
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Used memory"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#1F78C1",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 10,
            "x": 14,
            "y": 8
          },
          "id": 18,
          "options": {
            "legend": {
              "calcs": [
                "lastNotNull"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.2.5",
          "targets": [
            {
              "application": {
                "filter": "Memory"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_total_hdd_space{routerboard_name=\"$node\"} - mktxp_system_free_hdd_space{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Used memory"
              },
              "legendFormat": "Used memory",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "application": {
                "filter": "Memory"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_total_hdd_space{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Total memory"
              },
              "legendFormat": "Total memory",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "B"
            }
          ],
          "title": "HDD Utilization",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "fixed"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "volt"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 2,
            "x": 0,
            "y": 10
          },
          "id": 57,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "value",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "General"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_system_routerboard_voltage{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "System version and hw"
              },
              "legendFormat": "",
              "mode": 2,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Voltage",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "palette-classic"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 3,
            "x": 2,
            "y": 10
          },
          "id": 113,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_public_ip_address_info{routerboard_name=\"$node\"}",
              "instant": true,
              "interval": "",
              "legendFormat": "{{routerboard_address}}",
              "refId": "B"
            }
          ],
          "title": "IP Address",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "green",
                "mode": "palette-classic"
              },
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "text": "N/A"
                    }
                  },
                  "type": "special"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 5,
            "x": 0,
            "y": 12
          },
          "id": 93,
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "text": {},
            "textMode": "name",
            "wideLayout": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_public_ip_address_info{routerboard_name=\"$node\"}",
              "instant": true,
              "interval": "",
              "legendFormat": "{{public_address}}",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_public_ip_address_info{routerboard_name=\"$node\"}",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "{{dns_name}}",
              "refId": "A"
            }
          ],
          "title": "Public Address",
          "type": "stat"
        },
        {
          "collapsed": false,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 15
          },
          "id": 2,
          "panels": [],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "DHCP",
          "type": "row"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 5,
            "x": 0,
            "y": 16
          },
          "id": 97,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_ip_pool_used{routerboard_name=\"$node\"} ",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ pool }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "IP Pool Usage",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "dtdurations"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 231
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP VLAN"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 227
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "active_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 240
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Host Name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 383
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Comment"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 360
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 19,
            "w": 19,
            "x": 5,
            "y": 16
          },
          "id": 25,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "active_address"
              }
            ]
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_dhcp_lease_info{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "DHCP Leases",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": false,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 9,
                  "Value": 13,
                  "__name__": 8,
                  "active_address": 5,
                  "address": 4,
                  "comment": 1,
                  "expires_after": 6,
                  "host_name": 0,
                  "instance": 7,
                  "job": 10,
                  "mac_address": 3,
                  "routerboard_address": 11,
                  "routerboard_name": 12,
                  "server": 2
                },
                "renameByName": {
                  "Value": "Expires After",
                  "comment": "Comment",
                  "host_name": "Host Name",
                  "server": "DHCP Server"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 5,
            "x": 0,
            "y": 24
          },
          "id": 20,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_dhcp_lease_active_count{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ server }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "DHCP Leases by Server",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 5,
            "x": 0,
            "y": 32
          },
          "id": 23,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "sum(mktxp_dhcp_lease_active_count{routerboard_name=\"$node\"})",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "In - {{ server }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Total DHCP Leases",
          "type": "bargauge"
        },
        {
          "collapsed": false,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 35
          },
          "id": 45,
          "panels": [],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "Network",
          "type": "row"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "Unplugged"
                    },
                    "1": {
                      "text": ""
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 2,
            "x": 0,
            "y": 36
          },
          "id": 70,
          "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showThresholdLabels": false,
            "showThresholdMarkers": true,
            "sizing": "auto",
            "text": {}
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_routes_total_routes{routerboard_name=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Total Routes",
          "type": "gauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 4,
            "x": 2,
            "y": 36
          },
          "id": 71,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_routes_protocol_count{routerboard_name=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "/errors on interface/"
              },
              "legendFormat": "{{protocol}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Routes per protocol",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "No"
                    },
                    "1": {
                      "text": "Yes"
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 6,
            "x": 6,
            "y": 36
          },
          "id": 69,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_interface_full_duplex{routerboard_name=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Ethernet Ports: Full Duplex",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "pps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byRegexp",
                  "options": "/Out/"
                },
                "properties": [
                  {
                    "id": "custom.transform",
                    "value": "negative-Y"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 16,
            "w": 12,
            "x": 12,
            "y": 36
          },
          "id": 55,
          "options": {
            "legend": {
              "calcs": [
                "sum"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_interface_rx_error_total{routerboard_name=\"$node\"}[4m])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "/errors on interface/"
              },
              "legendFormat": "In Errors | {{name}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_interface_tx_error_total{routerboard_name=\"$node\"}[4m])",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Out Errors | {{name}}",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Interface Errors",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "Unplugged"
                    },
                    "1": {
                      "text": "Plugged-In"
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 0,
            "y": 41
          },
          "id": 51,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "last"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_interface_status{routerboard_name=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Ethernet Ports: Status",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "custom": {
                "align": "auto",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "Mbits"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 6,
            "y": 41
          },
          "id": 53,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_interface_rate{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Rates",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "__name__": true,
                  "address": true,
                  "env": true,
                  "instance": true,
                  "job": true,
                  "name": false,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {},
                "renameByName": {
                  "Value": "Rate",
                  "name": "Interface",
                  "routerboard_name": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 231
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP VLAN"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 227
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "active_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 240
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Host Name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 383
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Comment"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 360
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 4,
            "w": 12,
            "x": 0,
            "y": 48
          },
          "id": 85,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "active_address"
              }
            ]
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_poe_info{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "POE",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 9,
                  "Value": 13,
                  "__name__": 8,
                  "active_address": 5,
                  "address": 4,
                  "comment": 1,
                  "expires_after": 6,
                  "host_name": 0,
                  "instance": 7,
                  "job": 10,
                  "mac_address": 3,
                  "routerboard_address": 11,
                  "routerboard_name": 12,
                  "server": 2
                },
                "renameByName": {
                  "comment": "Comment",
                  "host_name": "Host Name",
                  "name": "Interface",
                  "poe_out": "State",
                  "poe_out_status": "Status",
                  "poe_priority": "Priority",
                  "server": "DHCP Server"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byRegexp",
                  "options": "/Out/"
                },
                "properties": [
                  {
                    "id": "custom.transform",
                    "value": "negative-Y"
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-GrYlRd"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byRegexp",
                  "options": "/In/"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-BlPu"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 14,
            "w": 24,
            "x": 0,
            "y": 52
          },
          "id": 75,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.2.5",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_interface_rx_byte_total{routerboard_name=\"$node\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "In | {{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_interface_tx_byte_total{routerboard_name=\"$node\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Outgoing traffic on interface ether1-gateway"
              },
              "legendFormat": "Out | {{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Interface traffic ",
          "type": "timeseries"
        },
        {
          "collapsed": false,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 66
          },
          "id": 84,
          "panels": [],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "Firewall",
          "type": "row"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "displayName",
                    "value": "enabled"
                  },
                  {
                    "id": "mappings",
                    "value": [
                      {
                        "options": {
                          "false": {
                            "color": "green",
                            "index": 0,
                            "text": "Yes"
                          },
                          "true": {
                            "color": "red",
                            "index": 1,
                            "text": "No"
                          }
                        },
                        "type": "value"
                      }
                    ]
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "disabled"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 80
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "dst_addresses"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 424
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 67
          },
          "id": 117,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "enablePagination": false,
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "Count"
              }
            ]
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "mktxp_connection_stats{routerboard_name=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Open Connections",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": false,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true,
                  "version": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 7,
                  "__name__": 1,
                  "dhcp_name": 6,
                  "dst_addresses": 8,
                  "instance": 2,
                  "job": 3,
                  "routerboard_address": 4,
                  "routerboard_name": 5,
                  "src_address": 9
                },
                "renameByName": {
                  "Value": "Count",
                  "disabled": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "fillOpacity": 80,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineWidth": 1,
                "scaleDistribution": {
                  "type": "linear"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "#6ED0E0",
                    "value": 5
                  },
                  {
                    "color": "#EAB839",
                    "value": 10
                  },
                  {
                    "color": "#EF843C",
                    "value": 40
                  },
                  {
                    "color": "red",
                    "value": 60
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 67
          },
          "id": 118,
          "options": {
            "barRadius": 0,
            "barWidth": 0.97,
            "fullHighlight": false,
            "groupWidth": 0.7,
            "legend": {
              "calcs": [
                "last",
                "mean",
                "max"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true,
              "sortBy": "Last",
              "sortDesc": true
            },
            "orientation": "auto",
            "showValue": "auto",
            "stacking": "none",
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            },
            "xTickLabelRotation": 0,
            "xTickLabelSpacing": 0
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "mktxp_connection_stats{routerboard_name=\"$node\"}",
              "instant": true,
              "interval": "",
              "legendFormat": "{{dhcp_name}}",
              "range": false,
              "refId": "A"
            }
          ],
          "title": "Open Connections Stats",
          "type": "barchart"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 0,
            "y": 75
          },
          "id": 81,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_firewall_filter_total{routerboard_name=\"$node\", log=\"1\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Logged Firewall Rules Traffic ",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 12,
            "w": 12,
            "x": 12,
            "y": 75
          },
          "id": 82,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_firewall_raw_total{routerboard_name=\"$node\", log=\"1\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Logged Raw Firewall Rules Traffic ",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 14,
            "w": 12,
            "x": 0,
            "y": 87
          },
          "id": 43,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_firewall_filter_total{routerboard_name=\"$node\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Firewall Rules Traffic ",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 14,
            "w": 12,
            "x": 12,
            "y": 87
          },
          "id": 76,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_firewall_raw_total{routerboard_name=\"$node\"}[4m])*8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Raw Firewall Rules Traffic ",
          "type": "timeseries"
        },
        {
          "collapsed": true,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 101
          },
          "id": 90,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "continuous-GrYlRd"
                  },
                  "custom": {
                    "fillOpacity": 70,
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineWidth": 0,
                    "spanNulls": false
                  },
                  "mappings": [
                    {
                      "options": {
                        "0": {
                          "color": "red",
                          "index": 0,
                          "text": "Down"
                        },
                        "1": {
                          "color": "green",
                          "index": 1,
                          "text": "Up"
                        }
                      },
                      "type": "value"
                    }
                  ],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      }
                    ]
                  }
                },
                "overrides": []
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 0,
                "y": 102
              },
              "id": 87,
              "options": {
                "alignValue": "left",
                "legend": {
                  "displayMode": "list",
                  "placement": "bottom",
                  "showLegend": true
                },
                "mergeValues": true,
                "rowHeight": 0.9,
                "showValue": "never",
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "single",
                  "sort": "none"
                }
              },
              "pluginVersion": "7.4.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "max_over_time(mktxp_netwatch_status{routerboard_name=\"$node\"}[1m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Status over time",
              "type": "state-timeline"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "thresholds"
                  },
                  "custom": {
                    "align": "center",
                    "cellOptions": {
                      "type": "color-text"
                    },
                    "filterable": false,
                    "inspect": false
                  },
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 0
                      },
                      {
                        "color": "green",
                        "value": 1
                      }
                    ]
                  }
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "status"
                    },
                    "properties": [
                      {
                        "id": "mappings",
                        "value": [
                          {
                            "options": {
                              "0": {
                                "color": "red",
                                "index": 0,
                                "text": "Down"
                              },
                              "1": {
                                "color": "green",
                                "index": 1,
                                "text": "Up"
                              }
                            },
                            "type": "value"
                          }
                        ]
                      },
                      {
                        "id": "color",
                        "value": {
                          "mode": "thresholds"
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 12,
                "y": 102
              },
              "id": 88,
              "options": {
                "cellHeight": "sm",
                "footer": {
                  "countRows": false,
                  "fields": "",
                  "reducer": [
                    "sum"
                  ],
                  "show": false
                },
                "showHeader": true,
                "sortBy": []
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_netwatch_info{routerboard_name=\"$node\"}",
                  "format": "table",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "",
                  "refId": "A"
                }
              ],
              "title": "Netwatch Info",
              "transformations": [
                {
                  "id": "organize",
                  "options": {
                    "excludeByName": {
                      "Time": true,
                      "Value": true,
                      "__name__": true,
                      "disabled": true,
                      "instance": true,
                      "job": true,
                      "name": true,
                      "routerboard_address": true,
                      "routerboard_name": true,
                      "timeout": true
                    },
                    "indexByName": {
                      "Time": 5,
                      "Value": 9,
                      "__name__": 4,
                      "comment": 1,
                      "host": 0,
                      "instance": 3,
                      "interval": 11,
                      "job": 6,
                      "name": 12,
                      "routerboard_address": 7,
                      "routerboard_name": 8,
                      "since": 10,
                      "status": 2,
                      "timeout": 13
                    },
                    "renameByName": {
                      "comment": "Comment",
                      "host": "Host",
                      "host_name": "Host Name",
                      "interval": "Interval",
                      "server": "DHCP Server",
                      "since": "Since",
                      "status": "Status"
                    }
                  }
                }
              ],
              "type": "table"
            }
          ],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "Netwatch",
          "type": "row"
        },
        {
          "collapsed": true,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 102
          },
          "id": 29,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "decimals": 1,
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "dB"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsZero",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsNull",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 0,
                "y": 103
              },
              "id": 31,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "lastNotNull",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "bottom",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "none"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_noise_floor{routerboard_name=\"$node\"}",
                  "interval": "",
                  "legendFormat": "{{channel}}",
                  "range": true,
                  "refId": "A"
                }
              ],
              "title": "Noise Floor",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "decimals": 2,
                  "links": [],
                  "mappings": [],
                  "max": 100,
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "percent"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsZero",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsNull",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 12,
                "y": 103
              },
              "id": 73,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "lastNotNull",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "bottom",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "none"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_overall_tx_ccq{routerboard_name=\"$node\"}",
                  "instant": false,
                  "interval": "",
                  "legendFormat": "{{channel}}",
                  "refId": "A"
                }
              ],
              "title": "Overall Tx CCQ",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "fixed"
                  },
                  "custom": {
                    "align": "center",
                    "cellOptions": {
                      "type": "auto"
                    },
                    "filterable": false,
                    "inspect": false
                  },
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  }
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "__name__"
                    },
                    "properties": [
                      {
                        "id": "displayName"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "rx_signal"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 127
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "name"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 267
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "mac_address"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 165
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "ssid"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 140
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 0,
                "y": 111
              },
              "id": 68,
              "options": {
                "cellHeight": "sm",
                "footer": {
                  "countRows": false,
                  "fields": "",
                  "reducer": [
                    "sum"
                  ],
                  "show": false
                },
                "showHeader": true,
                "sortBy": [
                  {
                    "desc": true,
                    "displayName": "rx_signal"
                  }
                ]
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_clients_devices_info{routerboard_name=\"$node\"}",
                  "format": "table",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "",
                  "refId": "A"
                }
              ],
              "title": "Client Devices",
              "transformations": [
                {
                  "id": "organize",
                  "options": {
                    "excludeByName": {
                      "Time": true,
                      "Value": true,
                      "__name__": true,
                      "instance": true,
                      "job": true,
                      "routerboard_address": true,
                      "routerboard_name": true
                    },
                    "indexByName": {
                      "Time": 0,
                      "Value": 13,
                      "__name__": 1,
                      "dhcp_address": 3,
                      "dhcp_name": 2,
                      "instance": 12,
                      "interface": 11,
                      "job": 5,
                      "mac_address": 4,
                      "routerboard_address": 6,
                      "routerboard_name": 7,
                      "rx_rate": 8,
                      "tx_rate": 9,
                      "uptime": 10
                    },
                    "renameByName": {}
                  }
                }
              ],
              "type": "table"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "decimals": 0,
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "short"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsZero",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsNull",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 12,
                "y": 111
              },
              "id": 37,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "lastNotNull",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "bottom",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "none"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_registered_clients{routerboard_name=\"$node\"}",
                  "interval": "",
                  "legendFormat": "{{channel}}",
                  "range": true,
                  "refId": "A"
                }
              ],
              "title": "Number of clients",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "max": 100,
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "percent"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsNull",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 0,
                "y": 119
              },
              "id": 61,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "none"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_clients_tx_ccq{routerboard_name=\"$node\"}",
                  "instant": false,
                  "interval": "",
                  "legendFormat": "{{dhcp_name}}",
                  "refId": "A"
                }
              ],
              "title": "WLAN Clients Tx CCQ",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "Incoming traffic on interface ether1-gateway"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "#1F78C1",
                          "mode": "fixed"
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "Outgoing traffic on interface ether1-gateway"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "#EAB839",
                          "mode": "fixed"
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Out/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "#EAB839",
                          "mode": "fixed"
                        }
                      },
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byValue",
                      "options": {
                        "op": "gte",
                        "reducer": "allIsZero",
                        "value": 0
                      }
                    },
                    "properties": [
                      {
                        "id": "custom.hideFrom",
                        "value": {
                          "legend": true,
                          "tooltip": true,
                          "viz": false
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 8,
                "w": 12,
                "x": 12,
                "y": 119
              },
              "id": 63,
              "options": {
                "legend": {
                  "calcs": [],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_wlan_clients_tx_bytes_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "In - {{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_wlan_clients_rx_bytes_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Outgoing traffic on interface ether1-gateway"
                  },
                  "legendFormat": "Out - {{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "range": true,
                  "refId": "B"
                }
              ],
              "title": "Clients Traffic",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 0,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "dB"
                },
                "overrides": []
              },
              "gridPos": {
                "h": 7,
                "w": 12,
                "x": 0,
                "y": 127
              },
              "id": 65,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "list",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_clients_signal_strength{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Clients Signal Strength",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 0,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "none"
                },
                "overrides": []
              },
              "gridPos": {
                "h": 7,
                "w": 12,
                "x": 12,
                "y": 127
              },
              "id": 66,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_wlan_clients_signal_to_noise{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Clients  Signal-to-Noise ",
              "type": "timeseries"
            }
          ],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "Wireless",
          "type": "row"
        },
        {
          "collapsed": true,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 103
          },
          "id": 33,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "custom": {
                    "align": "center",
                    "cellOptions": {
                      "type": "auto"
                    },
                    "filterable": false,
                    "inspect": false
                  },
                  "decimals": 2,
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "none"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "board"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 189
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "identity"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 103
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "version"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 110
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 6,
                "w": 6,
                "x": 0,
                "y": 104
              },
              "id": 35,
              "options": {
                "cellHeight": "sm",
                "footer": {
                  "countRows": false,
                  "fields": "",
                  "reducer": [
                    "sum"
                  ],
                  "show": false
                },
                "showHeader": true,
                "sortBy": []
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_capsman_remote_caps_info{routerboard_name=\"$node\"}",
                  "format": "table",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "{{identity}}",
                  "refId": "A"
                }
              ],
              "title": "Remote Caps",
              "transformations": [
                {
                  "id": "organize",
                  "options": {
                    "excludeByName": {
                      "Time": true,
                      "Value": true,
                      "__name__": true,
                      "instance": true,
                      "job": true,
                      "routerboard_address": true,
                      "routerboard_name": true
                    },
                    "indexByName": {
                      "Time": 0,
                      "Value": 10,
                      "__name__": 1,
                      "base_mac": 4,
                      "board": 3,
                      "identity": 2,
                      "instance": 5,
                      "job": 6,
                      "routerboard_address": 7,
                      "routerboard_name": 8,
                      "version": 9
                    },
                    "renameByName": {}
                  }
                }
              ],
              "type": "table"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "fixed"
                  },
                  "custom": {
                    "align": "center",
                    "cellOptions": {
                      "type": "auto"
                    },
                    "filterable": false,
                    "inspect": false
                  },
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  }
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "__name__"
                    },
                    "properties": [
                      {
                        "id": "displayName"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "rx_signal"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 127
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "name"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 267
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "mac_address"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 165
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "ssid"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 140
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 15,
                "w": 18,
                "x": 6,
                "y": 104
              },
              "id": 41,
              "options": {
                "cellHeight": "sm",
                "footer": {
                  "countRows": false,
                  "fields": "",
                  "reducer": [
                    "sum"
                  ],
                  "show": false
                },
                "showHeader": true,
                "sortBy": [
                  {
                    "desc": true,
                    "displayName": "rx_signal"
                  }
                ]
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_capsman_clients_devices_info{routerboard_name=\"$node\"}",
                  "format": "table",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "",
                  "refId": "A"
                }
              ],
              "title": "CAPsMAN Clients",
              "transformations": [
                {
                  "id": "organize",
                  "options": {
                    "excludeByName": {
                      "Time": true,
                      "Value": true,
                      "__name__": true,
                      "instance": true,
                      "job": true,
                      "routerboard_address": true,
                      "routerboard_name": true
                    },
                    "indexByName": {
                      "Time": 0,
                      "Value": 15,
                      "__name__": 1,
                      "dhcp_address": 3,
                      "dhcp_name": 2,
                      "instance": 9,
                      "interface": 10,
                      "job": 12,
                      "mac_address": 4,
                      "routerboard_address": 13,
                      "routerboard_name": 14,
                      "rx_rate": 6,
                      "rx_signal": 5,
                      "ssid": 11,
                      "tx_rate": 7,
                      "uptime": 8
                    },
                    "renameByName": {}
                  }
                }
              ],
              "type": "table"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "decimals": 0,
                  "links": [],
                  "mappings": [],
                  "min": 1,
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "#EAB839",
                        "value": 30
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  }
                },
                "overrides": []
              },
              "gridPos": {
                "h": 7,
                "w": 6,
                "x": 0,
                "y": 110
              },
              "id": 47,
              "options": {
                "displayMode": "lcd",
                "maxVizHeight": 300,
                "minVizHeight": 10,
                "minVizWidth": 0,
                "namePlacement": "auto",
                "orientation": "horizontal",
                "reduceOptions": {
                  "calcs": [
                    "mean"
                  ],
                  "fields": "",
                  "values": false
                },
                "showUnfilled": true,
                "sizing": "auto",
                "text": {},
                "valueMode": "color"
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_capsman_registrations_count{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": true,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ interface }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "sum(mktxp_capsman_registrations_count{routerboard_name=\"$node\"})",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "Total",
                  "refId": "B"
                }
              ],
              "title": "CAPsMAN Registrations",
              "type": "bargauge"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "thresholds"
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "red"
                      },
                      {
                        "color": "orange",
                        "value": -80
                      },
                      {
                        "color": "purple",
                        "value": -70
                      },
                      {
                        "color": "green",
                        "value": -60
                      },
                      {
                        "color": "rgb(20, 104, 9)",
                        "value": -40
                      }
                    ]
                  },
                  "unit": "dB"
                },
                "overrides": []
              },
              "gridPos": {
                "h": 11,
                "w": 6,
                "x": 0,
                "y": 117
              },
              "id": 48,
              "options": {
                "displayMode": "gradient",
                "maxVizHeight": 300,
                "minVizHeight": 10,
                "minVizWidth": 0,
                "namePlacement": "auto",
                "orientation": "horizontal",
                "reduceOptions": {
                  "calcs": [
                    "lastNotNull"
                  ],
                  "fields": "",
                  "values": false
                },
                "showUnfilled": true,
                "sizing": "auto",
                "text": {},
                "valueMode": "color"
              },
              "pluginVersion": "10.0.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_capsman_clients_signal_strength{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": true,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Registered Client Signal Strength",
              "type": "bargauge"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 0,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": false,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "max": -16,
                  "min": -80,
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "dB"
                },
                "overrides": []
              },
              "gridPos": {
                "h": 9,
                "w": 18,
                "x": 6,
                "y": 119
              },
              "id": 49,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "10.4.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_capsman_clients_signal_strength{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "CAPsMan Clients Signal Strength",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Out/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "#EAB839",
                          "mode": "fixed"
                        }
                      },
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/In/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "green",
                          "mode": "fixed"
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 10,
                "w": 24,
                "x": 0,
                "y": 128
              },
              "id": 39,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.3.2",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_capsman_clients_tx_bytes_total{routerboard_name=\"$node\"}[4m])*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "In | {{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_capsman_clients_rx_bytes_total{routerboard_name=\"$node\"}[4m])*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Outgoing traffic on interface ether1-gateway"
                  },
                  "legendFormat": "Out | {{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "range": true,
                  "refId": "B"
                }
              ],
              "title": "CAPsMAN Clients Traffic",
              "type": "timeseries"
            }
          ],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "CAPsMAN",
          "type": "row"
        },
        {
          "collapsed": true,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 104
          },
          "id": 109,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 0,
                "y": 105
              },
              "id": 107,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_simple_rates_download_total{routerboard_name=\"$node\"}*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Download",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_simple_rates_upload_total{routerboard_name=\"$node\"}*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Upload",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "B"
                }
              ],
              "title": "Simple Queue Rates",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "decbytes"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 12,
                "y": 105
              },
              "id": 102,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_simple_bytes_download_total{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Download",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_simple_bytes_upload_total{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Upload",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "B"
                }
              ],
              "title": "Simple Queue Processed Bytes",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "Bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 0,
                "y": 116
              },
              "id": 111,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_simple_queued_bytes_upload_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Download",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_simple_queued_bytes_upload_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Upload",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "B"
                }
              ],
              "title": "Simple Queue Queued Bytes",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "Bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 12,
                "y": 116
              },
              "id": 112,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_simple_dropped_download_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Download",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_simple_dropped_upload_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }} Upload",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "B"
                }
              ],
              "title": "Simple Queue Dropped Bytes",
              "type": "timeseries"
            }
          ],
          "title": "Simple Queue",
          "type": "row"
        },
        {
          "collapsed": true,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 105
          },
          "id": 100,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 0,
                "y": 106
              },
              "id": 101,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_tree_rates_total{routerboard_name=\"$node\"}*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Queue Tree Rates",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "decbytes"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 12,
                "y": 106
              },
              "id": 110,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_queue_tree_bytes_total{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Queue Tree Processed Bytes",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "Bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 0,
                "y": 117
              },
              "id": 106,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_tree_queued_bytes_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Queue Tree Queued Bytes",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "Bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Upload/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 11,
                "w": 12,
                "x": 12,
                "y": 117
              },
              "id": 105,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_queue_tree_dropped_total{routerboard_name=\"$node\"}[4m])",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Queue Tree Dropped Bytes",
              "type": "timeseries"
            }
          ],
          "title": "Queue Tree",
          "type": "row"
        },
        {
          "collapsed": true,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 106
          },
          "id": 122,
          "panels": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "fixed"
                  },
                  "custom": {
                    "align": "center",
                    "cellOptions": {
                      "type": "auto"
                    },
                    "filterable": false,
                    "inspect": false
                  },
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  }
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "__name__"
                    },
                    "properties": [
                      {
                        "id": "displayName"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "rx_signal"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 127
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "name"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 267
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "mac_address"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 165
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "ssid"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 140
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "IP Address"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 325
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byName",
                      "options": "Name"
                    },
                    "properties": [
                      {
                        "id": "custom.width",
                        "value": 344
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 13,
                "w": 12,
                "x": 0,
                "y": 107
              },
              "id": 121,
              "options": {
                "cellHeight": "sm",
                "footer": {
                  "countRows": false,
                  "fields": "",
                  "reducer": [
                    "sum"
                  ],
                  "show": false
                },
                "showHeader": true,
                "sortBy": [
                  {
                    "desc": false,
                    "displayName": "User"
                  }
                ]
              },
              "pluginVersion": "11.1.4",
              "targets": [
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_kid_control_device_info{routerboard_name=\"$node\"}",
                  "format": "table",
                  "instant": true,
                  "interval": "",
                  "legendFormat": "",
                  "refId": "A"
                }
              ],
              "title": "Connected Devices",
              "transformations": [
                {
                  "id": "organize",
                  "options": {
                    "excludeByName": {
                      "Time": true,
                      "Value": true,
                      "__name__": true,
                      "disabled": true,
                      "instance": true,
                      "job": true,
                      "name": false,
                      "routerboard_address": true,
                      "routerboard_name": true
                    },
                    "includeByName": {},
                    "indexByName": {
                      "Time": 0,
                      "Value": 11,
                      "__name__": 1,
                      "dhcp_name": 2,
                      "disabled": 12,
                      "instance": 7,
                      "ip_address": 5,
                      "job": 8,
                      "mac_address": 4,
                      "name": 3,
                      "routerboard_address": 9,
                      "routerboard_name": 10,
                      "user": 6
                    },
                    "renameByName": {
                      "dhcp_name": "DHCP Name",
                      "ip_address": "IP Address",
                      "mac_address": "Mac Address",
                      "name": "Name",
                      "user": "User"
                    }
                  }
                }
              ],
              "type": "table"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisBorderShow": false,
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "insertNulls": false,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "Bps"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Up/"
                    },
                    "properties": [
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      },
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "yellow",
                          "mode": "fixed"
                        }
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Down/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "light-green",
                          "mode": "fixed"
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 13,
                "w": 12,
                "x": 12,
                "y": 107
              },
              "id": 124,
              "options": {
                "legend": {
                  "calcs": [
                    "mean",
                    "max",
                    "min"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.2.5",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_kid_control_device_rate_down{routerboard_name=\"$node\"}*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "Down | {{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_kid_control_device_rate_up{routerboard_name=\"$node\"}*8",
                  "hide": false,
                  "instant": false,
                  "legendFormat": "Up | {{ dhcp_name }}",
                  "range": true,
                  "refId": "B"
                }
              ],
              "title": "Transfer Rates",
              "type": "timeseries"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "description": "",
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "thresholds"
                  },
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "dark-orange"
                      },
                      {
                        "color": "semi-dark-yellow",
                        "value": 0
                      },
                      {
                        "color": "yellow",
                        "value": 10
                      },
                      {
                        "color": "super-light-yellow",
                        "value": 20
                      },
                      {
                        "color": "super-light-green",
                        "value": 40
                      },
                      {
                        "color": "light-green",
                        "value": 60
                      },
                      {
                        "color": "green",
                        "value": 80
                      },
                      {
                        "color": "super-light-blue",
                        "value": 100
                      },
                      {
                        "color": "light-blue",
                        "value": 120
                      },
                      {
                        "color": "blue",
                        "value": 140
                      }
                    ]
                  },
                  "unit": "s"
                },
                "overrides": []
              },
              "gridPos": {
                "h": 13,
                "w": 12,
                "x": 0,
                "y": 120
              },
              "id": 125,
              "options": {
                "displayMode": "gradient",
                "maxVizHeight": 300,
                "minVizHeight": 16,
                "minVizWidth": 8,
                "namePlacement": "auto",
                "orientation": "horizontal",
                "reduceOptions": {
                  "calcs": [
                    "lastNotNull"
                  ],
                  "fields": "",
                  "values": false
                },
                "showUnfilled": true,
                "sizing": "auto",
                "valueMode": "text"
              },
              "pluginVersion": "10.0.1",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "mktxp_kid_control_device_idle_time{routerboard_name=\"$node\"}",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "{{ dhcp_name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                }
              ],
              "title": "Idle Times",
              "type": "bargauge"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "fieldConfig": {
                "defaults": {
                  "color": {
                    "mode": "palette-classic"
                  },
                  "custom": {
                    "axisCenteredZero": false,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 30,
                    "gradientMode": "none",
                    "hideFrom": {
                      "legend": false,
                      "tooltip": false,
                      "viz": false
                    },
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                      "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": true,
                    "stacking": {
                      "group": "A",
                      "mode": "none"
                    },
                    "thresholdsStyle": {
                      "mode": "off"
                    }
                  },
                  "links": [],
                  "mappings": [],
                  "thresholds": {
                    "mode": "absolute",
                    "steps": [
                      {
                        "color": "green"
                      },
                      {
                        "color": "red",
                        "value": 80
                      }
                    ]
                  },
                  "unit": "decbytes"
                },
                "overrides": [
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/Out/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "#EAB839",
                          "mode": "fixed"
                        }
                      },
                      {
                        "id": "custom.transform",
                        "value": "negative-Y"
                      }
                    ]
                  },
                  {
                    "matcher": {
                      "id": "byRegexp",
                      "options": "/In/"
                    },
                    "properties": [
                      {
                        "id": "color",
                        "value": {
                          "fixedColor": "green",
                          "mode": "fixed"
                        }
                      }
                    ]
                  }
                ]
              },
              "gridPos": {
                "h": 13,
                "w": 12,
                "x": 12,
                "y": 120
              },
              "id": 123,
              "options": {
                "legend": {
                  "calcs": [
                    "mean"
                  ],
                  "displayMode": "table",
                  "placement": "right",
                  "showLegend": true,
                  "sortBy": "Mean",
                  "sortDesc": true
                },
                "tooltip": {
                  "maxHeight": 600,
                  "mode": "multi",
                  "sort": "desc"
                }
              },
              "pluginVersion": "9.3.2",
              "targets": [
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_kid_control_device_bytes_down_total{routerboard_name=\"$node\"}[4m])*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "instant": false,
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Incoming traffic on interface ether1-gateway"
                  },
                  "legendFormat": "In | {{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "refId": "A"
                },
                {
                  "application": {
                    "filter": "Network"
                  },
                  "datasource": {
                    "type": "prometheus",
                    "uid": "${datasource}"
                  },
                  "editorMode": "code",
                  "expr": "rate(mktxp_kid_control_device_bytes_up_total{routerboard_name=\"$node\"}[4m])*8",
                  "format": "time_series",
                  "functions": [],
                  "group": {
                    "filter": "Network"
                  },
                  "hide": false,
                  "host": {
                    "filter": "MikroTik Router"
                  },
                  "interval": "",
                  "intervalFactor": 1,
                  "item": {
                    "filter": "Outgoing traffic on interface ether1-gateway"
                  },
                  "legendFormat": "Out | {{ name }}",
                  "mode": 0,
                  "options": {
                    "showDisabledItems": false
                  },
                  "range": true,
                  "refId": "B"
                }
              ],
              "title": "Data Transfers",
              "type": "timeseries"
            }
          ],
          "title": "Kid Control Devices",
          "type": "row"
        },
        {
          "collapsed": false,
          "datasource": {
            "type": "prometheus",
            "uid": "E1M7U50Gz"
          },
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 107
          },
          "id": 80,
          "panels": [],
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "E1M7U50Gz"
              },
              "refId": "A"
            }
          ],
          "title": "MKTXP Metrics",
          "type": "row"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 10
                  },
                  {
                    "color": "purple",
                    "value": 20
                  },
                  {
                    "color": "orange",
                    "value": 50
                  }
                ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 6,
            "x": 0,
            "y": 108
          },
          "id": 78,
          "options": {
            "displayMode": "gradient",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.1.4",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_collection_time_total{routerboard_name=\"$node\"}[4m])  ",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "MKTXP Collection Times",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 18,
            "x": 6,
            "y": 108
          },
          "id": 77,
          "options": {
            "legend": {
              "calcs": [
                "mean"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_collection_time_total{routerboard_name=\"$node\"}[4m])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "editorMode": "code",
              "expr": "sum(rate(mktxp_collection_time_total{routerboard_name=\"$node\"}[4m]))",
              "interval": "",
              "legendFormat": "Total",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "MKTXP Collection Times",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 116
          },
          "id": 27,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "expr": "mktxp_internet_bandwidth",
              "instant": false,
              "interval": "",
              "legendFormat": "{{direction}}",
              "refId": "A"
            }
          ],
          "title": "Internet Bandwidth",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 116
          },
          "id": 74,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "maxHeight": 600,
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.3.2",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${datasource}"
              },
              "expr": "mktxp_internet_latency",
              "instant": false,
              "interval": "",
              "legendFormat": "latency",
              "refId": "A"
            }
          ],
          "title": "Internet Latency",
          "type": "timeseries"
        }
      ],
      "refresh": "10s",
      "schemaVersion": 39,
      "tags": [
        "mikrotik",
        "mktxp"
      ],
      "templating": {
        "list": [
          {
            "current": {
              "selected": false,
              "text": "victoriametrics",
              "value": "ae68gzhsxi60wd"
            },
            "hide": 0,
            "includeAll": false,
            "label": "datasource",
            "multi": false,
            "name": "datasource",
            "options": [],
            "query": "prometheus",
            "queryValue": "",
            "refresh": 1,
            "regex": "",
            "skipUrlSync": false,
            "type": "datasource"
          },
          {
            "current": {
              "selected": false,
              "text": "gw1-home-lab",
              "value": "gw1-home-lab"
            },
            "datasource": {
              "type": "prometheus",
              "uid": "${datasource}"
            },
            "definition": "label_values(mktxp_system_identity_info, routerboard_name)",
            "hide": 0,
            "includeAll": false,
            "label": "Routerboard",
            "multi": false,
            "name": "node",
            "options": [],
            "query": {
              "query": "label_values(mktxp_system_identity_info, routerboard_name)",
              "refId": "StandardVariableQuery"
            },
            "refresh": 2,
            "regex": "",
            "skipUrlSync": false,
            "sort": 1,
            "tagValuesQuery": "",
            "tagsQuery": "",
            "type": "query",
            "useTags": false
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "PBFA97CFB590B2093"
            },
            "filters": [],
            "hide": 0,
            "name": "Filters",
            "skipUrlSync": false,
            "type": "adhoc"
          }
        ]
      },
      "time": {
        "from": "now-12h",
        "to": "now"
      },
      "timepicker": {},
      "timezone": "",
      "title": "Mikrotik MKTXP Exporter Overview",
      "uid": "mikrotik-mktxp-exporter",
      "version": 1,
      "weekStart": ""
    }
================================================

File: helm-release.yaml
================================================
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: prometheus-mikrotik-exporter
  namespace: monitoring
  labels:
    app: prometheus-mikrotik-exporter
    stream: sre
    owner: sre
    env: home-lab
    product: observability
    temporary: "false"
    deleteAfter: "false"
spec:
  chart:
    spec:
      chart: prometheus-mikrotik-exporter
      sourceRef:
        kind: HelmRepository
        name: prometheus-mikrotik-exporter
        namespace: flux-system
      version: "0.4.0"
  releaseName: prometheus-mikrotik-exporter
  interval: 5m
  timeout: 3m
  maxHistory: 1
  install:
    remediation:
      retries: 3
  upgrade:
    remediation:
      retries: 3
  values:
    replicaCount: 1
    image:
      repository: ghcr.io/akpw/mktxp
      pullPolicy: IfNotPresent
      tag: "stable-20240603114403"
    imagePullSecrets:
      - name: deploy-secret
    nameOverride: ""
    fullnameOverride: ""
    serviceAccount:
      create: true
      automount: true
      annotations: {}
      name: ""
    serviceMonitor:
      enabled: true
      annotations: {}
      additionalLabels: {}
      interval: 30s
      scrapeTimeout: ""
    podAnnotations: {}
    podLabels:
      app: prometheus-mikrotik-exporter
      stream: sre
      owner: sre
      env: home-lab
      product: observability
      temporary: "false"
      deleteAfter: "false"
    podSecurityContext:
      {}
    securityContext:
      {}
    service:
      type: ClusterIP
      port: 49090
    resources: {}
      # requests:
      #   cpu: 250m
      #   memory: 512Mi
      # limits:
      #   cpu: 250m
      #   memory: 512Mi
    nodeSelector: {}
    tolerations: []
    affinity: {}
    annotations: {}
    config:
      # mktxp
      router:
        existingSecret: ""
        existingSecretKey: config
        value: |
          ## Source: https://github.com/akpw/mktxp/blob/main/mktxp/cli/config/mktxp.conf
          [gw1-home-lab]
              enabled = True                  # turns metrics collection for this RouterOS device on / off
              hostname = 192.168.30.1         # RouterOS IP address
              port = 8728                     # RouterOS IP Port
              username = scrapper             # RouterOS user, needs to have 'read' and 'api' permissions
              password = scrapper             # RouterOS password
              use_ssl = False                 # enables connection via API-SSL servis
              no_ssl_certificate = False      # enables API_SSL connect without router SSL certificate
              ssl_certificate_verify = False  # turns SSL certificate verification on / off
              installed_packages = True       # Installed packages
              dhcp = True                     # DHCP general metrics
              dhcp_lease = True               # DHCP lease metrics
              connections = True              # IP connections metrics
              connection_stats = True         # Open IP connections metrics
              pool = True                     # Pool metrics
              interface = True                # Interfaces traffic metrics
              firewall = True                 # IPv4 Firewall rules traffic metrics
              ipv6_firewall = False           # IPv6 Firewall rules traffic metrics
              ipv6_neighbor = False           # Reachable IPv6 Neighbors
              poe = False                     # POE metrics
              monitor = True                  # Interface monitor metrics
              netwatch = True                 # Netwatch metrics
              public_ip = True                # Public IP metrics
              route = True                    # Routes metrics
              wireless = False                # WLAN general metrics
              wireless_clients = False        # WLAN clients metrics
              capsman = False                 # CAPsMAN general metrics
              capsman_clients = False         # CAPsMAN clients metrics
              kid_control_devices = False     # Kid Control metrics
              user = True                     # Active Users metrics
              queue = True                    # Queues metrics
              remote_dhcp_entry = None        # An MKTXP entry for remote DHCP info resolution (capsman/wireless)
              use_comments_over_names = True  # when available, forces using comments over the interfaces names
              check_for_updates = False       # check for available ROS updates
          [default]
              use_comments_over_names = True
              ssl_certificate_verify = False
              netwatch = True
              dhcp_lease = True
              route = True
              check_for_updates = False
              dhcp = True
              queue = True
              ipv6_route = False
              no_ssl_certificate = False
              neighbor = False
              use_ssl = False
              kid_control_dynamic = False
              capsman = False
              wireless_clients = False
              interface = True
              poe = False
              enabled = True
              firewall = True
              pool = True
              connection_stats = True
              installed_packages = True
              ipv6_pool = False
              capsman_clients = False
              public_ip = True
              plaintext_login = True
              kid_control_assigned = False
              bgp = False
              user = True
              ipv6_neighbor = False
              monitor = True
              connections = True
              wireless = False
              ipv6_firewall = False
              username = scrapper
              password = scrapper
              remote_dhcp_entry = None
              remote_capsman_entry = None
              port = 8728
      # _mktxp
      scrapper:
        existingSecret: ""
        existingSecretKey: config
        value: |
          ## Source: https://github.com/akpw/mktxp/blob/main/mktxp/cli/config/_mktxp.conf
          [MKTXP]
              port = 49090
              socket_timeout = 2
              initial_delay_on_failure = 120
              max_delay_on_failure = 900
              delay_inc_div = 5
              bandwidth = True                    # Turns metrics bandwidth metrics collection on / off
              bandwidth_test_interval = 600       # Interval for colllecting bandwidth metrics
              minimal_collect_interval = 30       # Minimal metric collection interval
              verbose_mode = True                 # Set it on for troubleshooting
              fetch_routers_in_parallel = True    # Set to True if you want to fetch multiple routers parallel
              max_worker_threads = 5              # Max number of worker threads that can fetch routers (parallel fetch only)
              max_scrape_duration = 10            # Max duration of individual routers' metrics collection (parallel fetch only)
              total_max_scrape_duration = 30      # Max overall duration of all metrics collection (parallel fetch only)
================================================

File: source.yaml
================================================
---
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: HelmRepository
metadata:
  name: prometheus-mikrotik-exporter
  namespace: flux-system
  labels:
    app: prometheus-mikrotik-exporter
    stream: sre
    env: home-lab
    owner: sre
    product: observability
    temporary: "false"
    deleteAfter: "false"
spec:
  interval: 24h
  url: https://helm.vrs-factory.dev
================================================

File: ip_dhcp_server_network.tf
================================================
resource "routeros_ip_dhcp_server_network" "bridge_lan" {
  comment    = "bridge_lan default"
  address    = "192.168.88.0/24"
  gateway    = "192.168.88.1"
  dns_server = ["192.168.88.1"]
  netmask    = 0
}
resource "routeros_ip_dhcp_server_network" "vlan10" {
  comment    = "vlan10 management"
  address    = "192.168.10.0/24"
  gateway    = "192.168.10.1"
  dns_server = ["192.168.10.1"]
  netmask    = 0
}
resource "routeros_ip_dhcp_server_network" "vlan20" {
  comment    = "vlan20 wifi&lan"
  address    = "192.168.20.0/24"
  gateway    = "192.168.20.1"
  dns_server = ["192.168.20.1"]
  netmask    = 0
}
resource "routeros_ip_dhcp_server_network" "vlan30" {
  comment    = "vlan30 servers"
  address    = "192.168.30.0/24"
  gateway    = "192.168.30.1"
  dns_server = ["192.168.30.1"]
  netmask    = 0
}
================================================

File: README.md
================================================
# Terraform provisioning of homelab MikroTik.
## VLANs:
| VLAN Number | Network              | Description            |
|-------------|----------------------|------------------------|
| 1           | 192.168.1.0/24       | default VLAN           |
| 5           | 192.168.5.0/24       | openvpn VLAN           |
| 10          | 192.168.10.0/24      | management VLAN        |
| 20          | 192.168.20.0/24      | wifi&lan VLAN          |
| 30          | 192.168.30.0/24      | servers VLAN           |
| 100-200     | 192.168.100-200.0/24 | guest VLAN             |
## How to openvpn:
  - Create routeros_system_certificate for user.
  - Create routeros_ppp_secret resource for user.
  - Create routeros_interface_ovpn_server for user.
## Useful commands:
```
openssl ec -in ovpn.key -outform PEM -out ovpn.pem
```
================================================