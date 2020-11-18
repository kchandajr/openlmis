import urllib

#components
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-fulfillment/v8.2.0/README.md", "components/fulfillmentService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-requisition/v8.3.1/README.md", "components/requisitionService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-auth/v4.3.1/README.md", "components/authService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-auth/v4.3.1/DESIGN.md", "components/authServiceDesign.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-cce/v1.3.0/README.md", "components/cceService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-notification/v4.3.1/README.md", "components/notificationService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-referencedata/v15.2.0/README.md", "components/referencedataService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-stockmanagement/v5.1.2/README.md", "components/stockmanagementService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-report/v1.2.1/README.md", "components/reportService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-hapifhir/v2.0.0/README.md", "components/hapifhirService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-diagnostics/v1.1.0/README.md", "components/diagnosticsService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-template-service/v3.7.0/README.md", "components/templateServiceService.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-reference-ui/v5.1.9/README.md", "components/referenceUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-auth-ui/v6.2.5/README.md", "components/authUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-cce-ui/v1.0.8/README.md", "components/cceUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-referencedata-ui/v5.6.4/README.md", "components/referencedataUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-report-ui/v5.2.5/README.md", "components/reportUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-requisition-ui/v7.0.4/README.md", "components/requisitionUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-fulfillment-ui/v6.0.8/README.md", "components/fulfillmentUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-stockmanagement-ui/v2.0.8/README.md", "components/stockmanagementUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/dev-ui/v9.0.1/README.md", "components/devUI.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/README.md", "components/uiComponents.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/index.md", "components/uiOverview.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/extension_guide.md", "components/uiExtensionGuide.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-layout/v5.1.8/README.md", "components/uiLayout.md")

#conventions
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-template-service/v3.7.0/STYLE-GUIDE.md", "conventions/codeStyleguide.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-template-service/v3.7.0/TESTING.md", "conventions/testing.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-template-service/v3.7.0/ERROR_HANDLING.md", "conventions/errorHandling.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-template-service/v3.7.0/LICENSE-HEADER.md", "conventions/licenseHeader.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/conventions.md", "conventions/uiConventions.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/conventions-angularjs.md", "conventions/uiAngularjs.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/conventions-javascript.md", "conventions/uiJavascript.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/conventions-markup.md", "conventions/uiMarkup.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/conventions-testing.md", "conventions/uiTesting.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/information-architecture.md", "conventions/uiInformationArchitecture.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-ui-components/v7.2.4/docs/performance.md", "conventions/uiPerformance.md")

# deployment
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/deploymentTopology.md", "deployment/topology.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/provision/Provision-single-host.md", "deployment/provisionSingleHost.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/provision/Provision-swarm-With-ELB.md", "deployment/provisionSwarmWithELB.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/provision/Provision-swarm-With-Elastic-ip.md", "deployment/provisionSwarmWithElasticIp.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/provision/RDS-configuration.md", "deployment/rdsConfiguration.md")
urllib.urlretrieve("https://raw.githubusercontent.com/OpenLMIS/openlmis-deployment/v3.10.0/deployment/README.md", "deployment/demoAndCiJenkins.md")
