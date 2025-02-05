# Repository Information
Name: MikroTik-Demo

# Directory Structure
Directory structure:
└── github_repos/MikroTik-Demo/
    ├── .editorconfig
    │   ├── config
    │   ├── description
    │   ├── HEAD
    │   ├── hooks/
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   ├── push-to-checkout.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info/
    │   │   └── exclude
    │   ├── logs/
    │   │   ├── HEAD
    │   │   └── refs/
    │   │       ├── heads/
    │   │       │   └── master
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-9a403d947241a079bb858e40d9268e59cbcd1f38.idx
    │   │       └── pack-9a403d947241a079bb858e40d9268e59cbcd1f38.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── azure-pipelines.yml
    ├── Directory.Build.props
    ├── MikroTik.EntityBuilder/
    │   ├── Generated/
    │   │   ├── GeneratedExtensions.cs
    │   │   ├── ViewModels/
    │   │   │   ├── AccountingSnapshotDetailPageViewModel.cs
    │   │   │   ├── AccountingSnapshotPageViewModel.cs
    │   │   │   ├── AccountingUncountedDetailPageViewModel.cs
    │   │   │   ├── AccountingUncountedPageViewModel.cs
    │   │   │   ├── AccountingWebAccessDetailPageViewModel.cs
    │   │   │   ├── AccountingWebAccessPageViewModel.cs
    │   │   │   ├── BgpAdvertisementsDetailPageViewModel.cs
    │   │   │   ├── BgpAdvertisementsPageViewModel.cs
    │   │   │   ├── BgpInstanceDetailPageViewModel.cs
    │   │   │   ├── BgpInstancePageViewModel.cs
    │   │   │   ├── BgpNetworkDetailPageViewModel.cs
    │   │   │   ├── BgpNetworkPageViewModel.cs
    │   │   │   ├── BgpPeerDetailPageViewModel.cs
    │   │   │   ├── BgpPeerPageViewModel.cs
    │   │   │   ├── BridgeFilterDetailPageViewModel.cs
    │   │   │   ├── BridgeFilterPageViewModel.cs
    │   │   │   ├── BridgeNatDetailPageViewModel.cs
    │   │   │   ├── BridgeNatPageViewModel.cs
    │   │   │   ├── BridgePortDetailPageViewModel.cs
    │   │   │   ├── BridgePortPageViewModel.cs
    │   │   │   ├── BridgeSettingsDetailPageViewModel.cs
    │   │   │   ├── BridgeSettingsPageViewModel.cs
    │   │   │   ├── CapsManRegistrationTableDetailPageViewModel.cs
    │   │   │   ├── CapsManRegistrationTablePageViewModel.cs
    │   │   │   ├── ConnectionTrackingDetailPageViewModel.cs
    │   │   │   ├── ConnectionTrackingPageViewModel.cs
    │   │   │   ├── DhcpServerAlertDetailPageViewModel.cs
    │   │   │   ├── DhcpServerAlertPageViewModel.cs
    │   │   │   ├── DhcpServerConfigDetailPageViewModel.cs
    │   │   │   ├── DhcpServerConfigPageViewModel.cs
    │   │   │   ├── DhcpServerLeaseDetailPageViewModel.cs
    │   │   │   ├── DhcpServerLeasePageViewModel.cs
    │   │   │   ├── DhcpServerNetworkDetailPageViewModel.cs
    │   │   │   ├── DhcpServerNetworkPageViewModel.cs
    │   │   │   ├── DhcpServerOptionDetailPageViewModel.cs
    │   │   │   ├── DhcpServerOptionPageViewModel.cs
    │   │   │   ├── DnsCacheAllDetailPageViewModel.cs
    │   │   │   ├── DnsCacheAllPageViewModel.cs
    │   │   │   ├── DnsCacheDetailPageViewModel.cs
    │   │   │   ├── DnsCachePageViewModel.cs
    │   │   │   ├── DnsStaticDetailPageViewModel.cs
    │   │   │   ├── DnsStaticPageViewModel.cs
    │   │   │   ├── EthernetMonitorDetailPageViewModel.cs
    │   │   │   ├── EthernetMonitorPageViewModel.cs
    │   │   │   ├── FirewallAddressListDetailPageViewModel.cs
    │   │   │   ├── FirewallAddressListPageViewModel.cs
    │   │   │   ├── FirewallConnectionDetailPageViewModel.cs
    │   │   │   ├── FirewallConnectionPageViewModel.cs
    │   │   │   ├── FirewallFilterDetailPageViewModel.cs
    │   │   │   ├── FirewallFilterPageViewModel.cs
    │   │   │   ├── FirewallMangleDetailPageViewModel.cs
    │   │   │   ├── FirewallManglePageViewModel.cs
    │   │   │   ├── FirewallNatDetailPageViewModel.cs
    │   │   │   ├── FirewallNatPageViewModel.cs
    │   │   │   ├── FirewalServicePortDetailPageViewModel.cs
    │   │   │   ├── FirewalServicePortPageViewModel.cs
    │   │   │   ├── HotspotActiveDetailPageViewModel.cs
    │   │   │   ├── HotspotActivePageViewModel.cs
    │   │   │   ├── HotspotIpBindingDetailPageViewModel.cs
    │   │   │   ├── HotspotIpBindingPageViewModel.cs
    │   │   │   ├── HotspotUserDetailPageViewModel.cs
    │   │   │   ├── HotspotUserPageViewModel.cs
    │   │   │   ├── HotspotUserProfileDetailPageViewModel.cs
    │   │   │   ├── HotspotUserProfilePageViewModel.cs
    │   │   │   ├── InterfaceBridgeDetailPageViewModel.cs
    │   │   │   ├── InterfaceBridgePageViewModel.cs
    │   │   │   ├── InterfaceDetailPageViewModel.cs
    │   │   │   ├── InterfaceEthernetDetailPageViewModel.cs
    │   │   │   ├── InterfaceEthernetPageViewModel.cs
    │   │   │   ├── InterfaceMonitorTrafficDetailPageViewModel.cs
    │   │   │   ├── InterfaceMonitorTrafficPageViewModel.cs
    │   │   │   ├── InterfacePageViewModel.cs
    │   │   │   ├── InterfaceWirelessDetailPageViewModel.cs
    │   │   │   ├── InterfaceWirelessPageViewModel.cs
    │   │   │   ├── IpAccountingDetailPageViewModel.cs
    │   │   │   ├── IpAccountingPageViewModel.cs
    │   │   │   ├── IpAddressDetailPageViewModel.cs
    │   │   │   ├── IpAddressPageViewModel.cs
    │   │   │   ├── IpArpDetailPageViewModel.cs
    │   │   │   ├── IpArpPageViewModel.cs
    │   │   │   ├── IpDhcpClientDetailPageViewModel.cs
    │   │   │   ├── IpDhcpClientPageViewModel.cs
    │   │   │   ├── IpDhcpRelayDetailPageViewModel.cs
    │   │   │   ├── IpDhcpRelayPageViewModel.cs
    │   │   │   ├── IpDhcpServerDetailPageViewModel.cs
    │   │   │   ├── IpDhcpServerPageViewModel.cs
    │   │   │   ├── IpDnsDetailPageViewModel.cs
    │   │   │   ├── IpDnsPageViewModel.cs
    │   │   │   ├── IpPoolDetailPageViewModel.cs
    │   │   │   ├── IpPoolPageViewModel.cs
    │   │   │   ├── IpRouteDetailPageViewModel.cs
    │   │   │   ├── IpRoutePageViewModel.cs
    │   │   │   ├── LogDetailPageViewModel.cs
    │   │   │   ├── LogPageViewModel.cs
    │   │   │   ├── PppAaaDetailPageViewModel.cs
    │   │   │   ├── PppAaaPageViewModel.cs
    │   │   │   ├── PppActiveDetailPageViewModel.cs
    │   │   │   ├── PppActivePageViewModel.cs
    │   │   │   ├── PppProfileDetailPageViewModel.cs
    │   │   │   ├── PppProfilePageViewModel.cs
    │   │   │   ├── PppSecretDetailPageViewModel.cs
    │   │   │   ├── PppSecretPageViewModel.cs
    │   │   │   ├── QueueSimpleDetailPageViewModel.cs
    │   │   │   ├── QueueSimplePageViewModel.cs
    │   │   │   ├── QueueTreeDetailPageViewModel.cs
    │   │   │   ├── QueueTreePageViewModel.cs
    │   │   │   ├── QueueTypeDetailPageViewModel.cs
    │   │   │   ├── QueueTypePageViewModel.cs
    │   │   │   ├── SystemIdentityDetailPageViewModel.cs
    │   │   │   ├── SystemIdentityPageViewModel.cs
    │   │   │   ├── SystemResourceDetailPageViewModel.cs
    │   │   │   ├── SystemResourcePageViewModel.cs
    │   │   │   ├── SystemRouterboardDetailPageViewModel.cs
    │   │   │   ├── SystemRouterboardPageViewModel.cs
    │   │   │   ├── ToolPingDetailPageViewModel.cs
    │   │   │   ├── ToolPingPageViewModel.cs
    │   │   │   ├── ToolTorchDetailPageViewModel.cs
    │   │   │   ├── ToolTorchPageViewModel.cs
    │   │   │   ├── ToolTracerouteDetailPageViewModel.cs
    │   │   │   ├── ToolTraceroutePageViewModel.cs
    │   │   │   ├── UserDetailPageViewModel.cs
    │   │   │   ├── UserGroupDetailPageViewModel.cs
    │   │   │   ├── UserGroupPageViewModel.cs
    │   │   │   ├── UserPageViewModel.cs
    │   │   │   ├── WirelessAccessListDetailPageViewModel.cs
    │   │   │   ├── WirelessAccessListPageViewModel.cs
    │   │   │   ├── WirelessChannelsDetailPageViewModel.cs
    │   │   │   ├── WirelessChannelsPageViewModel.cs
    │   │   │   ├── WirelessRegistrationTableDetailPageViewModel.cs
    │   │   │   ├── WirelessRegistrationTablePageViewModel.cs
    │   │   │   ├── WirelessSecurityProfileDetailPageViewModel.cs
    │   │   │   ├── WirelessSecurityProfilePageViewModel.cs
    │   │   │   ├── WirelessSnifferDetailPageViewModel.cs
    │   │   │   └── WirelessSnifferPageViewModel.cs
    │   │   └── Views/
    │   │       ├── AccountingSnapshotDetailPage.xaml
    │   │       ├── AccountingSnapshotDetailPage.xaml.cs
    │   │       ├── AccountingSnapshotPage.xaml
    │   │       ├── AccountingSnapshotPage.xaml.cs
    │   │       ├── AccountingUncountedDetailPage.xaml
    │   │       ├── AccountingUncountedDetailPage.xaml.cs
    │   │       ├── AccountingUncountedPage.xaml
    │   │       ├── AccountingUncountedPage.xaml.cs
    │   │       ├── AccountingWebAccessDetailPage.xaml
    │   │       ├── AccountingWebAccessDetailPage.xaml.cs
    │   │       ├── AccountingWebAccessPage.xaml
    │   │       ├── AccountingWebAccessPage.xaml.cs
    │   │       ├── BgpAdvertisementsDetailPage.xaml
    │   │       ├── BgpAdvertisementsDetailPage.xaml.cs
    │   │       ├── BgpAdvertisementsPage.xaml
    │   │       ├── BgpAdvertisementsPage.xaml.cs
    │   │       ├── BgpInstanceDetailPage.xaml
    │   │       ├── BgpInstanceDetailPage.xaml.cs
    │   │       ├── BgpInstancePage.xaml
    │   │       ├── BgpInstancePage.xaml.cs
    │   │       ├── BgpNetworkDetailPage.xaml
    │   │       ├── BgpNetworkDetailPage.xaml.cs
    │   │       ├── BgpNetworkPage.xaml
    │   │       ├── BgpNetworkPage.xaml.cs
    │   │       ├── BgpPeerDetailPage.xaml
    │   │       ├── BgpPeerDetailPage.xaml.cs
    │   │       ├── BgpPeerPage.xaml
    │   │       ├── BgpPeerPage.xaml.cs
    │   │       ├── BridgeFilterDetailPage.xaml
    │   │       ├── BridgeFilterDetailPage.xaml.cs
    │   │       ├── BridgeFilterPage.xaml
    │   │       ├── BridgeFilterPage.xaml.cs
    │   │       ├── BridgeNatDetailPage.xaml
    │   │       ├── BridgeNatDetailPage.xaml.cs
    │   │       ├── BridgeNatPage.xaml
    │   │       ├── BridgeNatPage.xaml.cs
    │   │       ├── BridgePortDetailPage.xaml
    │   │       ├── BridgePortDetailPage.xaml.cs
    │   │       ├── BridgePortPage.xaml
    │   │       ├── BridgePortPage.xaml.cs
    │   │       ├── BridgeSettingsDetailPage.xaml
    │   │       ├── BridgeSettingsDetailPage.xaml.cs
    │   │       ├── BridgeSettingsPage.xaml
    │   │       ├── BridgeSettingsPage.xaml.cs
    │   │       ├── CapsManRegistrationTableDetailPage.xaml
    │   │       ├── CapsManRegistrationTableDetailPage.xaml.cs
    │   │       ├── CapsManRegistrationTablePage.xaml
    │   │       ├── CapsManRegistrationTablePage.xaml.cs
    │   │       ├── ConnectionTrackingDetailPage.xaml
    │   │       ├── ConnectionTrackingDetailPage.xaml.cs
    │   │       ├── ConnectionTrackingPage.xaml
    │   │       ├── ConnectionTrackingPage.xaml.cs
    │   │       ├── DhcpServerAlertDetailPage.xaml
    │   │       ├── DhcpServerAlertDetailPage.xaml.cs
    │   │       ├── DhcpServerAlertPage.xaml
    │   │       ├── DhcpServerAlertPage.xaml.cs
    │   │       ├── DhcpServerConfigDetailPage.xaml
    │   │       ├── DhcpServerConfigDetailPage.xaml.cs
    │   │       ├── DhcpServerConfigPage.xaml
    │   │       ├── DhcpServerConfigPage.xaml.cs
    │   │       ├── DhcpServerLeaseDetailPage.xaml
    │   │       ├── DhcpServerLeaseDetailPage.xaml.cs
    │   │       ├── DhcpServerLeasePage.xaml
    │   │       ├── DhcpServerLeasePage.xaml.cs
    │   │       ├── DhcpServerNetworkDetailPage.xaml
    │   │       ├── DhcpServerNetworkDetailPage.xaml.cs
    │   │       ├── DhcpServerNetworkPage.xaml
    │   │       ├── DhcpServerNetworkPage.xaml.cs
    │   │       ├── DhcpServerOptionDetailPage.xaml
    │   │       ├── DhcpServerOptionDetailPage.xaml.cs
    │   │       ├── DhcpServerOptionPage.xaml
    │   │       ├── DhcpServerOptionPage.xaml.cs
    │   │       ├── DnsCacheAllDetailPage.xaml
    │   │       ├── DnsCacheAllDetailPage.xaml.cs
    │   │       ├── DnsCacheAllPage.xaml
    │   │       ├── DnsCacheAllPage.xaml.cs
    │   │       ├── DnsCacheDetailPage.xaml
    │   │       ├── DnsCacheDetailPage.xaml.cs
    │   │       ├── DnsCachePage.xaml
    │   │       ├── DnsCachePage.xaml.cs
    │   │       ├── DnsStaticDetailPage.xaml
    │   │       ├── DnsStaticDetailPage.xaml.cs
    │   │       ├── DnsStaticPage.xaml
    │   │       ├── DnsStaticPage.xaml.cs
    │   │       ├── EthernetMonitorDetailPage.xaml
    │   │       ├── EthernetMonitorDetailPage.xaml.cs
    │   │       ├── EthernetMonitorPage.xaml
    │   │       ├── EthernetMonitorPage.xaml.cs
    │   │       ├── FirewallAddressListDetailPage.xaml
    │   │       ├── FirewallAddressListDetailPage.xaml.cs
    │   │       ├── FirewallAddressListPage.xaml
    │   │       ├── FirewallAddressListPage.xaml.cs
    │   │       ├── FirewallConnectionDetailPage.xaml
    │   │       ├── FirewallConnectionDetailPage.xaml.cs
    │   │       ├── FirewallConnectionPage.xaml
    │   │       ├── FirewallConnectionPage.xaml.cs
    │   │       ├── FirewallFilterDetailPage.xaml
    │   │       ├── FirewallFilterDetailPage.xaml.cs
    │   │       ├── FirewallFilterPage.xaml
    │   │       ├── FirewallFilterPage.xaml.cs
    │   │       ├── FirewallMangleDetailPage.xaml
    │   │       ├── FirewallMangleDetailPage.xaml.cs
    │   │       ├── FirewallManglePage.xaml
    │   │       ├── FirewallManglePage.xaml.cs
    │   │       ├── FirewallNatDetailPage.xaml
    │   │       ├── FirewallNatDetailPage.xaml.cs
    │   │       ├── FirewallNatPage.xaml
    │   │       ├── FirewallNatPage.xaml.cs
    │   │       ├── FirewalServicePortDetailPage.xaml
    │   │       ├── FirewalServicePortDetailPage.xaml.cs
    │   │       ├── FirewalServicePortPage.xaml
    │   │       ├── FirewalServicePortPage.xaml.cs
    │   │       ├── HotspotActiveDetailPage.xaml
    │   │       ├── HotspotActiveDetailPage.xaml.cs
    │   │       ├── HotspotActivePage.xaml
    │   │       ├── HotspotActivePage.xaml.cs
    │   │       ├── HotspotIpBindingDetailPage.xaml
    │   │       ├── HotspotIpBindingDetailPage.xaml.cs
    │   │       ├── HotspotIpBindingPage.xaml
    │   │       ├── HotspotIpBindingPage.xaml.cs
    │   │       ├── HotspotUserDetailPage.xaml
    │   │       ├── HotspotUserDetailPage.xaml.cs
    │   │       ├── HotspotUserPage.xaml
    │   │       ├── HotspotUserPage.xaml.cs
    │   │       ├── HotspotUserProfileDetailPage.xaml
    │   │       ├── HotspotUserProfileDetailPage.xaml.cs
    │   │       ├── HotspotUserProfilePage.xaml
    │   │       ├── HotspotUserProfilePage.xaml.cs
    │   │       ├── InterfaceBridgeDetailPage.xaml
    │   │       ├── InterfaceBridgeDetailPage.xaml.cs
    │   │       ├── InterfaceBridgePage.xaml
    │   │       ├── InterfaceBridgePage.xaml.cs
    │   │       ├── InterfaceDetailPage.xaml
    │   │       ├── InterfaceDetailPage.xaml.cs
    │   │       ├── InterfaceEthernetDetailPage.xaml
    │   │       ├── InterfaceEthernetDetailPage.xaml.cs
    │   │       ├── InterfaceEthernetPage.xaml
    │   │       ├── InterfaceEthernetPage.xaml.cs
    │   │       ├── InterfaceMonitorTrafficDetailPage.xaml
    │   │       ├── InterfaceMonitorTrafficDetailPage.xaml.cs
    │   │       ├── InterfaceMonitorTrafficPage.xaml
    │   │       ├── InterfaceMonitorTrafficPage.xaml.cs
    │   │       ├── InterfacePage.xaml
    │   │       ├── InterfacePage.xaml.cs
    │   │       ├── InterfaceWirelessDetailPage.xaml
    │   │       ├── InterfaceWirelessDetailPage.xaml.cs
    │   │       ├── InterfaceWirelessPage.xaml
    │   │       ├── InterfaceWirelessPage.xaml.cs
    │   │       ├── IpAccountingDetailPage.xaml
    │   │       ├── IpAccountingDetailPage.xaml.cs
    │   │       ├── IpAccountingPage.xaml
    │   │       ├── IpAccountingPage.xaml.cs
    │   │       ├── IpAddressDetailPage.xaml
    │   │       ├── IpAddressDetailPage.xaml.cs
    │   │       ├── IpAddressPage.xaml
    │   │       ├── IpAddressPage.xaml.cs
    │   │       ├── IpArpDetailPage.xaml
    │   │       ├── IpArpDetailPage.xaml.cs
    │   │       ├── IpArpPage.xaml
    │   │       ├── IpArpPage.xaml.cs
    │   │       ├── IpDhcpClientDetailPage.xaml
    │   │       ├── IpDhcpClientDetailPage.xaml.cs
    │   │       ├── IpDhcpClientPage.xaml
    │   │       ├── IpDhcpClientPage.xaml.cs
    │   │       ├── IpDhcpRelayDetailPage.xaml
    │   │       ├── IpDhcpRelayDetailPage.xaml.cs
    │   │       ├── IpDhcpRelayPage.xaml
    │   │       ├── IpDhcpRelayPage.xaml.cs
    │   │       ├── IpDhcpServerDetailPage.xaml
    │   │       ├── IpDhcpServerDetailPage.xaml.cs
    │   │       ├── IpDhcpServerPage.xaml
    │   │       ├── IpDhcpServerPage.xaml.cs
    │   │       ├── IpDnsDetailPage.xaml
    │   │       ├── IpDnsDetailPage.xaml.cs
    │   │       ├── IpDnsPage.xaml
    │   │       ├── IpDnsPage.xaml.cs
    │   │       ├── IpPoolDetailPage.xaml
    │   │       ├── IpPoolDetailPage.xaml.cs
    │   │       ├── IpPoolPage.xaml
    │   │       ├── IpPoolPage.xaml.cs
    │   │       ├── IpRouteDetailPage.xaml
    │   │       ├── IpRouteDetailPage.xaml.cs
    │   │       ├── IpRoutePage.xaml
    │   │       ├── IpRoutePage.xaml.cs
    │   │       ├── LogDetailPage.xaml
    │   │       ├── LogDetailPage.xaml.cs
    │   │       ├── LogPage.xaml
    │   │       ├── LogPage.xaml.cs
    │   │       ├── PppAaaDetailPage.xaml
    │   │       ├── PppAaaDetailPage.xaml.cs
    │   │       ├── PppAaaPage.xaml
    │   │       ├── PppAaaPage.xaml.cs
    │   │       ├── PppActiveDetailPage.xaml
    │   │       ├── PppActiveDetailPage.xaml.cs
    │   │       ├── PppActivePage.xaml
    │   │       ├── PppActivePage.xaml.cs
    │   │       ├── PppProfileDetailPage.xaml
    │   │       ├── PppProfileDetailPage.xaml.cs
    │   │       ├── PppProfilePage.xaml
    │   │       ├── PppProfilePage.xaml.cs
    │   │       ├── PppSecretDetailPage.xaml
    │   │       ├── PppSecretDetailPage.xaml.cs
    │   │       ├── PppSecretPage.xaml
    │   │       ├── PppSecretPage.xaml.cs
    │   │       ├── QueueSimpleDetailPage.xaml
    │   │       ├── QueueSimpleDetailPage.xaml.cs
    │   │       ├── QueueSimplePage.xaml
    │   │       ├── QueueSimplePage.xaml.cs
    │   │       ├── QueueTreeDetailPage.xaml
    │   │       ├── QueueTreeDetailPage.xaml.cs
    │   │       ├── QueueTreePage.xaml
    │   │       ├── QueueTreePage.xaml.cs
    │   │       ├── QueueTypeDetailPage.xaml
    │   │       ├── QueueTypeDetailPage.xaml.cs
    │   │       ├── QueueTypePage.xaml
    │   │       ├── QueueTypePage.xaml.cs
    │   │       ├── SystemIdentityDetailPage.xaml
    │   │       ├── SystemIdentityDetailPage.xaml.cs
    │   │       ├── SystemIdentityPage.xaml
    │   │       ├── SystemIdentityPage.xaml.cs
    │   │       ├── SystemResourceDetailPage.xaml
    │   │       ├── SystemResourceDetailPage.xaml.cs
    │   │       ├── SystemResourcePage.xaml
    │   │       ├── SystemResourcePage.xaml.cs
    │   │       ├── SystemRouterboardDetailPage.xaml
    │   │       ├── SystemRouterboardDetailPage.xaml.cs
    │   │       ├── SystemRouterboardPage.xaml
    │   │       ├── SystemRouterboardPage.xaml.cs
    │   │       ├── ToolPingDetailPage.xaml
    │   │       ├── ToolPingDetailPage.xaml.cs
    │   │       ├── ToolPingPage.xaml
    │   │       ├── ToolPingPage.xaml.cs
    │   │       ├── ToolTorchDetailPage.xaml
    │   │       ├── ToolTorchDetailPage.xaml.cs
    │   │       ├── ToolTorchPage.xaml
    │   │       ├── ToolTorchPage.xaml.cs
    │   │       ├── ToolTracerouteDetailPage.xaml
    │   │       ├── ToolTracerouteDetailPage.xaml.cs
    │   │       ├── ToolTraceroutePage.xaml
    │   │       ├── ToolTraceroutePage.xaml.cs
    │   │       ├── UserDetailPage.xaml
    │   │       ├── UserDetailPage.xaml.cs
    │   │       ├── UserGroupDetailPage.xaml
    │   │       ├── UserGroupDetailPage.xaml.cs
    │   │       ├── UserGroupPage.xaml
    │   │       ├── UserGroupPage.xaml.cs
    │   │       ├── UserPage.xaml
    │   │       ├── UserPage.xaml.cs
    │   │       ├── WirelessAccessListDetailPage.xaml
    │   │       ├── WirelessAccessListDetailPage.xaml.cs
    │   │       ├── WirelessAccessListPage.xaml
    │   │       ├── WirelessAccessListPage.xaml.cs
    │   │       ├── WirelessChannelsDetailPage.xaml
    │   │       ├── WirelessChannelsDetailPage.xaml.cs
    │   │       ├── WirelessChannelsPage.xaml
    │   │       ├── WirelessChannelsPage.xaml.cs
    │   │       ├── WirelessRegistrationTableDetailPage.xaml
    │   │       ├── WirelessRegistrationTableDetailPage.xaml.cs
    │   │       ├── WirelessRegistrationTablePage.xaml
    │   │       ├── WirelessRegistrationTablePage.xaml.cs
    │   │       ├── WirelessSecurityProfileDetailPage.xaml
    │   │       ├── WirelessSecurityProfileDetailPage.xaml.cs
    │   │       ├── WirelessSecurityProfilePage.xaml
    │   │       ├── WirelessSecurityProfilePage.xaml.cs
    │   │       ├── WirelessSnifferDetailPage.xaml
    │   │       ├── WirelessSnifferDetailPage.xaml.cs
    │   │       ├── WirelessSnifferPage.xaml
    │   │       └── WirelessSnifferPage.xaml.cs
    │   ├── MikroTik.EntityBuilder.csproj
    │   ├── MikroTik.EntityBuilder.sln
    │   ├── Program.cs
    │   └── Templates/
    │       ├── DetailPageTemplate
    │       ├── DetailPageTemplateCodeBehind
    │       ├── DetailViewModelTemplate
    │       ├── ViewModelTemplate
    │       ├── ViewTemplate
    │       └── ViewTemplateCodeBehind
    ├── ModemConfigurator/
    │   ├── ModemConfigurator.sln
    │   ├── NuGet.config
    │   └── src/
    │       ├── ModemConfigurator/
    │       │   ├── App.xaml
    │       │   ├── App.xaml.cs
    │       │   ├── Controls/
    │       │   │   └── Picker{T}.cs
    │       │   ├── ModemConfigurator.csproj
    │       │   ├── ModemStartup.cs
    │       │   ├── Services/
    │       │   │   ├── FormsLogListener.cs
    │       │   │   ├── IModemSettings.cs
    │       │   │   └── ModemSettings.cs
    │       │   ├── ViewModels/
    │       │   │   ├── BaseCollectionViewModel.cs
    │       │   │   ├── BaseDetailViewModel.cs
    │       │   │   ├── ErrorPageViewModel.cs
    │       │   │   ├── LoadingPageViewModel.cs
    │       │   │   ├── MainPageViewModel.cs
    │       │   │   ├── ModemSettingsPageViewModel.cs
    │       │   │   └── ViewModelBase.cs
    │       │   └── Views/
    │       │       ├── ErrorPage.xaml
    │       │       ├── ErrorPage.xaml.cs
    │       │       ├── LoadingPage.xaml
    │       │       ├── LoadingPage.xaml.cs
    │       │       ├── MainPage.xaml
    │       │       ├── MainPage.xaml.cs
    │       │       ├── ModemSettingsPage.xaml
    │       │       └── ModemSettingsPage.xaml.cs
    │       └── ModemConfigurator.iOS/
    │           ├── AppDelegate.cs
    │           ├── Assets.xcassets/
    │           │   ├── AppIcon.appiconset/
    │           │   │   └── Contents.json
    │           │   └── Contents.json
    │           ├── Entitlements.plist
    │           ├── Info.plist
    │           ├── Main.cs
    │           ├── ModemConfigurator.iOS.csproj
    │           ├── Properties/
    │           │   └── AssemblyInfo.cs
    │           └── Resources/
    │               ├── LaunchScreen.storyboard
    │               └── Media.xcassets/
    │                   ├── AvantiPointLogo.imageset/
    │                   │   └── Contents.json
    │                   └── Contents.json
    └── ReadMe.md


# Content
File: /.editorconfig
# Suppress: EC112
# top-most EditorConfig file
root = true

# Don't use tabs for indentation.
[*]
indent_style = space
# (Please don't specify an indent_size here; that has too many unintended consequences.)

[*.yml]
indent_size = 2

# Code files
[*.{cs,csx,vb,vbx}]
indent_size = 4

# Code files
[*.sln]
indent_size = 4

# Xml project files
[*.{csproj,vbproj,vcxproj,vcxproj.filters,proj,projitems,shproj}]
indent_size = 2

# Xml config files
[*.{props,targets,ruleset,config,nuspec,resx,vsixmanifest,vsct}]
indent_size = 2

# XAML files
[*.xaml]
indent_size = 2

# JSON files
[*.json]
indent_size = 2

# XML files
[*.xml]
indent_size = 2

# PList Files
[*.plist]
indent_size = 2

# YAML files
[*.{yaml,yml}]
indent_size = 2

#indent switch case contents.
csharp_indent_case_contents = true
#indent switch labels
csharp_indent_switch_labels = true

#Formatting - new line options

#place catch statements on a new line
csharp_new_line_before_catch = true
#place else statements on a new line
csharp_new_line_before_else = true
#require braces to be on a new line for types, methods, properties, lambdas, control_blocks, and accessors (also known as "Allman" style)
csharp_new_line_before_open_brace = types, methods, properties, lambdas, control_blocks, accessors

#Formatting - organize using options

#sort System.* using directives alphabetically, and place them before other usings
dotnet_sort_system_directives_first = true

#Formatting - spacing options

#require a space before the colon for bases or interfaces in a type declaration
csharp_space_after_colon_in_inheritance_clause = true
#require a space after a keyword in a control flow statement such as a for loop
csharp_space_after_keywords_in_control_flow_statements = true
#require a space before the colon for bases or interfaces in a type declaration
csharp_space_before_colon_in_inheritance_clause = true
#remove space within empty argument list parentheses
csharp_space_between_method_call_empty_parameter_list_parentheses = false
#remove space between method call name and opening parenthesis
csharp_space_between_method_call_name_and_opening_parenthesis = false
#do not place space characters after the opening parenthesis and before the closing parenthesis of a method call
csharp_space_between_method_call_parameter_list_parentheses = false
#remove space within empty parameter list parentheses for a method declaration
csharp_space_between_method_declaration_empty_parameter_list_parentheses = false
#place a space character after the opening parenthesis and before the closing parenthesis of a method declaration parameter list.
csharp_space_between_method_declaration_parameter_list_parentheses = false

#Formatting - wrapping options

#leave code block on single line
csharp_preserve_single_line_blocks = true

#Style - expression bodied member options

#prefer expression-bodied members for accessors
csharp_style_expression_bodied_accessors = true:suggestion
#prefer block bodies for constructors
csharp_style_expression_bodied_constructors = false:suggestion
#prefer block bodies for methods
csharp_style_expression_bodied_methods = false:suggestion
#prefer expression-bodied members for properties
csharp_style_expression_bodied_properties = true:suggestion

#Style - expression level options

#prefer the language keyword for member access expressions, instead of the type name, for types that have a keyword to represent them
dotnet_style_predefined_type_for_member_access = true:suggestion

#Style - implicit and explicit types

#prefer var is used to declare variables with built-in system types such as int
csharp_style_var_for_built_in_types = true:suggestion
#prefer var when the type is already mentioned on the right-hand side of a declaration expression
csharp_style_var_when_type_is_apparent = true:suggestion

#Style - language keyword and framework type options

#prefer the language keyword for local variables, method parameters, and class members, instead of the type name, for types that have a keyword to represent them
dotnet_style_predefined_type_for_locals_parameters_members = true:suggestion

#Style - qualification options

#prefer fields not to be prefaced with this. or Me. in Visual Basic
dotnet_style_qualification_for_field = false:suggestion
#prefer methods not to be prefaced with this. or Me. in Visual Basic
dotnet_style_qualification_for_method = false:suggestion
#prefer properties not to be prefaced with this. or Me. in Visual Basic
dotnet_style_qualification_for_property = false:suggestion


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/dansiegel/MikroTik-Demo.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/master


File: /.git\hooks\applypatch-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:


File: /.git\hooks\commit-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}


File: /.git\hooks\fsmonitor-watchman.sample
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
File: /.git\hooks\post-update.sample
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info


File: /.git\hooks\pre-applypatch.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:


File: /.git\hooks\pre-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --


File: /.git\hooks\pre-merge-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:


File: /.git\hooks\pre-push.sample
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0


File: /.git\hooks\pre-rebase.sample
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END


File: /.git\hooks\pre-receive.sample
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi


File: /.git\hooks\prepare-commit-msg.sample
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi


File: /.git\hooks\push-to-checkout.sample
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi


File: /.git\hooks\update.sample
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0


File: /.git\info\exclude
File: /.git\logs\HEAD
0000000000000000000000000000000000000000 81129b35e8512664a303da12cc0af4af34781637 vivek-dodia <vivek.dodia@icloud.com> 1738606320 -0500	clone: from https://github.com/dansiegel/MikroTik-Demo.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 81129b35e8512664a303da12cc0af4af34781637 vivek-dodia <vivek.dodia@icloud.com> 1738606320 -0500	clone: from https://github.com/dansiegel/MikroTik-Demo.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 81129b35e8512664a303da12cc0af4af34781637 vivek-dodia <vivek.dodia@icloud.com> 1738606320 -0500	clone: from https://github.com/dansiegel/MikroTik-Demo.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
81129b35e8512664a303da12cc0af4af34781637 refs/remotes/origin/master
68679638bb0b46d2ffa5501420805f4e3daf0d35 refs/remotes/origin/xf5


File: /.git\refs\heads\master
81129b35e8512664a303da12cc0af4af34781637


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
*.sln text eol=lf
*.xaml text eol=lf
*.cs text eol=lf
*.csproj text eol=lf

File: /.gitignore
# Autosave files
*~

# build
[Oo]bj/
[Bb]in/
packages/
TestResults/

# globs
Makefile.in
File: /azure-pipelines.yml
trigger:
  batch: true
  branches:
    include:
    - master
    - dev
  paths:
    exclude:
    - README.md
    - .editorconfig
    - .gitignore

pr:
  branches:
    include:
    - master
  paths:
    exclude:
    - README.md
    - .editorconfig
    - .gitignore

name: $(Build.BuildId)

variables:
  - name: BuildConfiguration
    value: 'Release'
  - name: TargetSolution
    value: 'ModemConfigurator/src/ModemConfigurator.iOS/ModemConfigurator.iOS.csproj'
  - name: MacImage
    value: macOS-latest
  - group: ModemConfigurator

stages:
  - stage: build
    displayName: Build
    jobs:
      - job: iOSBuild
        displayName: iOS Build
        pool:
          vmImage: $(MacImage)
          demands:
            - xcode
            - Xamarin.iOS
        steps:
          - task: InstallAppleCertificate@2
            displayName: Install Apple Certificate
            inputs:
              certSecureFile: $(iOSCertificate)
              certPwd: $(iOSCertificatePassword)
          - task: InstallAppleProvisioningProfile@1
            displayName: Install Apple Provisioning Profile
            inputs:
              provProfileSecureFile: $(iOSProvisioningProfile)
          - task: ios-bundle-version@1
            displayName: Update Build Version
            inputs:
              sourcePath: ModemConfigurator/src/ModemConfigurator.iOS/Info.plist
              versionCodeOption: 'buildid'
              versionCode: $(Build.BuildId)
              versionName: '3.5.0.$(Build.BuildId)'
              printFile: true
          - bash: |
              dotnet tool install --global boots
              boots --stable Mono
              boots --stable XamariniOS
            displayName: Ensure Latest Mono & Xamarin.iOS SDKs
          - task: NuGetToolInstaller@1
            displayName: Install Latest NuGet
            inputs:
              checkLatest: true
          - task: NuGetCommand@2
            displayName: NuGet Restore
            inputs:
              command: restore
              restoreSolution: ModemConfigurator/src/ModemConfigurator/ModemConfigurator.csproj
          - task: XamariniOS@2
            displayName: Build ModemConfigurator
            inputs:
              solutionFile: $(TargetSolution)
              configuration: $(BuildConfiguration)
              args: '/p:OutputPath=$(Build.ArtifactStagingDirectory) /bl:$(BuildArtifactStagingDirectory)/build.binlog'
              runNugetRestore: true
            env:
              Secret_AppCenterSecret: $(AppCenterSecret)
          - task: PublishPipelineArtifact@1
            displayName: Publish Build Artifacts
            inputs:
              artifact: ios-app
              targetPath: $(Build.ArtifactStagingDirectory)
  - stage: deploy
    displayName: Deploy
    jobs:
      - deployment: iOSDeploy
        displayName: iOS Deploy
        environment: 'App Center'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AppCenterDistribute@3
                  displayName: Deploy to App Center
                  inputs:
                    serverEndpoint: AppCenter
                    appSlug: $(AppSlug)
                    appFile: '$(Pipeline.Workspace)/ios-app/ModemConfigurator.iOS.ipa'
                    symbolsDsymFiles: '$(Pipeline.Workspace)/ios-app/ModemConfigurator.iOS.app.dSYM'
                    symbolsIncludeParentDirectory: false
                    releaseNotesOption: input
                    releaseNotesInput: 'Update for tik4net 3.5.0'
                    isSilent: false


File: /Directory.Build.props
<Project>
  <PropertyGroup>
    <GeneratedFilesFolder>$(MSBuildThisFileDirectory)MikroTik.EntityBuilder\Generated</GeneratedFilesFolder>
  </PropertyGroup>
</Project>

File: /MikroTik.EntityBuilder\Generated\GeneratedExtensions.cs
using ModemConfigurator.Views;
using ModemConfigurator.ViewModels;
using Prism.Ioc;

namespace ModemConfigurator
{
    public static class GeneratedExtensions
    {
        public static void RegisterAutoGeneratedViews(this IContainerRegistry containerRegistry)
        {
            containerRegistry.RegisterForNavigation<LogPage, LogPageViewModel>();
            containerRegistry.RegisterForNavigation<LogDetailPage, LogDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<UserPage, UserPageViewModel>();
            containerRegistry.RegisterForNavigation<UserDetailPage, UserDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<UserGroupPage, UserGroupPageViewModel>();
            containerRegistry.RegisterForNavigation<UserGroupDetailPage, UserGroupDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<ToolPingPage, ToolPingPageViewModel>();
            containerRegistry.RegisterForNavigation<ToolPingDetailPage, ToolPingDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<ToolTorchPage, ToolTorchPageViewModel>();
            containerRegistry.RegisterForNavigation<ToolTorchDetailPage, ToolTorchDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<ToolTraceroutePage, ToolTraceroutePageViewModel>();
            containerRegistry.RegisterForNavigation<ToolTracerouteDetailPage, ToolTracerouteDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<SystemIdentityPage, SystemIdentityPageViewModel>();
            containerRegistry.RegisterForNavigation<SystemIdentityDetailPage, SystemIdentityDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<SystemResourcePage, SystemResourcePageViewModel>();
            containerRegistry.RegisterForNavigation<SystemResourceDetailPage, SystemResourceDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<SystemRouterboardPage, SystemRouterboardPageViewModel>();
            containerRegistry.RegisterForNavigation<SystemRouterboardDetailPage, SystemRouterboardDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpAdvertisementsPage, BgpAdvertisementsPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpAdvertisementsDetailPage, BgpAdvertisementsDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpInstancePage, BgpInstancePageViewModel>();
            containerRegistry.RegisterForNavigation<BgpInstanceDetailPage, BgpInstanceDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpNetworkPage, BgpNetworkPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpNetworkDetailPage, BgpNetworkDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpPeerPage, BgpPeerPageViewModel>();
            containerRegistry.RegisterForNavigation<BgpPeerDetailPage, BgpPeerDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<QueueSimplePage, QueueSimplePageViewModel>();
            containerRegistry.RegisterForNavigation<QueueSimpleDetailPage, QueueSimpleDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<QueueTreePage, QueueTreePageViewModel>();
            containerRegistry.RegisterForNavigation<QueueTreeDetailPage, QueueTreeDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<QueueTypePage, QueueTypePageViewModel>();
            containerRegistry.RegisterForNavigation<QueueTypeDetailPage, QueueTypeDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<PppAaaPage, PppAaaPageViewModel>();
            containerRegistry.RegisterForNavigation<PppAaaDetailPage, PppAaaDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<PppActivePage, PppActivePageViewModel>();
            containerRegistry.RegisterForNavigation<PppActiveDetailPage, PppActiveDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<PppProfilePage, PppProfilePageViewModel>();
            containerRegistry.RegisterForNavigation<PppProfileDetailPage, PppProfileDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<PppSecretPage, PppSecretPageViewModel>();
            containerRegistry.RegisterForNavigation<PppSecretDetailPage, PppSecretDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingSnapshotPage, AccountingSnapshotPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingSnapshotDetailPage, AccountingSnapshotDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingUncountedPage, AccountingUncountedPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingUncountedDetailPage, AccountingUncountedDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingWebAccessPage, AccountingWebAccessPageViewModel>();
            containerRegistry.RegisterForNavigation<AccountingWebAccessDetailPage, AccountingWebAccessDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerConfigPage, DhcpServerConfigPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerConfigDetailPage, DhcpServerConfigDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpAccountingPage, IpAccountingPageViewModel>();
            containerRegistry.RegisterForNavigation<IpAccountingDetailPage, IpAccountingDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpAddressPage, IpAddressPageViewModel>();
            containerRegistry.RegisterForNavigation<IpAddressDetailPage, IpAddressDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpArpPage, IpArpPageViewModel>();
            containerRegistry.RegisterForNavigation<IpArpDetailPage, IpArpDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpClientPage, IpDhcpClientPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpClientDetailPage, IpDhcpClientDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpRelayPage, IpDhcpRelayPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpRelayDetailPage, IpDhcpRelayDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpServerPage, IpDhcpServerPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDhcpServerDetailPage, IpDhcpServerDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDnsPage, IpDnsPageViewModel>();
            containerRegistry.RegisterForNavigation<IpDnsDetailPage, IpDnsDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpPoolPage, IpPoolPageViewModel>();
            containerRegistry.RegisterForNavigation<IpPoolDetailPage, IpPoolDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<IpRoutePage, IpRoutePageViewModel>();
            containerRegistry.RegisterForNavigation<IpRouteDetailPage, IpRouteDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotActivePage, HotspotActivePageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotActiveDetailPage, HotspotActiveDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotIpBindingPage, HotspotIpBindingPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotIpBindingDetailPage, HotspotIpBindingDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotUserPage, HotspotUserPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotUserDetailPage, HotspotUserDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotUserProfilePage, HotspotUserProfilePageViewModel>();
            containerRegistry.RegisterForNavigation<HotspotUserProfileDetailPage, HotspotUserProfileDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallAddressListPage, FirewallAddressListPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallAddressListDetailPage, FirewallAddressListDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallConnectionPage, FirewallConnectionPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallConnectionDetailPage, FirewallConnectionDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<ConnectionTrackingPage, ConnectionTrackingPageViewModel>();
            containerRegistry.RegisterForNavigation<ConnectionTrackingDetailPage, ConnectionTrackingDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallFilterPage, FirewallFilterPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallFilterDetailPage, FirewallFilterDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallManglePage, FirewallManglePageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallMangleDetailPage, FirewallMangleDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallNatPage, FirewallNatPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewallNatDetailPage, FirewallNatDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewalServicePortPage, FirewalServicePortPageViewModel>();
            containerRegistry.RegisterForNavigation<FirewalServicePortDetailPage, FirewalServicePortDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DnsCachePage, DnsCachePageViewModel>();
            containerRegistry.RegisterForNavigation<DnsCacheDetailPage, DnsCacheDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DnsCacheAllPage, DnsCacheAllPageViewModel>();
            containerRegistry.RegisterForNavigation<DnsCacheAllDetailPage, DnsCacheAllDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DnsStaticPage, DnsStaticPageViewModel>();
            containerRegistry.RegisterForNavigation<DnsStaticDetailPage, DnsStaticDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerAlertPage, DhcpServerAlertPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerAlertDetailPage, DhcpServerAlertDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerLeasePage, DhcpServerLeasePageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerLeaseDetailPage, DhcpServerLeaseDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerNetworkPage, DhcpServerNetworkPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerNetworkDetailPage, DhcpServerNetworkDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerOptionPage, DhcpServerOptionPageViewModel>();
            containerRegistry.RegisterForNavigation<DhcpServerOptionDetailPage, DhcpServerOptionDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfacePage, InterfacePageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceDetailPage, InterfaceDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceBridgePage, InterfaceBridgePageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceBridgeDetailPage, InterfaceBridgeDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceEthernetPage, InterfaceEthernetPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceEthernetDetailPage, InterfaceEthernetDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceMonitorTrafficPage, InterfaceMonitorTrafficPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceMonitorTrafficDetailPage, InterfaceMonitorTrafficDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceWirelessPage, InterfaceWirelessPageViewModel>();
            containerRegistry.RegisterForNavigation<InterfaceWirelessDetailPage, InterfaceWirelessDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessAccessListPage, WirelessAccessListPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessAccessListDetailPage, WirelessAccessListDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessChannelsPage, WirelessChannelsPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessChannelsDetailPage, WirelessChannelsDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessRegistrationTablePage, WirelessRegistrationTablePageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessRegistrationTableDetailPage, WirelessRegistrationTableDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessSecurityProfilePage, WirelessSecurityProfilePageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessSecurityProfileDetailPage, WirelessSecurityProfileDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessSnifferPage, WirelessSnifferPageViewModel>();
            containerRegistry.RegisterForNavigation<WirelessSnifferDetailPage, WirelessSnifferDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<EthernetMonitorPage, EthernetMonitorPageViewModel>();
            containerRegistry.RegisterForNavigation<EthernetMonitorDetailPage, EthernetMonitorDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeFilterPage, BridgeFilterPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeFilterDetailPage, BridgeFilterDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeNatPage, BridgeNatPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeNatDetailPage, BridgeNatDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgePortPage, BridgePortPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgePortDetailPage, BridgePortDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeSettingsPage, BridgeSettingsPageViewModel>();
            containerRegistry.RegisterForNavigation<BridgeSettingsDetailPage, BridgeSettingsDetailPageViewModel>();
            containerRegistry.RegisterForNavigation<CapsManRegistrationTablePage, CapsManRegistrationTablePageViewModel>();
            containerRegistry.RegisterForNavigation<CapsManRegistrationTableDetailPage, CapsManRegistrationTableDetailPageViewModel>();

        }
    }
}

File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingSnapshotDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingSnapshotDetailPageViewModel : BaseDetailViewModel<AccountingSnapshot>
    {
        public AccountingSnapshotDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Snapshot Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingSnapshotPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingSnapshotPageViewModel : BaseCollectionViewModel<AccountingSnapshot>
    {
        public AccountingSnapshotPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Snapshot";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingUncountedDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingUncountedDetailPageViewModel : BaseDetailViewModel<AccountingUncounted>
    {
        public AccountingUncountedDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Uncounted Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingUncountedPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingUncountedPageViewModel : BaseCollectionViewModel<AccountingUncounted>
    {
        public AccountingUncountedPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Uncounted";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingWebAccessDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingWebAccessDetailPageViewModel : BaseDetailViewModel<AccountingWebAccess>
    {
        public AccountingWebAccessDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Web Access Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\AccountingWebAccessPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class AccountingWebAccessPageViewModel : BaseCollectionViewModel<AccountingWebAccess>
    {
        public AccountingWebAccessPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Accounting Web Access";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpAdvertisementsDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpAdvertisementsDetailPageViewModel : BaseDetailViewModel<BgpAdvertisements>
    {
        public BgpAdvertisementsDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Advertisements Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpAdvertisementsPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpAdvertisementsPageViewModel : BaseCollectionViewModel<BgpAdvertisements>
    {
        public BgpAdvertisementsPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Advertisements";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpInstanceDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpInstanceDetailPageViewModel : BaseDetailViewModel<BgpInstance>
    {
        public BgpInstanceDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Instance Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpInstancePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpInstancePageViewModel : BaseCollectionViewModel<BgpInstance>
    {
        public BgpInstancePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Instance";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpNetworkDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpNetworkDetailPageViewModel : BaseDetailViewModel<BgpNetwork>
    {
        public BgpNetworkDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Network Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpNetworkPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpNetworkPageViewModel : BaseCollectionViewModel<BgpNetwork>
    {
        public BgpNetworkPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Network";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpPeerDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpPeerDetailPageViewModel : BaseDetailViewModel<BgpPeer>
    {
        public BgpPeerDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Peer Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BgpPeerPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Routing.Bgp;

namespace ModemConfigurator.ViewModels
{
    public class BgpPeerPageViewModel : BaseCollectionViewModel<BgpPeer>
    {
        public BgpPeerPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bgp Peer";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeFilterDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeFilterDetailPageViewModel : BaseDetailViewModel<BridgeFilter>
    {
        public BridgeFilterDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Filter Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeFilterPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeFilterPageViewModel : BaseCollectionViewModel<BridgeFilter>
    {
        public BridgeFilterPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Filter";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeNatDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeNatDetailPageViewModel : BaseDetailViewModel<BridgeNat>
    {
        public BridgeNatDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Nat Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeNatPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeNatPageViewModel : BaseCollectionViewModel<BridgeNat>
    {
        public BridgeNatPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Nat";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgePortDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgePortDetailPageViewModel : BaseDetailViewModel<BridgePort>
    {
        public BridgePortDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Port Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgePortPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgePortPageViewModel : BaseCollectionViewModel<BridgePort>
    {
        public BridgePortPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Port";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeSettingsDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeSettingsDetailPageViewModel : BaseDetailViewModel<BridgeSettings>
    {
        public BridgeSettingsDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Settings Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\BridgeSettingsPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Bridge;

namespace ModemConfigurator.ViewModels
{
    public class BridgeSettingsPageViewModel : BaseCollectionViewModel<BridgeSettings>
    {
        public BridgeSettingsPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Bridge Settings";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\CapsManRegistrationTableDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.CapsMan;

namespace ModemConfigurator.ViewModels
{
    public class CapsManRegistrationTableDetailPageViewModel : BaseDetailViewModel<CapsManRegistrationTable>
    {
        public CapsManRegistrationTableDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Caps Man Registration Table Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\CapsManRegistrationTablePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.CapsMan;

namespace ModemConfigurator.ViewModels
{
    public class CapsManRegistrationTablePageViewModel : BaseCollectionViewModel<CapsManRegistrationTable>
    {
        public CapsManRegistrationTablePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Caps Man Registration Table";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ConnectionTrackingDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class ConnectionTrackingDetailPageViewModel : BaseDetailViewModel<ConnectionTracking>
    {
        public ConnectionTrackingDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Connection Tracking Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ConnectionTrackingPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class ConnectionTrackingPageViewModel : BaseCollectionViewModel<ConnectionTracking>
    {
        public ConnectionTrackingPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Connection Tracking";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerAlertDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerAlertDetailPageViewModel : BaseDetailViewModel<DhcpServerAlert>
    {
        public DhcpServerAlertDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Alert Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerAlertPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerAlertPageViewModel : BaseCollectionViewModel<DhcpServerAlert>
    {
        public DhcpServerAlertPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Alert";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerConfigDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerConfigDetailPageViewModel : BaseDetailViewModel<DhcpServerConfig>
    {
        public DhcpServerConfigDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Config Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerConfigPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerConfigPageViewModel : BaseCollectionViewModel<DhcpServerConfig>
    {
        public DhcpServerConfigPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Config";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerLeaseDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerLeaseDetailPageViewModel : BaseDetailViewModel<DhcpServerLease>
    {
        public DhcpServerLeaseDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Lease Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerLeasePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerLeasePageViewModel : BaseCollectionViewModel<DhcpServerLease>
    {
        public DhcpServerLeasePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Lease";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerNetworkDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerNetworkDetailPageViewModel : BaseDetailViewModel<DhcpServerNetwork>
    {
        public DhcpServerNetworkDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Network Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerNetworkPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerNetworkPageViewModel : BaseCollectionViewModel<DhcpServerNetwork>
    {
        public DhcpServerNetworkPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Network";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerOptionDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerOptionDetailPageViewModel : BaseDetailViewModel<DhcpServerOption>
    {
        public DhcpServerOptionDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Option Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DhcpServerOptionPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.DhcpServer;

namespace ModemConfigurator.ViewModels
{
    public class DhcpServerOptionPageViewModel : BaseCollectionViewModel<DhcpServerOption>
    {
        public DhcpServerOptionPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dhcp Server Option";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsCacheAllDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsCacheAllDetailPageViewModel : BaseDetailViewModel<DnsCacheAll>
    {
        public DnsCacheAllDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Cache All Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsCacheAllPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsCacheAllPageViewModel : BaseCollectionViewModel<DnsCacheAll>
    {
        public DnsCacheAllPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Cache All";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsCacheDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsCacheDetailPageViewModel : BaseDetailViewModel<DnsCache>
    {
        public DnsCacheDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Cache Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsCachePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsCachePageViewModel : BaseCollectionViewModel<DnsCache>
    {
        public DnsCachePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Cache";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsStaticDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsStaticDetailPageViewModel : BaseDetailViewModel<DnsStatic>
    {
        public DnsStaticDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Static Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\DnsStaticPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Dns;

namespace ModemConfigurator.ViewModels
{
    public class DnsStaticPageViewModel : BaseCollectionViewModel<DnsStatic>
    {
        public DnsStaticPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Dns Static";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\EthernetMonitorDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Ethernet;

namespace ModemConfigurator.ViewModels
{
    public class EthernetMonitorDetailPageViewModel : BaseDetailViewModel<EthernetMonitor>
    {
        public EthernetMonitorDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ethernet Monitor Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\EthernetMonitorPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Ethernet;

namespace ModemConfigurator.ViewModels
{
    public class EthernetMonitorPageViewModel : BaseCollectionViewModel<EthernetMonitor>
    {
        public EthernetMonitorPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ethernet Monitor";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallAddressListDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallAddressListDetailPageViewModel : BaseDetailViewModel<FirewallAddressList>
    {
        public FirewallAddressListDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Address List Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallAddressListPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallAddressListPageViewModel : BaseCollectionViewModel<FirewallAddressList>
    {
        public FirewallAddressListPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Address List";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallConnectionDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallConnectionDetailPageViewModel : BaseDetailViewModel<FirewallConnection>
    {
        public FirewallConnectionDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Connection Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallConnectionPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallConnectionPageViewModel : BaseCollectionViewModel<FirewallConnection>
    {
        public FirewallConnectionPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Connection";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallFilterDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallFilterDetailPageViewModel : BaseDetailViewModel<FirewallFilter>
    {
        public FirewallFilterDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Filter Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallFilterPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallFilterPageViewModel : BaseCollectionViewModel<FirewallFilter>
    {
        public FirewallFilterPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Filter";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallMangleDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallMangleDetailPageViewModel : BaseDetailViewModel<FirewallMangle>
    {
        public FirewallMangleDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Mangle Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallManglePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallManglePageViewModel : BaseCollectionViewModel<FirewallMangle>
    {
        public FirewallManglePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Mangle";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallNatDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallNatDetailPageViewModel : BaseDetailViewModel<FirewallNat>
    {
        public FirewallNatDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Nat Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewallNatPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewallNatPageViewModel : BaseCollectionViewModel<FirewallNat>
    {
        public FirewallNatPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewall Nat";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewalServicePortDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewalServicePortDetailPageViewModel : BaseDetailViewModel<FirewalServicePort>
    {
        public FirewalServicePortDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewal Service Port Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\FirewalServicePortPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Firewall;

namespace ModemConfigurator.ViewModels
{
    public class FirewalServicePortPageViewModel : BaseCollectionViewModel<FirewalServicePort>
    {
        public FirewalServicePortPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Firewal Service Port";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotActiveDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotActiveDetailPageViewModel : BaseDetailViewModel<HotspotActive>
    {
        public HotspotActiveDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot Active Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotActivePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotActivePageViewModel : BaseCollectionViewModel<HotspotActive>
    {
        public HotspotActivePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot Active";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotIpBindingDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotIpBindingDetailPageViewModel : BaseDetailViewModel<HotspotIpBinding>
    {
        public HotspotIpBindingDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot Ip Binding Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotIpBindingPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotIpBindingPageViewModel : BaseCollectionViewModel<HotspotIpBinding>
    {
        public HotspotIpBindingPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot Ip Binding";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotUserDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotUserDetailPageViewModel : BaseDetailViewModel<HotspotUser>
    {
        public HotspotUserDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot User Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotUserPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotUserPageViewModel : BaseCollectionViewModel<HotspotUser>
    {
        public HotspotUserPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot User";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotUserProfileDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotUserProfileDetailPageViewModel : BaseDetailViewModel<HotspotUserProfile>
    {
        public HotspotUserProfileDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot User Profile Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\HotspotUserProfilePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip.Hotspot;

namespace ModemConfigurator.ViewModels
{
    public class HotspotUserProfilePageViewModel : BaseCollectionViewModel<HotspotUserProfile>
    {
        public HotspotUserProfilePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Hotspot User Profile";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceBridgeDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceBridgeDetailPageViewModel : BaseDetailViewModel<InterfaceBridge>
    {
        public InterfaceBridgeDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Bridge Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceBridgePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceBridgePageViewModel : BaseCollectionViewModel<InterfaceBridge>
    {
        public InterfaceBridgePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Bridge";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceDetailPageViewModel : BaseDetailViewModel<Interface>
    {
        public InterfaceDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceEthernetDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceEthernetDetailPageViewModel : BaseDetailViewModel<InterfaceEthernet>
    {
        public InterfaceEthernetDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Ethernet Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceEthernetPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceEthernetPageViewModel : BaseCollectionViewModel<InterfaceEthernet>
    {
        public InterfaceEthernetPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Ethernet";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceMonitorTrafficDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceMonitorTrafficDetailPageViewModel : BaseDetailViewModel<InterfaceMonitorTraffic>
    {
        public InterfaceMonitorTrafficDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Monitor Traffic Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceMonitorTrafficPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceMonitorTrafficPageViewModel : BaseCollectionViewModel<InterfaceMonitorTraffic>
    {
        public InterfaceMonitorTrafficPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Monitor Traffic";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfacePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfacePageViewModel : BaseCollectionViewModel<Interface>
    {
        public InterfacePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceWirelessDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceWirelessDetailPageViewModel : BaseDetailViewModel<InterfaceWireless>
    {
        public InterfaceWirelessDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Wireless Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\InterfaceWirelessPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface;

namespace ModemConfigurator.ViewModels
{
    public class InterfaceWirelessPageViewModel : BaseCollectionViewModel<InterfaceWireless>
    {
        public InterfaceWirelessPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Interface Wireless";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpAccountingDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpAccountingDetailPageViewModel : BaseDetailViewModel<IpAccounting>
    {
        public IpAccountingDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Accounting Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpAccountingPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpAccountingPageViewModel : BaseCollectionViewModel<IpAccounting>
    {
        public IpAccountingPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Accounting";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpAddressDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpAddressDetailPageViewModel : BaseDetailViewModel<IpAddress>
    {
        public IpAddressDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Address Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpAddressPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpAddressPageViewModel : BaseCollectionViewModel<IpAddress>
    {
        public IpAddressPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Address";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpArpDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpArpDetailPageViewModel : BaseDetailViewModel<IpArp>
    {
        public IpArpDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Arp Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpArpPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpArpPageViewModel : BaseCollectionViewModel<IpArp>
    {
        public IpArpPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Arp";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpClientDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpClientDetailPageViewModel : BaseDetailViewModel<IpDhcpClient>
    {
        public IpDhcpClientDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Client Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpClientPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpClientPageViewModel : BaseCollectionViewModel<IpDhcpClient>
    {
        public IpDhcpClientPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Client";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpRelayDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpRelayDetailPageViewModel : BaseDetailViewModel<IpDhcpRelay>
    {
        public IpDhcpRelayDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Relay Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpRelayPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpRelayPageViewModel : BaseCollectionViewModel<IpDhcpRelay>
    {
        public IpDhcpRelayPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Relay";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpServerDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpServerDetailPageViewModel : BaseDetailViewModel<IpDhcpServer>
    {
        public IpDhcpServerDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Server Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDhcpServerPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDhcpServerPageViewModel : BaseCollectionViewModel<IpDhcpServer>
    {
        public IpDhcpServerPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dhcp Server";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDnsDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDnsDetailPageViewModel : BaseDetailViewModel<IpDns>
    {
        public IpDnsDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dns Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpDnsPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpDnsPageViewModel : BaseCollectionViewModel<IpDns>
    {
        public IpDnsPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Dns";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpPoolDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpPoolDetailPageViewModel : BaseDetailViewModel<IpPool>
    {
        public IpPoolDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Pool Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpPoolPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpPoolPageViewModel : BaseCollectionViewModel<IpPool>
    {
        public IpPoolPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Pool";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpRouteDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpRouteDetailPageViewModel : BaseDetailViewModel<IpRoute>
    {
        public IpRouteDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Route Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\IpRoutePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ip;

namespace ModemConfigurator.ViewModels
{
    public class IpRoutePageViewModel : BaseCollectionViewModel<IpRoute>
    {
        public IpRoutePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ip Route";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\LogDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;

namespace ModemConfigurator.ViewModels
{
    public class LogDetailPageViewModel : BaseDetailViewModel<Log>
    {
        public LogDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Log Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\LogPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;

namespace ModemConfigurator.ViewModels
{
    public class LogPageViewModel : BaseCollectionViewModel<Log>
    {
        public LogPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Log";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppAaaDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppAaaDetailPageViewModel : BaseDetailViewModel<PppAaa>
    {
        public PppAaaDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Aaa Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppAaaPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppAaaPageViewModel : BaseCollectionViewModel<PppAaa>
    {
        public PppAaaPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Aaa";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppActiveDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppActiveDetailPageViewModel : BaseDetailViewModel<PppActive>
    {
        public PppActiveDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Active Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppActivePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppActivePageViewModel : BaseCollectionViewModel<PppActive>
    {
        public PppActivePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Active";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppProfileDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppProfileDetailPageViewModel : BaseDetailViewModel<PppProfile>
    {
        public PppProfileDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Profile Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppProfilePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppProfilePageViewModel : BaseCollectionViewModel<PppProfile>
    {
        public PppProfilePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Profile";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppSecretDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppSecretDetailPageViewModel : BaseDetailViewModel<PppSecret>
    {
        public PppSecretDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Secret Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\PppSecretPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Ppp;

namespace ModemConfigurator.ViewModels
{
    public class PppSecretPageViewModel : BaseCollectionViewModel<PppSecret>
    {
        public PppSecretPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Ppp Secret";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueSimpleDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueSimpleDetailPageViewModel : BaseDetailViewModel<QueueSimple>
    {
        public QueueSimpleDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Simple Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueSimplePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueSimplePageViewModel : BaseCollectionViewModel<QueueSimple>
    {
        public QueueSimplePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Simple";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueTreeDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueTreeDetailPageViewModel : BaseDetailViewModel<QueueTree>
    {
        public QueueTreeDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Tree Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueTreePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueTreePageViewModel : BaseCollectionViewModel<QueueTree>
    {
        public QueueTreePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Tree";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueTypeDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueTypeDetailPageViewModel : BaseDetailViewModel<QueueType>
    {
        public QueueTypeDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Type Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\QueueTypePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Queue;

namespace ModemConfigurator.ViewModels
{
    public class QueueTypePageViewModel : BaseCollectionViewModel<QueueType>
    {
        public QueueTypePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Queue Type";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemIdentityDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemIdentityDetailPageViewModel : BaseDetailViewModel<SystemIdentity>
    {
        public SystemIdentityDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Identity Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemIdentityPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemIdentityPageViewModel : BaseCollectionViewModel<SystemIdentity>
    {
        public SystemIdentityPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Identity";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemResourceDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemResourceDetailPageViewModel : BaseDetailViewModel<SystemResource>
    {
        public SystemResourceDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Resource Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemResourcePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemResourcePageViewModel : BaseCollectionViewModel<SystemResource>
    {
        public SystemResourcePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Resource";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemRouterboardDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemRouterboardDetailPageViewModel : BaseDetailViewModel<SystemRouterboard>
    {
        public SystemRouterboardDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Routerboard Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\SystemRouterboardPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.System;

namespace ModemConfigurator.ViewModels
{
    public class SystemRouterboardPageViewModel : BaseCollectionViewModel<SystemRouterboard>
    {
        public SystemRouterboardPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "System Routerboard";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolPingDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolPingDetailPageViewModel : BaseDetailViewModel<ToolPing>
    {
        public ToolPingDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Ping Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolPingPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolPingPageViewModel : BaseCollectionViewModel<ToolPing>
    {
        public ToolPingPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Ping";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolTorchDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolTorchDetailPageViewModel : BaseDetailViewModel<ToolTorch>
    {
        public ToolTorchDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Torch Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolTorchPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolTorchPageViewModel : BaseCollectionViewModel<ToolTorch>
    {
        public ToolTorchPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Torch";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolTracerouteDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolTracerouteDetailPageViewModel : BaseDetailViewModel<ToolTraceroute>
    {
        public ToolTracerouteDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Traceroute Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\ToolTraceroutePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Tool;

namespace ModemConfigurator.ViewModels
{
    public class ToolTraceroutePageViewModel : BaseCollectionViewModel<ToolTraceroute>
    {
        public ToolTraceroutePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Tool Traceroute";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\UserDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.User;

namespace ModemConfigurator.ViewModels
{
    public class UserDetailPageViewModel : BaseDetailViewModel<User>
    {
        public UserDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "User Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\UserGroupDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.User;

namespace ModemConfigurator.ViewModels
{
    public class UserGroupDetailPageViewModel : BaseDetailViewModel<UserGroup>
    {
        public UserGroupDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "User Group Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\UserGroupPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.User;

namespace ModemConfigurator.ViewModels
{
    public class UserGroupPageViewModel : BaseCollectionViewModel<UserGroup>
    {
        public UserGroupPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "User Group";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\UserPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.User;

namespace ModemConfigurator.ViewModels
{
    public class UserPageViewModel : BaseCollectionViewModel<User>
    {
        public UserPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "User";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessAccessListDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessAccessListDetailPageViewModel : BaseDetailViewModel<WirelessAccessList>
    {
        public WirelessAccessListDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Access List Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessAccessListPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessAccessListPageViewModel : BaseCollectionViewModel<WirelessAccessList>
    {
        public WirelessAccessListPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Access List";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessChannelsDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessChannelsDetailPageViewModel : BaseDetailViewModel<WirelessChannels>
    {
        public WirelessChannelsDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Channels Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessChannelsPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessChannelsPageViewModel : BaseCollectionViewModel<WirelessChannels>
    {
        public WirelessChannelsPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Channels";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessRegistrationTableDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessRegistrationTableDetailPageViewModel : BaseDetailViewModel<WirelessRegistrationTable>
    {
        public WirelessRegistrationTableDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Registration Table Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessRegistrationTablePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessRegistrationTablePageViewModel : BaseCollectionViewModel<WirelessRegistrationTable>
    {
        public WirelessRegistrationTablePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Registration Table";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessSecurityProfileDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessSecurityProfileDetailPageViewModel : BaseDetailViewModel<WirelessSecurityProfile>
    {
        public WirelessSecurityProfileDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Security Profile Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessSecurityProfilePageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessSecurityProfilePageViewModel : BaseCollectionViewModel<WirelessSecurityProfile>
    {
        public WirelessSecurityProfilePageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Security Profile";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessSnifferDetailPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessSnifferDetailPageViewModel : BaseDetailViewModel<WirelessSniffer>
    {
        public WirelessSnifferDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Sniffer Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\ViewModels\WirelessSnifferPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using tik4net.Objects.Interface.Wireless;

namespace ModemConfigurator.ViewModels
{
    public class WirelessSnifferPageViewModel : BaseCollectionViewModel<WirelessSniffer>
    {
        public WirelessSnifferPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Wireless Sniffer";
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingSnapshotDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingSnapshotDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Accounting Snapshot">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/accounting/snapshot"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Dst Address" IsEnabled="False" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Dst User" IsEnabled="False" Text="{Binding Entity.DstUser}" />
        <EntryCell Label="Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Src Address" IsEnabled="False" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Src User" IsEnabled="False" Text="{Binding Entity.SrcUser}" />
<!--
        <EntryCell Label="Accounting Snapshot" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Accounting Snapshot" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Accounting Snapshot"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\AccountingSnapshotDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingSnapshotDetailPage : ContentPage
    {
        public AccountingSnapshotDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingSnapshotPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingSnapshotPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/accounting/snapshot"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstUser" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstUser}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcUser" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcUser}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\AccountingSnapshotPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingSnapshotPage : ContentPage
    {
        public AccountingSnapshotPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingUncountedDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingUncountedDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Accounting Uncounted">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/accounting/uncounted"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Packets}" />
<!--
        <EntryCell Label="Accounting Uncounted" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Accounting Uncounted" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Accounting Uncounted"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\AccountingUncountedDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingUncountedDetailPage : ContentPage
    {
        public AccountingUncountedDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingUncountedPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingUncountedPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/accounting/uncounted"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\AccountingUncountedPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingUncountedPage : ContentPage
    {
        public AccountingUncountedPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingWebAccessDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingWebAccessDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Accounting Web Access">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/accounting/web-access"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Accessible Via Web" Text="{Binding Entity.AccessibleViaWeb}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
<!--
        <EntryCell Label="Accounting Web Access" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Accounting Web Access" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Accounting Web Access"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\AccountingWebAccessDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingWebAccessDetailPage : ContentPage
    {
        public AccountingWebAccessDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\AccountingWebAccessPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.AccountingWebAccessPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/accounting/web-access"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="AccessibleViaWeb" FlexLayout.Basis="50%" />
            <Label Text="{Binding AccessibleViaWeb}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\AccountingWebAccessPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class AccountingWebAccessPage : ContentPage
    {
        public AccountingWebAccessPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpAdvertisementsDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpAdvertisementsDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bgp Advertisements">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="routing/bgp/advertisements"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Peer" Text="{Binding Entity.Peer}" />
        <EntryCell Label="Prefix" Text="{Binding Entity.Prefix}" />
        <EntryCell Label="Nexthop" Text="{Binding Entity.Nexthop}" />
        <EntryCell Label="As Path" Text="{Binding Entity.AsPath}" />
        <EntryCell Label="Origin" Text="{Binding Entity.Origin}" />
        <EntryCell Label="Communities" Text="{Binding Entity.Communities}" />
<!--
        <EntryCell Label="Bgp Advertisements" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bgp Advertisements" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bgp Advertisements"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BgpAdvertisementsDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpAdvertisementsDetailPage : ContentPage
    {
        public BgpAdvertisementsDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpAdvertisementsPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpAdvertisementsPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="routing/bgp/advertisements"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Peer" FlexLayout.Basis="50%" />
            <Label Text="{Binding Peer}" FlexLayout.Basis="50%" />
            <Label Text="Prefix" FlexLayout.Basis="50%" />
            <Label Text="{Binding Prefix}" FlexLayout.Basis="50%" />
            <Label Text="Nexthop" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nexthop}" FlexLayout.Basis="50%" />
            <Label Text="AsPath" FlexLayout.Basis="50%" />
            <Label Text="{Binding AsPath}" FlexLayout.Basis="50%" />
            <Label Text="Origin" FlexLayout.Basis="50%" />
            <Label Text="{Binding Origin}" FlexLayout.Basis="50%" />
            <Label Text="Communities" FlexLayout.Basis="50%" />
            <Label Text="{Binding Communities}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BgpAdvertisementsPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpAdvertisementsPage : ContentPage
    {
        public BgpAdvertisementsPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpInstanceDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpInstanceDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bgp Instance">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/routing/bgp/instance"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="As" Keyboard="Numeric" Text="{Binding Entity.As}" />
        <EntryCell Label="Router Id" Text="{Binding Entity.RouterId}" />
        <SwitchCell Text="Redistribute Connected" On="{Binding Entity.RedistributeConnected}" />
        <SwitchCell Text="Redistribute Static" On="{Binding Entity.RedistributeStatic}" />
        <SwitchCell Text="Redistribute Rip" On="{Binding Entity.RedistributeRip}" />
        <SwitchCell Text="Redistribute Ospf" On="{Binding Entity.RedistributeOspf}" />
        <SwitchCell Text="Redistribute Other Bgp" On="{Binding Entity.RedistributeOtherBgp}" />
        <SwitchCell Text="Client To Client Reflection" On="{Binding Entity.ClientToClientReflection}" />
        <SwitchCell Text="Ignore As Path Len" On="{Binding Entity.IgnoreAsPathLen}" />
        <SwitchCell Text="Default" On="{Binding Entity.Default}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Bgp Instance" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bgp Instance" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bgp Instance"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BgpInstanceDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpInstanceDetailPage : ContentPage
    {
        public BgpInstanceDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpInstancePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpInstancePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/routing/bgp/instance"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="As" FlexLayout.Basis="50%" />
            <Label Text="{Binding As}" FlexLayout.Basis="50%" />
            <Label Text="RouterId" FlexLayout.Basis="50%" />
            <Label Text="{Binding RouterId}" FlexLayout.Basis="50%" />
            <Label Text="RedistributeConnected" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedistributeConnected}" FlexLayout.Basis="50%" />
            <Label Text="RedistributeStatic" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedistributeStatic}" FlexLayout.Basis="50%" />
            <Label Text="RedistributeRip" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedistributeRip}" FlexLayout.Basis="50%" />
            <Label Text="RedistributeOspf" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedistributeOspf}" FlexLayout.Basis="50%" />
            <Label Text="RedistributeOtherBgp" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedistributeOtherBgp}" FlexLayout.Basis="50%" />
            <Label Text="ClientToClientReflection" FlexLayout.Basis="50%" />
            <Label Text="{Binding ClientToClientReflection}" FlexLayout.Basis="50%" />
            <Label Text="IgnoreAsPathLen" FlexLayout.Basis="50%" />
            <Label Text="{Binding IgnoreAsPathLen}" FlexLayout.Basis="50%" />
            <Label Text="Default" FlexLayout.Basis="50%" />
            <Label Text="{Binding Default}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BgpInstancePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpInstancePage : ContentPage
    {
        public BgpInstancePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpNetworkDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpNetworkDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bgp Network">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/routing/bgp/network"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Network" Text="{Binding Entity.Network}" />
        <SwitchCell Text="Synchronize" On="{Binding Entity.Synchronize}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Bgp Network" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bgp Network" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bgp Network"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BgpNetworkDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpNetworkDetailPage : ContentPage
    {
        public BgpNetworkDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpNetworkPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpNetworkPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/routing/bgp/network"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Network" FlexLayout.Basis="50%" />
            <Label Text="{Binding Network}" FlexLayout.Basis="50%" />
            <Label Text="Synchronize" FlexLayout.Basis="50%" />
            <Label Text="{Binding Synchronize}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BgpNetworkPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpNetworkPage : ContentPage
    {
        public BgpNetworkPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpPeerDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpPeerDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bgp Peer">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/routing/bgp/peer"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Instance" Text="{Binding Entity.Instance}" />
        <EntryCell Label="Remote Address" Text="{Binding Entity.RemoteAddress}" />
        <EntryCell Label="Remote As" Keyboard="Numeric" Text="{Binding Entity.RemoteAs}" />
        <EntryCell Label="Nexthop Choice" Text="{Binding Entity.NexthopChoice}" />
        <SwitchCell Text="Multihop" On="{Binding Entity.Multihop}" />
        <SwitchCell Text="Route Reflect" On="{Binding Entity.RouteReflect}" />
        <EntryCell Label="Hold Time" Text="{Binding Entity.HoldTime}" />
        <EntryCell Label="Ttl" Text="{Binding Entity.Ttl}" />
        <EntryCell Label="Address Families" Text="{Binding Entity.AddressFamilies}" />
        <EntryCell Label="Default Originate" Text="{Binding Entity.DefaultOriginate}" />
        <SwitchCell Text="Remove Private As" On="{Binding Entity.RemovePrivateAs}" />
        <SwitchCell Text="As Override" On="{Binding Entity.AsOverride}" />
        <SwitchCell Text="Passive" On="{Binding Entity.Passive}" />
        <SwitchCell Text="Use Bfd" On="{Binding Entity.UseBfd}" />
        <EntryCell Label="Remote Id" Text="{Binding Entity.RemoteId}" />
        <EntryCell Label="Local Address" IsEnabled="False" Text="{Binding Entity.LocalAddress}" />
        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
        <EntryCell Label="Prefix Count" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.PrefixCount}" />
        <EntryCell Label="Updates Sent" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.UpdatesSent}" />
        <EntryCell Label="Updates Received" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.UpdatesReceived}" />
        <EntryCell Label="Withdrawn Sent" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.WithdrawnSent}" />
        <EntryCell Label="Withdrawn Received" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.WithdrawnReceived}" />
        <EntryCell Label="Remote Hold Time" IsEnabled="False" Text="{Binding Entity.RemoteHoldTime}" />
        <EntryCell Label="Used Hold Time" IsEnabled="False" Text="{Binding Entity.UsedHoldTime}" />
        <EntryCell Label="Used Keepalive Time" IsEnabled="False" Text="{Binding Entity.UsedKeepaliveTime}" />
        <SwitchCell Text="Refresh Capability" On="{Binding Entity.RefreshCapability}" />
        <SwitchCell Text="As 4 Capability" On="{Binding Entity.As4Capability}" />
        <EntryCell Label="State" IsEnabled="False" Text="{Binding Entity.State}" />
        <SwitchCell Text="Established" On="{Binding Entity.Established}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Bgp Peer" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bgp Peer" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bgp Peer"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BgpPeerDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpPeerDetailPage : ContentPage
    {
        public BgpPeerDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BgpPeerPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BgpPeerPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/routing/bgp/peer"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Instance" FlexLayout.Basis="50%" />
            <Label Text="{Binding Instance}" FlexLayout.Basis="50%" />
            <Label Text="RemoteAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteAddress}" FlexLayout.Basis="50%" />
            <Label Text="RemoteAs" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteAs}" FlexLayout.Basis="50%" />
            <Label Text="NexthopChoice" FlexLayout.Basis="50%" />
            <Label Text="{Binding NexthopChoice}" FlexLayout.Basis="50%" />
            <Label Text="Multihop" FlexLayout.Basis="50%" />
            <Label Text="{Binding Multihop}" FlexLayout.Basis="50%" />
            <Label Text="RouteReflect" FlexLayout.Basis="50%" />
            <Label Text="{Binding RouteReflect}" FlexLayout.Basis="50%" />
            <Label Text="HoldTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding HoldTime}" FlexLayout.Basis="50%" />
            <Label Text="Ttl" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ttl}" FlexLayout.Basis="50%" />
            <Label Text="AddressFamilies" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressFamilies}" FlexLayout.Basis="50%" />
            <Label Text="DefaultOriginate" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultOriginate}" FlexLayout.Basis="50%" />
            <Label Text="RemovePrivateAs" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemovePrivateAs}" FlexLayout.Basis="50%" />
            <Label Text="AsOverride" FlexLayout.Basis="50%" />
            <Label Text="{Binding AsOverride}" FlexLayout.Basis="50%" />
            <Label Text="Passive" FlexLayout.Basis="50%" />
            <Label Text="{Binding Passive}" FlexLayout.Basis="50%" />
            <Label Text="UseBfd" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseBfd}" FlexLayout.Basis="50%" />
            <Label Text="RemoteId" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteId}" FlexLayout.Basis="50%" />
            <Label Text="LocalAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding LocalAddress}" FlexLayout.Basis="50%" />
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />
            <Label Text="PrefixCount" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrefixCount}" FlexLayout.Basis="50%" />
            <Label Text="UpdatesSent" FlexLayout.Basis="50%" />
            <Label Text="{Binding UpdatesSent}" FlexLayout.Basis="50%" />
            <Label Text="UpdatesReceived" FlexLayout.Basis="50%" />
            <Label Text="{Binding UpdatesReceived}" FlexLayout.Basis="50%" />
            <Label Text="WithdrawnSent" FlexLayout.Basis="50%" />
            <Label Text="{Binding WithdrawnSent}" FlexLayout.Basis="50%" />
            <Label Text="WithdrawnReceived" FlexLayout.Basis="50%" />
            <Label Text="{Binding WithdrawnReceived}" FlexLayout.Basis="50%" />
            <Label Text="RemoteHoldTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteHoldTime}" FlexLayout.Basis="50%" />
            <Label Text="UsedHoldTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding UsedHoldTime}" FlexLayout.Basis="50%" />
            <Label Text="UsedKeepaliveTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding UsedKeepaliveTime}" FlexLayout.Basis="50%" />
            <Label Text="RefreshCapability" FlexLayout.Basis="50%" />
            <Label Text="{Binding RefreshCapability}" FlexLayout.Basis="50%" />
            <Label Text="As4Capability" FlexLayout.Basis="50%" />
            <Label Text="{Binding As4Capability}" FlexLayout.Basis="50%" />
            <Label Text="State" FlexLayout.Basis="50%" />
            <Label Text="{Binding State}" FlexLayout.Basis="50%" />
            <Label Text="Established" FlexLayout.Basis="50%" />
            <Label Text="{Binding Established}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BgpPeerPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BgpPeerPage : ContentPage
    {
        public BgpPeerPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeFilterDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeFilterDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bridge Filter">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/interface/bridge/filter"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Jump Target" Text="{Binding Entity.JumpTarget}" />
        <EntryCell Label="Log Prefix" Text="{Binding Entity.LogPrefix}" />
        <EntryCell Label="New Packet Mark" Text="{Binding Entity.NewPacketMark}" />
        <EntryCell Label="New Priority" Text="{Binding Entity.NewPriority}" />
        <SwitchCell Text="Passthrough" On="{Binding Entity.Passthrough}" />
        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Chain" Text="{Binding Entity.Chain}" />
        <EntryCell Label="In Bridge" Text="{Binding Entity.InBridge}" />
        <EntryCell Label="In Interface" Text="{Binding Entity.InInterface}" />
        <EntryCell Label="Out Bridge" Text="{Binding Entity.OutBridge}" />
        <EntryCell Label="Out Interface" Text="{Binding Entity.OutInterface}" />
        <EntryCell Label="Src Mac Address" Text="{Binding Entity.SrcMacAddress}" />
        <EntryCell Label="Dst Mac Address" Text="{Binding Entity.DstMacAddress}" />
        <EntryCell Label="Mac Protocol" Text="{Binding Entity.MacProtocol}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Src Port" Text="{Binding Entity.SrcPort}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Dst Port" Text="{Binding Entity.DstPort}" />
        <EntryCell Label="Ip Protocol" Text="{Binding Entity.IpProtocol}" />
        <EntryCell Label="Packet Mark" Text="{Binding Entity.PacketMark}" />
        <EntryCell Label="Ingress Priority" Text="{Binding Entity.IngressPriority}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Bridge Filter" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bridge Filter" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bridge Filter"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BridgeFilterDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeFilterDetailPage : ContentPage
    {
        public BridgeFilterDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeFilterPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeFilterPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/interface/bridge/filter"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Action" FlexLayout.Basis="50%" />
            <Label Text="{Binding Action}" FlexLayout.Basis="50%" />
            <Label Text="JumpTarget" FlexLayout.Basis="50%" />
            <Label Text="{Binding JumpTarget}" FlexLayout.Basis="50%" />
            <Label Text="LogPrefix" FlexLayout.Basis="50%" />
            <Label Text="{Binding LogPrefix}" FlexLayout.Basis="50%" />
            <Label Text="NewPacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding NewPacketMark}" FlexLayout.Basis="50%" />
            <Label Text="NewPriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding NewPriority}" FlexLayout.Basis="50%" />
            <Label Text="Passthrough" FlexLayout.Basis="50%" />
            <Label Text="{Binding Passthrough}" FlexLayout.Basis="50%" />
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Chain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Chain}" FlexLayout.Basis="50%" />
            <Label Text="InBridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding InBridge}" FlexLayout.Basis="50%" />
            <Label Text="InInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding InInterface}" FlexLayout.Basis="50%" />
            <Label Text="OutBridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutBridge}" FlexLayout.Basis="50%" />
            <Label Text="OutInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutInterface}" FlexLayout.Basis="50%" />
            <Label Text="SrcMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="MacProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacProtocol}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcPort}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstPort}" FlexLayout.Basis="50%" />
            <Label Text="IpProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding IpProtocol}" FlexLayout.Basis="50%" />
            <Label Text="PacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketMark}" FlexLayout.Basis="50%" />
            <Label Text="IngressPriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding IngressPriority}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BridgeFilterPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeFilterPage : ContentPage
    {
        public BridgeFilterPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeNatDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeNatDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bridge Nat">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/interface/bridge/nat"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="To Arp Reply Mac Address" Text="{Binding Entity.ToArpReplyMacAddress}" />
        <EntryCell Label="To Dst Mac Address" Text="{Binding Entity.ToDstMacAddress}" />
        <EntryCell Label="To Src Mac Address" Text="{Binding Entity.ToSrcMacAddress}" />
        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Chain" Text="{Binding Entity.Chain}" />
        <EntryCell Label="In Bridge" Text="{Binding Entity.InBridge}" />
        <EntryCell Label="In Interface" Text="{Binding Entity.InInterface}" />
        <EntryCell Label="Out Bridge" Text="{Binding Entity.OutBridge}" />
        <EntryCell Label="Out Interface" Text="{Binding Entity.OutInterface}" />
        <EntryCell Label="Src Mac Address" Text="{Binding Entity.SrcMacAddress}" />
        <EntryCell Label="Dst Mac Address" Text="{Binding Entity.DstMacAddress}" />
        <EntryCell Label="Mac Protocol" Text="{Binding Entity.MacProtocol}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Src Port" Text="{Binding Entity.SrcPort}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Dst Port" Text="{Binding Entity.DstPort}" />
        <EntryCell Label="Ip Protocol" Text="{Binding Entity.IpProtocol}" />
        <EntryCell Label="Packet Mark" Text="{Binding Entity.PacketMark}" />
        <EntryCell Label="Ingress Priority" Text="{Binding Entity.IngressPriority}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Bridge Nat" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bridge Nat" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bridge Nat"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BridgeNatDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeNatDetailPage : ContentPage
    {
        public BridgeNatDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeNatPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeNatPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/interface/bridge/nat"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Action" FlexLayout.Basis="50%" />
            <Label Text="{Binding Action}" FlexLayout.Basis="50%" />
            <Label Text="ToArpReplyMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToArpReplyMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="ToDstMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToDstMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="ToSrcMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToSrcMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Chain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Chain}" FlexLayout.Basis="50%" />
            <Label Text="InBridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding InBridge}" FlexLayout.Basis="50%" />
            <Label Text="InInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding InInterface}" FlexLayout.Basis="50%" />
            <Label Text="OutBridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutBridge}" FlexLayout.Basis="50%" />
            <Label Text="OutInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutInterface}" FlexLayout.Basis="50%" />
            <Label Text="SrcMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="MacProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacProtocol}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcPort}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstPort}" FlexLayout.Basis="50%" />
            <Label Text="IpProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding IpProtocol}" FlexLayout.Basis="50%" />
            <Label Text="PacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketMark}" FlexLayout.Basis="50%" />
            <Label Text="IngressPriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding IngressPriority}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BridgeNatPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeNatPage : ContentPage
    {
        public BridgeNatPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgePortDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgePortDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bridge Port">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/bridge/port"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Bridge" Text="{Binding Entity.Bridge}" />
        <EntryCell Label="Priority" Keyboard="Numeric" Text="{Binding Entity.Priority}" />
        <EntryCell Label="Path Cost" Keyboard="Numeric" Text="{Binding Entity.PathCost}" />
        <EntryCell Label="Horizon" Text="{Binding Entity.Horizon}" />
        <EntryCell Label="Edge" Text="{Binding Entity.Edge}" />
        <EntryCell Label="Point To Point" Text="{Binding Entity.PointToPoint}" />
        <EntryCell Label="External Fdb" Text="{Binding Entity.ExternalFdb}" />
        <SwitchCell Text="Auto Isolate" On="{Binding Entity.AutoIsolate}" />
<!--
        <EntryCell Label="Bridge Port" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bridge Port" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bridge Port"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BridgePortDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgePortDetailPage : ContentPage
    {
        public BridgePortDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgePortPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgePortPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/bridge/port"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="Bridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bridge}" FlexLayout.Basis="50%" />
            <Label Text="Priority" FlexLayout.Basis="50%" />
            <Label Text="{Binding Priority}" FlexLayout.Basis="50%" />
            <Label Text="PathCost" FlexLayout.Basis="50%" />
            <Label Text="{Binding PathCost}" FlexLayout.Basis="50%" />
            <Label Text="Horizon" FlexLayout.Basis="50%" />
            <Label Text="{Binding Horizon}" FlexLayout.Basis="50%" />
            <Label Text="Edge" FlexLayout.Basis="50%" />
            <Label Text="{Binding Edge}" FlexLayout.Basis="50%" />
            <Label Text="PointToPoint" FlexLayout.Basis="50%" />
            <Label Text="{Binding PointToPoint}" FlexLayout.Basis="50%" />
            <Label Text="ExternalFdb" FlexLayout.Basis="50%" />
            <Label Text="{Binding ExternalFdb}" FlexLayout.Basis="50%" />
            <Label Text="AutoIsolate" FlexLayout.Basis="50%" />
            <Label Text="{Binding AutoIsolate}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BridgePortPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgePortPage : ContentPage
    {
        public BridgePortPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeSettingsDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeSettingsDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Bridge Settings">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/bridge/settings"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <SwitchCell Text="Allow Fast Path" On="{Binding Entity.AllowFastPath}" />
        <SwitchCell Text="Use Ip Firewall" On="{Binding Entity.UseIpFirewall}" />
        <SwitchCell Text="Use Ip Firewall For Pppoe" On="{Binding Entity.UseIpFirewallForPppoe}" />
        <SwitchCell Text="Use Ip Firewall For Vlan" On="{Binding Entity.UseIpFirewallForVlan}" />
<!--
        <EntryCell Label="Bridge Settings" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Bridge Settings" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Bridge Settings"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\BridgeSettingsDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeSettingsDetailPage : ContentPage
    {
        public BridgeSettingsDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\BridgeSettingsPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.BridgeSettingsPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/bridge/settings"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="AllowFastPath" FlexLayout.Basis="50%" />
            <Label Text="{Binding AllowFastPath}" FlexLayout.Basis="50%" />
            <Label Text="UseIpFirewall" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseIpFirewall}" FlexLayout.Basis="50%" />
            <Label Text="UseIpFirewallForPppoe" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseIpFirewallForPppoe}" FlexLayout.Basis="50%" />
            <Label Text="UseIpFirewallForVlan" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseIpFirewallForVlan}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\BridgeSettingsPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class BridgeSettingsPage : ContentPage
    {
        public BridgeSettingsPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\CapsManRegistrationTableDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.CapsManRegistrationTableDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Caps Man Registration Table">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="caps-man/registration-table"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="MAC Address" IsEnabled="False" Text="{Binding Entity.MACAddress}" />
        <EntryCell Label="Interface" IsEnabled="False" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
        <EntryCell Label="SSID" IsEnabled="False" Text="{Binding Entity.SSID}" />
        <EntryCell Label="Tx Rate" IsEnabled="False" Text="{Binding Entity.TxRate}" />
        <EntryCell Label="Tx Rate Set" IsEnabled="False" Text="{Binding Entity.TxRateSet}" />
        <EntryCell Label="Rx Rate" IsEnabled="False" Text="{Binding Entity.RxRate}" />
        <EntryCell Label="Signal" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Signal}" />
        <EntryCell Label="Packets" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Bytes" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Comment" IsEnabled="False" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Caps Man Registration Table" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Caps Man Registration Table" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Caps Man Registration Table"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\CapsManRegistrationTableDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class CapsManRegistrationTableDetailPage : ContentPage
    {
        public CapsManRegistrationTableDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\CapsManRegistrationTablePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.CapsManRegistrationTablePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="caps-man/registration-table"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="MACAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MACAddress}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />
            <Label Text="SSID" FlexLayout.Basis="50%" />
            <Label Text="{Binding SSID}" FlexLayout.Basis="50%" />
            <Label Text="TxRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxRate}" FlexLayout.Basis="50%" />
            <Label Text="TxRateSet" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxRateSet}" FlexLayout.Basis="50%" />
            <Label Text="RxRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxRate}" FlexLayout.Basis="50%" />
            <Label Text="Signal" FlexLayout.Basis="50%" />
            <Label Text="{Binding Signal}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\CapsManRegistrationTablePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class CapsManRegistrationTablePage : ContentPage
    {
        public CapsManRegistrationTablePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ConnectionTrackingDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ConnectionTrackingDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Connection Tracking">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/firewall/connection/tracking"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Enabled" Text="{Binding Entity.Enabled}" />
        <EntryCell Label="Tcp Syn Sent Timeout" Text="{Binding Entity.TcpSynSentTimeout}" />
        <EntryCell Label="Tcp Syn Received Timeout" Text="{Binding Entity.TcpSynReceivedTimeout}" />
        <EntryCell Label="Tcp Established Timeout" Text="{Binding Entity.TcpEstablishedTimeout}" />
        <EntryCell Label="Tcp Fin Wait Timeout" Text="{Binding Entity.TcpFinWaitTimeout}" />
        <EntryCell Label="Tcp Close Wait Timeout" Text="{Binding Entity.TcpCloseWaitTimeout}" />
        <EntryCell Label="Tcp Last Ack Timeout" Text="{Binding Entity.TcpLastAckTimeout}" />
        <EntryCell Label="Tcp Time Wait Timeout" Text="{Binding Entity.TcpTimeWaitTimeout}" />
        <EntryCell Label="Tcp Close Timeout" Text="{Binding Entity.TcpCloseTimeout}" />
        <EntryCell Label="Udp Timeout" Text="{Binding Entity.UdpTimeout}" />
        <EntryCell Label="Udp Stream Timeout" Text="{Binding Entity.UdpStreamTimeout}" />
        <EntryCell Label="Icmp Timeout" Text="{Binding Entity.IcmpTimeout}" />
        <EntryCell Label="Generic Timeout" Text="{Binding Entity.GenericTimeout}" />
        <EntryCell Label="Max Entries" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.MaxEntries}" />
        <EntryCell Label="Total Entries" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalEntries}" />
<!--
        <EntryCell Label="Connection Tracking" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Connection Tracking" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Connection Tracking"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\ConnectionTrackingDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ConnectionTrackingDetailPage : ContentPage
    {
        public ConnectionTrackingDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ConnectionTrackingPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ConnectionTrackingPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/firewall/connection/tracking"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Enabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Enabled}" FlexLayout.Basis="50%" />
            <Label Text="TcpSynSentTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpSynSentTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpSynReceivedTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpSynReceivedTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpEstablishedTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpEstablishedTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpFinWaitTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpFinWaitTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpCloseWaitTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpCloseWaitTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpLastAckTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpLastAckTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpTimeWaitTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpTimeWaitTimeout}" FlexLayout.Basis="50%" />
            <Label Text="TcpCloseTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpCloseTimeout}" FlexLayout.Basis="50%" />
            <Label Text="UdpTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding UdpTimeout}" FlexLayout.Basis="50%" />
            <Label Text="UdpStreamTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding UdpStreamTimeout}" FlexLayout.Basis="50%" />
            <Label Text="IcmpTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding IcmpTimeout}" FlexLayout.Basis="50%" />
            <Label Text="GenericTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding GenericTimeout}" FlexLayout.Basis="50%" />
            <Label Text="MaxEntries" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxEntries}" FlexLayout.Basis="50%" />
            <Label Text="TotalEntries" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalEntries}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\ConnectionTrackingPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ConnectionTrackingPage : ContentPage
    {
        public ConnectionTrackingPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerAlertDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerAlertDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dhcp Server Alert">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server/alert"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Alert Timeout" Text="{Binding Entity.AlertTimeout}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="On Alert" Text="{Binding Entity.OnAlert}" />
        <EntryCell Label="Valid Server" Text="{Binding Entity.ValidServer}" />
        <EntryCell Label="Unknown Server" IsEnabled="False" Text="{Binding Entity.UnknownServer}" />
<!--
        <EntryCell Label="Dhcp Server Alert" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dhcp Server Alert" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dhcp Server Alert"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerAlertDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerAlertDetailPage : ContentPage
    {
        public DhcpServerAlertDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerAlertPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerAlertPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server/alert"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AlertTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding AlertTimeout}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="OnAlert" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnAlert}" FlexLayout.Basis="50%" />
            <Label Text="ValidServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding ValidServer}" FlexLayout.Basis="50%" />
            <Label Text="UnknownServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding UnknownServer}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerAlertPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerAlertPage : ContentPage
    {
        public DhcpServerAlertPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerConfigDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerConfigDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dhcp Server Config">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server/config"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Store Leases Disk" Text="{Binding Entity.StoreLeasesDisk}" />
<!--
        <EntryCell Label="Dhcp Server Config" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dhcp Server Config" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dhcp Server Config"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerConfigDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerConfigDetailPage : ContentPage
    {
        public DhcpServerConfigDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerConfigPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerConfigPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server/config"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="StoreLeasesDisk" FlexLayout.Basis="50%" />
            <Label Text="{Binding StoreLeasesDisk}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerConfigPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerConfigPage : ContentPage
    {
        public DhcpServerConfigPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerLeaseDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerLeaseDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dhcp Server Lease">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server/lease"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Address List" Text="{Binding Entity.AddressList}" />
        <SwitchCell Text="Always Broadcast" On="{Binding Entity.AlwaysBroadcast}" />
        <SwitchCell Text="Block Access" On="{Binding Entity.BlockAccess}" />
        <EntryCell Label="Client Id" Text="{Binding Entity.ClientId}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Src Mac Address" Text="{Binding Entity.SrcMacAddress}" />
        <EntryCell Label="Use Src Mac" Text="{Binding Entity.UseSrcMac}" />
        <EntryCell Label="Active Address" IsEnabled="False" Text="{Binding Entity.ActiveAddress}" />
        <EntryCell Label="Active Client Id" IsEnabled="False" Text="{Binding Entity.ActiveClientId}" />
        <EntryCell Label="Active Mac Address" IsEnabled="False" Text="{Binding Entity.ActiveMacAddress}" />
        <EntryCell Label="Active Server" IsEnabled="False" Text="{Binding Entity.ActiveServer}" />
        <EntryCell Label="Agent Circuit Id" IsEnabled="False" Text="{Binding Entity.AgentCircuitId}" />
        <EntryCell Label="Agent Remote Id" IsEnabled="False" Text="{Binding Entity.AgentRemoteId}" />
        <EntryCell Label="Blocked" IsEnabled="False" Text="{Binding Entity.Blocked}" />
        <EntryCell Label="Expires After" IsEnabled="False" Text="{Binding Entity.ExpiresAfter}" />
        <EntryCell Label="Host Name" IsEnabled="False" Text="{Binding Entity.HostName}" />
        <SwitchCell Text="Radius" On="{Binding Entity.Radius}" />
        <EntryCell Label="Rate Limit" IsEnabled="False" Text="{Binding Entity.RateLimit}" />
        <EntryCell Label="Server" IsEnabled="False" Text="{Binding Entity.Server}" />
        <EntryCell Label="Status" IsEnabled="False" Text="{Binding Entity.Status}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Dhcp Server Lease" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dhcp Server Lease" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dhcp Server Lease"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerLeaseDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerLeaseDetailPage : ContentPage
    {
        public DhcpServerLeaseDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerLeasePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerLeasePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server/lease"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="AddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressList}" FlexLayout.Basis="50%" />
            <Label Text="AlwaysBroadcast" FlexLayout.Basis="50%" />
            <Label Text="{Binding AlwaysBroadcast}" FlexLayout.Basis="50%" />
            <Label Text="BlockAccess" FlexLayout.Basis="50%" />
            <Label Text="{Binding BlockAccess}" FlexLayout.Basis="50%" />
            <Label Text="ClientId" FlexLayout.Basis="50%" />
            <Label Text="{Binding ClientId}" FlexLayout.Basis="50%" />
            <Label Text="LeaseTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding LeaseTime}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="UseSrcMac" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseSrcMac}" FlexLayout.Basis="50%" />
            <Label Text="ActiveAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ActiveAddress}" FlexLayout.Basis="50%" />
            <Label Text="ActiveClientId" FlexLayout.Basis="50%" />
            <Label Text="{Binding ActiveClientId}" FlexLayout.Basis="50%" />
            <Label Text="ActiveMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ActiveMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="ActiveServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding ActiveServer}" FlexLayout.Basis="50%" />
            <Label Text="AgentCircuitId" FlexLayout.Basis="50%" />
            <Label Text="{Binding AgentCircuitId}" FlexLayout.Basis="50%" />
            <Label Text="AgentRemoteId" FlexLayout.Basis="50%" />
            <Label Text="{Binding AgentRemoteId}" FlexLayout.Basis="50%" />
            <Label Text="Blocked" FlexLayout.Basis="50%" />
            <Label Text="{Binding Blocked}" FlexLayout.Basis="50%" />
            <Label Text="ExpiresAfter" FlexLayout.Basis="50%" />
            <Label Text="{Binding ExpiresAfter}" FlexLayout.Basis="50%" />
            <Label Text="HostName" FlexLayout.Basis="50%" />
            <Label Text="{Binding HostName}" FlexLayout.Basis="50%" />
            <Label Text="Radius" FlexLayout.Basis="50%" />
            <Label Text="{Binding Radius}" FlexLayout.Basis="50%" />
            <Label Text="RateLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding RateLimit}" FlexLayout.Basis="50%" />
            <Label Text="Server" FlexLayout.Basis="50%" />
            <Label Text="{Binding Server}" FlexLayout.Basis="50%" />
            <Label Text="Status" FlexLayout.Basis="50%" />
            <Label Text="{Binding Status}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerLeasePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerLeasePage : ContentPage
    {
        public DhcpServerLeasePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerNetworkDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerNetworkDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dhcp Server Network">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server/network"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Boot File Name" Text="{Binding Entity.BootFileName}" />
        <EntryCell Label="Caps Manager" Text="{Binding Entity.CapsManager}" />
        <EntryCell Label="Dhcp Option" Text="{Binding Entity.DhcpOption}" />
        <EntryCell Label="Dns Server" Text="{Binding Entity.DnsServer}" />
        <EntryCell Label="Domain" Text="{Binding Entity.Domain}" />
        <EntryCell Label="Gateway" Text="{Binding Entity.Gateway}" />
        <EntryCell Label="Netmask" Text="{Binding Entity.Netmask}" />
        <EntryCell Label="Next Server" Text="{Binding Entity.NextServer}" />
        <EntryCell Label="Ntp Server" Text="{Binding Entity.NtpServer}" />
        <EntryCell Label="Wins Server" Text="{Binding Entity.WinsServer}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Dhcp Server Network" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dhcp Server Network" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dhcp Server Network"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerNetworkDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerNetworkDetailPage : ContentPage
    {
        public DhcpServerNetworkDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerNetworkPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerNetworkPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server/network"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="BootFileName" FlexLayout.Basis="50%" />
            <Label Text="{Binding BootFileName}" FlexLayout.Basis="50%" />
            <Label Text="CapsManager" FlexLayout.Basis="50%" />
            <Label Text="{Binding CapsManager}" FlexLayout.Basis="50%" />
            <Label Text="DhcpOption" FlexLayout.Basis="50%" />
            <Label Text="{Binding DhcpOption}" FlexLayout.Basis="50%" />
            <Label Text="DnsServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding DnsServer}" FlexLayout.Basis="50%" />
            <Label Text="Domain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Domain}" FlexLayout.Basis="50%" />
            <Label Text="Gateway" FlexLayout.Basis="50%" />
            <Label Text="{Binding Gateway}" FlexLayout.Basis="50%" />
            <Label Text="Netmask" FlexLayout.Basis="50%" />
            <Label Text="{Binding Netmask}" FlexLayout.Basis="50%" />
            <Label Text="NextServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding NextServer}" FlexLayout.Basis="50%" />
            <Label Text="NtpServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding NtpServer}" FlexLayout.Basis="50%" />
            <Label Text="WinsServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding WinsServer}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerNetworkPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerNetworkPage : ContentPage
    {
        public DhcpServerNetworkPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerOptionDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerOptionDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dhcp Server Option">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server/option"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Code" Text="{Binding Entity.Code}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Value" Text="{Binding Entity.Value}" />
        <EntryCell Label="Raw Value" Text="{Binding Entity.RawValue}" />
<!--
        <EntryCell Label="Dhcp Server Option" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dhcp Server Option" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dhcp Server Option"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerOptionDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerOptionDetailPage : ContentPage
    {
        public DhcpServerOptionDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerOptionPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DhcpServerOptionPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server/option"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Code" FlexLayout.Basis="50%" />
            <Label Text="{Binding Code}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Value" FlexLayout.Basis="50%" />
            <Label Text="{Binding Value}" FlexLayout.Basis="50%" />
            <Label Text="RawValue" FlexLayout.Basis="50%" />
            <Label Text="{Binding RawValue}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DhcpServerOptionPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DhcpServerOptionPage : ContentPage
    {
        public DhcpServerOptionPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheAllDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsCacheAllDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dns Cache All">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dns/cache/all"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Data" IsEnabled="False" Text="{Binding Entity.Data}" />
        <EntryCell Label="Name" IsEnabled="False" Text="{Binding Entity.Name}" />
        <EntryCell Label="Ttl" IsEnabled="False" Text="{Binding Entity.Ttl}" />
        <EntryCell Label="Type" IsEnabled="False" Text="{Binding Entity.Type}" />
<!--
        <EntryCell Label="Dns Cache All" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dns Cache All" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dns Cache All"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheAllDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsCacheAllDetailPage : ContentPage
    {
        public DnsCacheAllDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheAllPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsCacheAllPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dns/cache/all"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Data" FlexLayout.Basis="50%" />
            <Label Text="{Binding Data}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Ttl" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ttl}" FlexLayout.Basis="50%" />
            <Label Text="Type" FlexLayout.Basis="50%" />
            <Label Text="{Binding Type}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheAllPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsCacheAllPage : ContentPage
    {
        public DnsCacheAllPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsCacheDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dns Cache">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dns/cache"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" IsEnabled="False" Text="{Binding Entity.Address}" />
        <EntryCell Label="Name" IsEnabled="False" Text="{Binding Entity.Name}" />
        <EntryCell Label="Ttl" IsEnabled="False" Text="{Binding Entity.Ttl}" />
<!--
        <EntryCell Label="Dns Cache" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dns Cache" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dns Cache"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DnsCacheDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsCacheDetailPage : ContentPage
    {
        public DnsCacheDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsCachePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsCachePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dns/cache"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Ttl" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ttl}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DnsCachePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsCachePage : ContentPage
    {
        public DnsCachePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsStaticDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsStaticDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Dns Static">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dns/static"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Ttl" Text="{Binding Entity.Ttl}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Dns Static" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Dns Static" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Dns Static"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\DnsStaticDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsStaticDetailPage : ContentPage
    {
        public DnsStaticDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\DnsStaticPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.DnsStaticPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dns/static"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Ttl" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ttl}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\DnsStaticPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class DnsStaticPage : ContentPage
    {
        public DnsStaticPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\EthernetMonitorDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.EthernetMonitorDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ethernet Monitor">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/interface/ethernet/monitor"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Name" IsEnabled="False" Text="{Binding Entity.Name}" />
        <EntryCell Label="Auto Negotiation" Text="{Binding Entity.AutoNegotiation}" />
        <EntryCell Label="Default Cable Settings" Text="{Binding Entity.DefaultCableSettings}" />
        <SwitchCell Text="Full Duplex" On="{Binding Entity.FullDuplex}" />
        <EntryCell Label="Rate" Text="{Binding Entity.Rate}" />
        <EntryCell Label="Status" Text="{Binding Entity.Status}" />
        <EntryCell Label="Tx Flow Control" Text="{Binding Entity.TxFlowControl}" />
        <EntryCell Label="Rx Flow Control" Text="{Binding Entity.RxFlowControl}" />
        <SwitchCell Text="Sfp Module Present" On="{Binding Entity.SfpModulePresent}" />
        <SwitchCell Text="Sfp Rx Lose" On="{Binding Entity.SfpRxLose}" />
        <SwitchCell Text="Sfp Tx Fault" On="{Binding Entity.SfpTxFault}" />
        <EntryCell Label="Sfp Connector Type" Text="{Binding Entity.SfpConnectorType}" />
        <EntryCell Label="Sfp Link Length Copper" Text="{Binding Entity.SfpLinkLengthCopper}" />
        <EntryCell Label="Sfp Vendor Name" Text="{Binding Entity.SfpVendorName}" />
        <EntryCell Label="Sfp Vendor Part Number" Text="{Binding Entity.SfpVendorPartNumber}" />
        <EntryCell Label="Sfp Vendor Revision" Text="{Binding Entity.SfpVendorRevision}" />
        <EntryCell Label="Sfp Vendor Serial" Text="{Binding Entity.SfpVendorSerial}" />
        <EntryCell Label="Sfp Manufacturing Date" Text="{Binding Entity.SfpManufacturingDate}" />
        <EntryCell Label="Eeprom" Text="{Binding Entity.Eeprom}" />
<!--
        <EntryCell Label="Ethernet Monitor" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ethernet Monitor" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ethernet Monitor"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\EthernetMonitorDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class EthernetMonitorDetailPage : ContentPage
    {
        public EthernetMonitorDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\EthernetMonitorPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.EthernetMonitorPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/interface/ethernet/monitor"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="AutoNegotiation" FlexLayout.Basis="50%" />
            <Label Text="{Binding AutoNegotiation}" FlexLayout.Basis="50%" />
            <Label Text="DefaultCableSettings" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultCableSettings}" FlexLayout.Basis="50%" />
            <Label Text="FullDuplex" FlexLayout.Basis="50%" />
            <Label Text="{Binding FullDuplex}" FlexLayout.Basis="50%" />
            <Label Text="Rate" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rate}" FlexLayout.Basis="50%" />
            <Label Text="Status" FlexLayout.Basis="50%" />
            <Label Text="{Binding Status}" FlexLayout.Basis="50%" />
            <Label Text="TxFlowControl" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxFlowControl}" FlexLayout.Basis="50%" />
            <Label Text="RxFlowControl" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxFlowControl}" FlexLayout.Basis="50%" />
            <Label Text="SfpModulePresent" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpModulePresent}" FlexLayout.Basis="50%" />
            <Label Text="SfpRxLose" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpRxLose}" FlexLayout.Basis="50%" />
            <Label Text="SfpTxFault" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpTxFault}" FlexLayout.Basis="50%" />
            <Label Text="SfpConnectorType" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpConnectorType}" FlexLayout.Basis="50%" />
            <Label Text="SfpLinkLengthCopper" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpLinkLengthCopper}" FlexLayout.Basis="50%" />
            <Label Text="SfpVendorName" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpVendorName}" FlexLayout.Basis="50%" />
            <Label Text="SfpVendorPartNumber" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpVendorPartNumber}" FlexLayout.Basis="50%" />
            <Label Text="SfpVendorRevision" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpVendorRevision}" FlexLayout.Basis="50%" />
            <Label Text="SfpVendorSerial" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpVendorSerial}" FlexLayout.Basis="50%" />
            <Label Text="SfpManufacturingDate" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpManufacturingDate}" FlexLayout.Basis="50%" />
            <Label Text="Eeprom" FlexLayout.Basis="50%" />
            <Label Text="{Binding Eeprom}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\EthernetMonitorPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class EthernetMonitorPage : ContentPage
    {
        public EthernetMonitorPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallAddressListDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallAddressListDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewall Address List">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/firewall/address-list"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <EntryCell Label="Timeout" Text="{Binding Entity.Timeout}" />
        <EntryCell Label="List" Text="{Binding Entity.List}" />
<!--
        <EntryCell Label="Firewall Address List" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewall Address List" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewall Address List"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewallAddressListDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallAddressListDetailPage : ContentPage
    {
        public FirewallAddressListDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallAddressListPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallAddressListPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/firewall/address-list"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Timeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding Timeout}" FlexLayout.Basis="50%" />
            <Label Text="List" FlexLayout.Basis="50%" />
            <Label Text="{Binding List}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewallAddressListPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallAddressListPage : ContentPage
    {
        public FirewallAddressListPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallConnectionDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallConnectionDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewall Connection">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/firewall/connection"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <SwitchCell Text="Assured" On="{Binding Entity.Assured}" />
        <EntryCell Label="Connection Mark" IsEnabled="False" Text="{Binding Entity.ConnectionMark}" />
        <EntryCell Label="Connection Type" IsEnabled="False" Text="{Binding Entity.ConnectionType}" />
        <EntryCell Label="Dst Address" IsEnabled="False" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Gre Key" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.GreKey}" />
        <EntryCell Label="Gre Version" IsEnabled="False" Text="{Binding Entity.GreVersion}" />
        <EntryCell Label="Icmp Code" IsEnabled="False" Text="{Binding Entity.IcmpCode}" />
        <EntryCell Label="Icmp Id" IsEnabled="False" Text="{Binding Entity.IcmpId}" />
        <EntryCell Label="Icmp Type" IsEnabled="False" Text="{Binding Entity.IcmpType}" />
        <SwitchCell Text="P 2p" On="{Binding Entity.P2p}" />
        <EntryCell Label="Protocol" IsEnabled="False" Text="{Binding Entity.Protocol}" />
        <EntryCell Label="Reply Dst Address" IsEnabled="False" Text="{Binding Entity.ReplyDstAddress}" />
        <EntryCell Label="Reply Src Address" IsEnabled="False" Text="{Binding Entity.ReplySrcAddress}" />
        <EntryCell Label="Src Address" IsEnabled="False" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Tcp State" IsEnabled="False" Text="{Binding Entity.TcpState}" />
        <EntryCell Label="Timeout" IsEnabled="False" Text="{Binding Entity.Timeout}" />
<!--
        <EntryCell Label="Firewall Connection" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewall Connection" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewall Connection"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewallConnectionDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallConnectionDetailPage : ContentPage
    {
        public FirewallConnectionDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallConnectionPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallConnectionPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/firewall/connection"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Assured" FlexLayout.Basis="50%" />
            <Label Text="{Binding Assured}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionMark}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionType" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionType}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="GreKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding GreKey}" FlexLayout.Basis="50%" />
            <Label Text="GreVersion" FlexLayout.Basis="50%" />
            <Label Text="{Binding GreVersion}" FlexLayout.Basis="50%" />
            <Label Text="IcmpCode" FlexLayout.Basis="50%" />
            <Label Text="{Binding IcmpCode}" FlexLayout.Basis="50%" />
            <Label Text="IcmpId" FlexLayout.Basis="50%" />
            <Label Text="{Binding IcmpId}" FlexLayout.Basis="50%" />
            <Label Text="IcmpType" FlexLayout.Basis="50%" />
            <Label Text="{Binding IcmpType}" FlexLayout.Basis="50%" />
            <Label Text="P2p" FlexLayout.Basis="50%" />
            <Label Text="{Binding P2p}" FlexLayout.Basis="50%" />
            <Label Text="Protocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding Protocol}" FlexLayout.Basis="50%" />
            <Label Text="ReplyDstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ReplyDstAddress}" FlexLayout.Basis="50%" />
            <Label Text="ReplySrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ReplySrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="TcpState" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpState}" FlexLayout.Basis="50%" />
            <Label Text="Timeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding Timeout}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewallConnectionPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallConnectionPage : ContentPage
    {
        public FirewallConnectionPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallFilterDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallFilterDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewall Filter">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/firewall/filter"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address List" Text="{Binding Entity.AddressList}" />
        <EntryCell Label="Address List Timeout" Text="{Binding Entity.AddressListTimeout}" />
        <EntryCell Label="Chain" Text="{Binding Entity.Chain}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Connection Bytes" Keyboard="Numeric" Text="{Binding Entity.ConnectionBytes}" />
        <EntryCell Label="Connection Limit" Keyboard="Numeric" Text="{Binding Entity.ConnectionLimit}" />
        <EntryCell Label="Connection Mark" Text="{Binding Entity.ConnectionMark}" />
        <EntryCell Label="Connection Rate" Keyboard="Numeric" Text="{Binding Entity.ConnectionRate}" />
        <EntryCell Label="Connection Type" Text="{Binding Entity.ConnectionType}" />
        <EntryCell Label="Content" Text="{Binding Entity.Content}" />
        <EntryCell Label="Dscp" Keyboard="Numeric" Text="{Binding Entity.Dscp}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Dst Address List" Text="{Binding Entity.DstAddressList}" />
        <EntryCell Label="Dst Address Type" Text="{Binding Entity.DstAddressType}" />
        <EntryCell Label="Dst Limit" Text="{Binding Entity.DstLimit}" />
        <EntryCell Label="Dst Port" Text="{Binding Entity.DstPort}" />
        <SwitchCell Text="Fragment" On="{Binding Entity.Fragment}" />
        <EntryCell Label="Hotspot" Text="{Binding Entity.Hotspot}" />
        <EntryCell Label="Icmp Options" Text="{Binding Entity.IcmpOptions}" />
        <EntryCell Label="In Bridge Port" Text="{Binding Entity.InBridgePort}" />
        <EntryCell Label="In Interface" Text="{Binding Entity.InInterface}" />
        <EntryCell Label="Ingress Priority" Keyboard="Numeric" Text="{Binding Entity.IngressPriority}" />
        <EntryCell Label="Ipv 4 Options" Text="{Binding Entity.Ipv4Options}" />
        <EntryCell Label="Jump Target" Text="{Binding Entity.JumpTarget}" />
        <EntryCell Label="Layer 7 Protocol" Text="{Binding Entity.Layer7Protocol}" />
        <EntryCell Label="Limit" Text="{Binding Entity.Limit}" />
        <EntryCell Label="Log Prefix" Text="{Binding Entity.LogPrefix}" />
        <EntryCell Label="Nth" Text="{Binding Entity.Nth}" />
        <EntryCell Label="Out Bridge Port" Text="{Binding Entity.OutBridgePort}" />
        <EntryCell Label="Out Interface" Text="{Binding Entity.OutInterface}" />
        <EntryCell Label="P 2p" Text="{Binding Entity.P2p}" />
        <EntryCell Label="Packet Mark" Text="{Binding Entity.PacketMark}" />
        <EntryCell Label="Packet Size" Text="{Binding Entity.PacketSize}" />
        <EntryCell Label="Per Connection Classifier" Text="{Binding Entity.PerConnectionClassifier}" />
        <EntryCell Label="Port" Text="{Binding Entity.Port}" />
        <EntryCell Label="Protocol" Text="{Binding Entity.Protocol}" />
        <EntryCell Label="Psd" Text="{Binding Entity.Psd}" />
        <EntryCell Label="Random" Text="{Binding Entity.Random}" />
        <EntryCell Label="Reject With" Text="{Binding Entity.RejectWith}" />
        <EntryCell Label="Routing Mark" Text="{Binding Entity.RoutingMark}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Src Address List" Text="{Binding Entity.SrcAddressList}" />
        <EntryCell Label="Src Address Type" Text="{Binding Entity.SrcAddressType}" />
        <EntryCell Label="Src Port" Text="{Binding Entity.SrcPort}" />
        <EntryCell Label="Src Mac Address" Text="{Binding Entity.SrcMacAddress}" />
        <EntryCell Label="Tcp Flags" Text="{Binding Entity.TcpFlags}" />
        <EntryCell Label="Tcp Mss" Text="{Binding Entity.TcpMss}" />
        <EntryCell Label="Time" Text="{Binding Entity.Time}" />
        <EntryCell Label="Ttl" Text="{Binding Entity.Ttl}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <EntryCell Label="Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Packets}" />
<!--
        <EntryCell Label="Firewall Filter" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewall Filter" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewall Filter"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewallFilterDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallFilterDetailPage : ContentPage
    {
        public FirewallFilterDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallFilterPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallFilterPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/firewall/filter"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Action" FlexLayout.Basis="50%" />
            <Label Text="{Binding Action}" FlexLayout.Basis="50%" />
            <Label Text="AddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressList}" FlexLayout.Basis="50%" />
            <Label Text="AddressListTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressListTimeout}" FlexLayout.Basis="50%" />
            <Label Text="Chain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Chain}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionBytes}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionLimit}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionMark}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionRate}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionState" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionState}" FlexLayout.Basis="50%" />
            <Label Text="ConnectionType" FlexLayout.Basis="50%" />
            <Label Text="{Binding ConnectionType}" FlexLayout.Basis="50%" />
            <Label Text="Content" FlexLayout.Basis="50%" />
            <Label Text="{Binding Content}" FlexLayout.Basis="50%" />
            <Label Text="Dscp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dscp}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstAddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddressList}" FlexLayout.Basis="50%" />
            <Label Text="DstAddressType" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddressType}" FlexLayout.Basis="50%" />
            <Label Text="DstLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstLimit}" FlexLayout.Basis="50%" />
            <Label Text="DstPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstPort}" FlexLayout.Basis="50%" />
            <Label Text="Fragment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Fragment}" FlexLayout.Basis="50%" />
            <Label Text="Hotspot" FlexLayout.Basis="50%" />
            <Label Text="{Binding Hotspot}" FlexLayout.Basis="50%" />
            <Label Text="IcmpOptions" FlexLayout.Basis="50%" />
            <Label Text="{Binding IcmpOptions}" FlexLayout.Basis="50%" />
            <Label Text="InBridgePort" FlexLayout.Basis="50%" />
            <Label Text="{Binding InBridgePort}" FlexLayout.Basis="50%" />
            <Label Text="InInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding InInterface}" FlexLayout.Basis="50%" />
            <Label Text="IngressPriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding IngressPriority}" FlexLayout.Basis="50%" />
            <Label Text="Ipv4Options" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ipv4Options}" FlexLayout.Basis="50%" />
            <Label Text="JumpTarget" FlexLayout.Basis="50%" />
            <Label Text="{Binding JumpTarget}" FlexLayout.Basis="50%" />
            <Label Text="Layer7Protocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding Layer7Protocol}" FlexLayout.Basis="50%" />
            <Label Text="Limit" FlexLayout.Basis="50%" />
            <Label Text="{Binding Limit}" FlexLayout.Basis="50%" />
            <Label Text="LogPrefix" FlexLayout.Basis="50%" />
            <Label Text="{Binding LogPrefix}" FlexLayout.Basis="50%" />
            <Label Text="Nth" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nth}" FlexLayout.Basis="50%" />
            <Label Text="OutBridgePort" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutBridgePort}" FlexLayout.Basis="50%" />
            <Label Text="OutInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutInterface}" FlexLayout.Basis="50%" />
            <Label Text="P2p" FlexLayout.Basis="50%" />
            <Label Text="{Binding P2p}" FlexLayout.Basis="50%" />
            <Label Text="PacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketMark}" FlexLayout.Basis="50%" />
            <Label Text="PacketSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketSize}" FlexLayout.Basis="50%" />
            <Label Text="PerConnectionClassifier" FlexLayout.Basis="50%" />
            <Label Text="{Binding PerConnectionClassifier}" FlexLayout.Basis="50%" />
            <Label Text="Port" FlexLayout.Basis="50%" />
            <Label Text="{Binding Port}" FlexLayout.Basis="50%" />
            <Label Text="Protocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding Protocol}" FlexLayout.Basis="50%" />
            <Label Text="Psd" FlexLayout.Basis="50%" />
            <Label Text="{Binding Psd}" FlexLayout.Basis="50%" />
            <Label Text="Random" FlexLayout.Basis="50%" />
            <Label Text="{Binding Random}" FlexLayout.Basis="50%" />
            <Label Text="RejectWith" FlexLayout.Basis="50%" />
            <Label Text="{Binding RejectWith}" FlexLayout.Basis="50%" />
            <Label Text="RoutingMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding RoutingMark}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddressList}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddressType" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddressType}" FlexLayout.Basis="50%" />
            <Label Text="SrcPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcPort}" FlexLayout.Basis="50%" />
            <Label Text="SrcMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="TcpFlags" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpFlags}" FlexLayout.Basis="50%" />
            <Label Text="TcpMss" FlexLayout.Basis="50%" />
            <Label Text="{Binding TcpMss}" FlexLayout.Basis="50%" />
            <Label Text="Time" FlexLayout.Basis="50%" />
            <Label Text="{Binding Time}" FlexLayout.Basis="50%" />
            <Label Text="Ttl" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ttl}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewallFilterPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallFilterPage : ContentPage
    {
        public FirewallFilterPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallMangleDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallMangleDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewall Mangle">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/firewall/mangle"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Chain" Text="{Binding Entity.Chain}" />
        <EntryCell Label="New Priority" Text="{Binding Entity.NewPriority}" />
        <SwitchCell Text="Passthrough" On="{Binding Entity.Passthrough}" />
        <EntryCell Label="Src Address List" Text="{Binding Entity.SrcAddressList}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="New Packet Mark" Text="{Binding Entity.NewPacketMark}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Dst Address List" Text="{Binding Entity.DstAddressList}" />
        <EntryCell Label="Protocol" Text="{Binding Entity.Protocol}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Jump Target" Text="{Binding Entity.JumpTarget}" />
        <EntryCell Label="Address List" Text="{Binding Entity.AddressList}" />
        <EntryCell Label="Address List Timeout" Text="{Binding Entity.AddressListTimeout}" />
<!--
        <EntryCell Label="Firewall Mangle" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewall Mangle" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewall Mangle"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewallMangleDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallMangleDetailPage : ContentPage
    {
        public FirewallMangleDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallManglePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallManglePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/firewall/mangle"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Chain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Chain}" FlexLayout.Basis="50%" />
            <Label Text="Action" FlexLayout.Basis="50%" />
            <Label Text="{Binding Action}" FlexLayout.Basis="50%" />
            <Label Text="NewPriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding NewPriority}" FlexLayout.Basis="50%" />
            <Label Text="Passthrough" FlexLayout.Basis="50%" />
            <Label Text="{Binding Passthrough}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddressList}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="NewPacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding NewPacketMark}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="DstAddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddressList}" FlexLayout.Basis="50%" />
            <Label Text="Protocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding Protocol}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="JumpTarget" FlexLayout.Basis="50%" />
            <Label Text="{Binding JumpTarget}" FlexLayout.Basis="50%" />
            <Label Text="AddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressList}" FlexLayout.Basis="50%" />
            <Label Text="AddressListTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressListTimeout}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewallManglePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallManglePage : ContentPage
    {
        public FirewallManglePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallNatDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallNatDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewall Nat">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/firewall/nat"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Chain" Text="{Binding Entity.Chain}" />
        <EntryCell Label="Action" Text="{Binding Entity.Action}" />
        <EntryCell Label="To Addresses" Text="{Binding Entity.ToAddresses}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Out Interface" Text="{Binding Entity.OutInterface}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Src Address List" Text="{Binding Entity.SrcAddressList}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="In Interface" Text="{Binding Entity.InInterface}" />
        <EntryCell Label="Protocol" Text="{Binding Entity.Protocol}" />
        <EntryCell Label="To Ports" Keyboard="Numeric" Text="{Binding Entity.ToPorts}" />
        <EntryCell Label="Dst Port" Keyboard="Numeric" Text="{Binding Entity.DstPort}" />
        <EntryCell Label="Src Port" Keyboard="Numeric" Text="{Binding Entity.SrcPort}" />
<!--
        <EntryCell Label="Firewall Nat" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewall Nat" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewall Nat"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewallNatDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallNatDetailPage : ContentPage
    {
        public FirewallNatDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewallNatPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewallNatPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/firewall/nat"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Chain" FlexLayout.Basis="50%" />
            <Label Text="{Binding Chain}" FlexLayout.Basis="50%" />
            <Label Text="Action" FlexLayout.Basis="50%" />
            <Label Text="{Binding Action}" FlexLayout.Basis="50%" />
            <Label Text="ToAddresses" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToAddresses}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="OutInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutInterface}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddressList}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="InInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding InInterface}" FlexLayout.Basis="50%" />
            <Label Text="Protocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding Protocol}" FlexLayout.Basis="50%" />
            <Label Text="ToPorts" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToPorts}" FlexLayout.Basis="50%" />
            <Label Text="DstPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstPort}" FlexLayout.Basis="50%" />
            <Label Text="SrcPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcPort}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewallNatPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewallNatPage : ContentPage
    {
        public FirewallNatPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewalServicePortDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewalServicePortDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Firewal Service Port">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/firewall/service-port"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Ports" Text="{Binding Entity.Ports}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Firewal Service Port" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Firewal Service Port" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Firewal Service Port"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\FirewalServicePortDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewalServicePortDetailPage : ContentPage
    {
        public FirewalServicePortDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\FirewalServicePortPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.FirewalServicePortPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/firewall/service-port"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Ports" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ports}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\FirewalServicePortPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class FirewalServicePortPage : ContentPage
    {
        public FirewalServicePortPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotActiveDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotActiveDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Hotspot Active">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/hotspot/active"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Server" IsEnabled="False" Text="{Binding Entity.Server}" />
        <EntryCell Label="Address" IsEnabled="False" Text="{Binding Entity.Address}" />
        <EntryCell Label="User Name" IsEnabled="False" Text="{Binding Entity.UserName}" />
        <EntryCell Label="Mac Address" IsEnabled="False" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Login By" IsEnabled="False" Text="{Binding Entity.LoginBy}" />
        <EntryCell Label="Up Time" IsEnabled="False" Text="{Binding Entity.UpTime}" />
        <EntryCell Label="Idle Time" IsEnabled="False" Text="{Binding Entity.IdleTime}" />
        <EntryCell Label="Session Time Left" IsEnabled="False" Text="{Binding Entity.SessionTimeLeft}" />
        <EntryCell Label="Idle Timeout" IsEnabled="False" Text="{Binding Entity.IdleTimeout}" />
        <EntryCell Label="Bytes In" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.BytesIn}" />
        <EntryCell Label="Bytes Out" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.BytesOut}" />
<!--
        <EntryCell Label="Hotspot Active" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Hotspot Active" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Hotspot Active"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\HotspotActiveDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotActiveDetailPage : ContentPage
    {
        public HotspotActiveDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotActivePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotActivePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/hotspot/active"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Server" FlexLayout.Basis="50%" />
            <Label Text="{Binding Server}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="UserName" FlexLayout.Basis="50%" />
            <Label Text="{Binding UserName}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="LoginBy" FlexLayout.Basis="50%" />
            <Label Text="{Binding LoginBy}" FlexLayout.Basis="50%" />
            <Label Text="UpTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding UpTime}" FlexLayout.Basis="50%" />
            <Label Text="IdleTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding IdleTime}" FlexLayout.Basis="50%" />
            <Label Text="SessionTimeLeft" FlexLayout.Basis="50%" />
            <Label Text="{Binding SessionTimeLeft}" FlexLayout.Basis="50%" />
            <Label Text="IdleTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding IdleTimeout}" FlexLayout.Basis="50%" />
            <Label Text="BytesIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding BytesIn}" FlexLayout.Basis="50%" />
            <Label Text="BytesOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding BytesOut}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\HotspotActivePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotActivePage : ContentPage
    {
        public HotspotActivePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotIpBindingDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotIpBindingDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Hotspot Ip Binding">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/hotspot/ip-binding"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Server" Text="{Binding Entity.Server}" />
        <EntryCell Label="To Address" Text="{Binding Entity.ToAddress}" />
        <EntryCell Label="Type" Text="{Binding Entity.Type}" />
<!--
        <EntryCell Label="Hotspot Ip Binding" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Hotspot Ip Binding" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Hotspot Ip Binding"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\HotspotIpBindingDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotIpBindingDetailPage : ContentPage
    {
        public HotspotIpBindingDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotIpBindingPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotIpBindingPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/hotspot/ip-binding"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="Server" FlexLayout.Basis="50%" />
            <Label Text="{Binding Server}" FlexLayout.Basis="50%" />
            <Label Text="ToAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding ToAddress}" FlexLayout.Basis="50%" />
            <Label Text="Type" FlexLayout.Basis="50%" />
            <Label Text="{Binding Type}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\HotspotIpBindingPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotIpBindingPage : ContentPage
    {
        public HotspotIpBindingPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotUserDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Hotspot User">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/hotspot/user"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Email" Text="{Binding Entity.Email}" />
        <EntryCell Label="Limit Bytes In" Keyboard="Numeric" Text="{Binding Entity.LimitBytesIn}" />
        <EntryCell Label="Limit Bytes Out" Keyboard="Numeric" Text="{Binding Entity.LimitBytesOut}" />
        <EntryCell Label="Limit Bytes Total" Keyboard="Numeric" Text="{Binding Entity.LimitBytesTotal}" />
        <EntryCell Label="Limit Uptime" Text="{Binding Entity.LimitUptime}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Password" Text="{Binding Entity.Password}" />
        <EntryCell Label="Profile" Text="{Binding Entity.Profile}" />
        <EntryCell Label="Routes" Text="{Binding Entity.Routes}" />
        <EntryCell Label="Server" Text="{Binding Entity.Server}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Bytes In" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.BytesIn}" />
        <EntryCell Label="Bytes Out" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.BytesOut}" />
        <EntryCell Label="Packets In" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.PacketsIn}" />
        <EntryCell Label="Packets Out" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.PacketsOut}" />
        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
<!--
        <EntryCell Label="Hotspot User" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Hotspot User" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Hotspot User"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotUserDetailPage : ContentPage
    {
        public HotspotUserDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotUserPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/hotspot/user"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Email" FlexLayout.Basis="50%" />
            <Label Text="{Binding Email}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesIn}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesOut}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesTotal" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesTotal}" FlexLayout.Basis="50%" />
            <Label Text="LimitUptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitUptime}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Password" FlexLayout.Basis="50%" />
            <Label Text="{Binding Password}" FlexLayout.Basis="50%" />
            <Label Text="Profile" FlexLayout.Basis="50%" />
            <Label Text="{Binding Profile}" FlexLayout.Basis="50%" />
            <Label Text="Routes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Routes}" FlexLayout.Basis="50%" />
            <Label Text="Server" FlexLayout.Basis="50%" />
            <Label Text="{Binding Server}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="BytesIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding BytesIn}" FlexLayout.Basis="50%" />
            <Label Text="BytesOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding BytesOut}" FlexLayout.Basis="50%" />
            <Label Text="PacketsIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketsIn}" FlexLayout.Basis="50%" />
            <Label Text="PacketsOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketsOut}" FlexLayout.Basis="50%" />
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotUserPage : ContentPage
    {
        public HotspotUserPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserProfileDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotUserProfileDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Hotspot User Profile">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/hotspot/user/profile"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <SwitchCell Text="Add Mac Cookie" On="{Binding Entity.AddMacCookie}" />
        <EntryCell Label="Address List" Text="{Binding Entity.AddressList}" />
        <EntryCell Label="Address Pool" Text="{Binding Entity.AddressPool}" />
        <SwitchCell Text="Advertise" On="{Binding Entity.Advertise}" />
        <EntryCell Label="Advertise Interval" Text="{Binding Entity.AdvertiseInterval}" />
        <EntryCell Label="Advertise Timeout" Text="{Binding Entity.AdvertiseTimeout}" />
        <EntryCell Label="Advertise Url" Text="{Binding Entity.AdvertiseUrl}" />
        <EntryCell Label="Idle Timeout" Text="{Binding Entity.IdleTimeout}" />
        <EntryCell Label="Incoming Filter" Text="{Binding Entity.IncomingFilter}" />
        <EntryCell Label="Incoming Packet Mark" Text="{Binding Entity.IncomingPacketMark}" />
        <EntryCell Label="Keepalive Timeout" Text="{Binding Entity.KeepaliveTimeout}" />
        <EntryCell Label="Mac Cookie Timeout" Text="{Binding Entity.MacCookieTimeout}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="On Login" Text="{Binding Entity.OnLogin}" />
        <EntryCell Label="On Logout" Text="{Binding Entity.OnLogout}" />
        <EntryCell Label="Open Status Page" Text="{Binding Entity.OpenStatusPage}" />
        <EntryCell Label="Outgoing Filter" Text="{Binding Entity.OutgoingFilter}" />
        <EntryCell Label="Outgoing Packet Mark" Text="{Binding Entity.OutgoingPacketMark}" />
        <EntryCell Label="Rate Limit" Text="{Binding Entity.RateLimit}" />
        <EntryCell Label="Session Timeout" Text="{Binding Entity.SessionTimeout}" />
        <EntryCell Label="Shared Users" Text="{Binding Entity.SharedUsers}" />
        <EntryCell Label="Status Autorefresh" Text="{Binding Entity.StatusAutorefresh}" />
        <SwitchCell Text="Transparent Proxy" On="{Binding Entity.TransparentProxy}" />
<!--
        <EntryCell Label="Hotspot User Profile" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Hotspot User Profile" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Hotspot User Profile"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserProfileDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotUserProfileDetailPage : ContentPage
    {
        public HotspotUserProfileDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserProfilePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.HotspotUserProfilePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/hotspot/user/profile"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AddMacCookie" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddMacCookie}" FlexLayout.Basis="50%" />
            <Label Text="AddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressList}" FlexLayout.Basis="50%" />
            <Label Text="AddressPool" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressPool}" FlexLayout.Basis="50%" />
            <Label Text="Advertise" FlexLayout.Basis="50%" />
            <Label Text="{Binding Advertise}" FlexLayout.Basis="50%" />
            <Label Text="AdvertiseInterval" FlexLayout.Basis="50%" />
            <Label Text="{Binding AdvertiseInterval}" FlexLayout.Basis="50%" />
            <Label Text="AdvertiseTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding AdvertiseTimeout}" FlexLayout.Basis="50%" />
            <Label Text="AdvertiseUrl" FlexLayout.Basis="50%" />
            <Label Text="{Binding AdvertiseUrl}" FlexLayout.Basis="50%" />
            <Label Text="IdleTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding IdleTimeout}" FlexLayout.Basis="50%" />
            <Label Text="IncomingFilter" FlexLayout.Basis="50%" />
            <Label Text="{Binding IncomingFilter}" FlexLayout.Basis="50%" />
            <Label Text="IncomingPacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding IncomingPacketMark}" FlexLayout.Basis="50%" />
            <Label Text="KeepaliveTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding KeepaliveTimeout}" FlexLayout.Basis="50%" />
            <Label Text="MacCookieTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacCookieTimeout}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="OnLogin" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnLogin}" FlexLayout.Basis="50%" />
            <Label Text="OnLogout" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnLogout}" FlexLayout.Basis="50%" />
            <Label Text="OpenStatusPage" FlexLayout.Basis="50%" />
            <Label Text="{Binding OpenStatusPage}" FlexLayout.Basis="50%" />
            <Label Text="OutgoingFilter" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutgoingFilter}" FlexLayout.Basis="50%" />
            <Label Text="OutgoingPacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutgoingPacketMark}" FlexLayout.Basis="50%" />
            <Label Text="RateLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding RateLimit}" FlexLayout.Basis="50%" />
            <Label Text="SessionTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding SessionTimeout}" FlexLayout.Basis="50%" />
            <Label Text="SharedUsers" FlexLayout.Basis="50%" />
            <Label Text="{Binding SharedUsers}" FlexLayout.Basis="50%" />
            <Label Text="StatusAutorefresh" FlexLayout.Basis="50%" />
            <Label Text="{Binding StatusAutorefresh}" FlexLayout.Basis="50%" />
            <Label Text="TransparentProxy" FlexLayout.Basis="50%" />
            <Label Text="{Binding TransparentProxy}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\HotspotUserProfilePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class HotspotUserProfilePage : ContentPage
    {
        public HotspotUserProfilePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceBridgeDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceBridgeDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Interface Bridge">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/bridge"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Admin Mac" Text="{Binding Entity.AdminMac}" />
        <EntryCell Label="Ageing Time" Text="{Binding Entity.AgeingTime}" />
        <SwitchCell Text="Auto Mac" On="{Binding Entity.AutoMac}" />
        <EntryCell Label="Forward Delay" Text="{Binding Entity.ForwardDelay}" />
        <EntryCell Label="L 2mtu" IsEnabled="False" Text="{Binding Entity.L2mtu}" />
        <EntryCell Label="Max Message Age" Text="{Binding Entity.MaxMessageAge}" />
        <EntryCell Label="Mtu" Text="{Binding Entity.Mtu}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Priority" Text="{Binding Entity.Priority}" />
        <EntryCell Label="Transmit Hold Count" Keyboard="Numeric" Text="{Binding Entity.TransmitHoldCount}" />
<!--
        <EntryCell Label="Interface Bridge" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Interface Bridge" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Interface Bridge"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceBridgeDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceBridgeDetailPage : ContentPage
    {
        public InterfaceBridgeDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceBridgePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceBridgePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/bridge"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AdminMac" FlexLayout.Basis="50%" />
            <Label Text="{Binding AdminMac}" FlexLayout.Basis="50%" />
            <Label Text="AgeingTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding AgeingTime}" FlexLayout.Basis="50%" />
            <Label Text="Arp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Arp}" FlexLayout.Basis="50%" />
            <Label Text="AutoMac" FlexLayout.Basis="50%" />
            <Label Text="{Binding AutoMac}" FlexLayout.Basis="50%" />
            <Label Text="ForwardDelay" FlexLayout.Basis="50%" />
            <Label Text="{Binding ForwardDelay}" FlexLayout.Basis="50%" />
            <Label Text="L2mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding L2mtu}" FlexLayout.Basis="50%" />
            <Label Text="MaxMessageAge" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxMessageAge}" FlexLayout.Basis="50%" />
            <Label Text="Mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mtu}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Priority" FlexLayout.Basis="50%" />
            <Label Text="{Binding Priority}" FlexLayout.Basis="50%" />
            <Label Text="ProtocolMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding ProtocolMode}" FlexLayout.Basis="50%" />
            <Label Text="TransmitHoldCount" FlexLayout.Basis="50%" />
            <Label Text="{Binding TransmitHoldCount}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\InterfaceBridgePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceBridgePage : ContentPage
    {
        public InterfaceBridgePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Interface">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/interface"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Default Name" IsEnabled="False" Text="{Binding Entity.DefaultName}" />
        <EntryCell Label="Type" Text="{Binding Entity.Type}" />
        <EntryCell Label="Mtu" Text="{Binding Entity.Mtu}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <SwitchCell Text="Fast Path" On="{Binding Entity.FastPath}" />
        <EntryCell Label="Rx Byte" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxByte}" />
        <EntryCell Label="Tx Byte" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxByte}" />
        <EntryCell Label="Rx Packet" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxPacket}" />
        <EntryCell Label="Tx Packet" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxPacket}" />
        <EntryCell Label="Rx Drop" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxDrop}" />
        <EntryCell Label="Tx Drop" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxDrop}" />
        <EntryCell Label="Rx Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxError}" />
        <EntryCell Label="Tx Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxError}" />
        <SwitchCell Text="Running" On="{Binding Entity.Running}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Last Link Down Time" Text="{Binding Entity.LastLinkDownTime}" />
        <EntryCell Label="Last Link Up Time" Text="{Binding Entity.LastLinkUpTime}" />
<!--
        <EntryCell Label="Interface" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Interface" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Interface"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceDetailPage : ContentPage
    {
        public InterfaceDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceEthernetDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceEthernetDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Interface Ethernet">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/ethernet"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Arp" Text="{Binding Entity.Arp}" />
        <SwitchCell Text="Auto Negotiation" On="{Binding Entity.AutoNegotiation}" />
        <EntryCell Label="Bandwidth" Text="{Binding Entity.Bandwidth}" />
        <EntryCell Label="Cable Setting" Text="{Binding Entity.CableSetting}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Disable Running Check" On="{Binding Entity.DisableRunningCheck}" />
        <SwitchCell Text="Full Duplex" On="{Binding Entity.FullDuplex}" />
        <EntryCell Label="L 2mtu" Keyboard="Numeric" Text="{Binding Entity.L2mtu}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Master Port" Text="{Binding Entity.MasterPort}" />
        <SwitchCell Text="Mdix Enable" On="{Binding Entity.MdixEnable}" />
        <EntryCell Label="Mtu" Keyboard="Numeric" Text="{Binding Entity.Mtu}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Orig Mac Address" Text="{Binding Entity.OrigMacAddress}" />
        <EntryCell Label="Poe Out" Text="{Binding Entity.PoeOut}" />
        <EntryCell Label="Poe Priority" Text="{Binding Entity.PoePriority}" />
        <EntryCell Label="Sfp Rate Select" Text="{Binding Entity.SfpRateSelect}" />
        <EntryCell Label="Speed" Text="{Binding Entity.Speed}" />
        <SwitchCell Text="Running" On="{Binding Entity.Running}" />
        <EntryCell Label="Rx 10241518" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx10241518}" />
        <EntryCell Label="Rx 128255" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx128255}" />
        <EntryCell Label="Rx 1519 Max" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx1519Max}" />
        <EntryCell Label="Rx 256511" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx256511}" />
        <EntryCell Label="Rx 5121023" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx5121023}" />
        <EntryCell Label="Rx 64" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx64}" />
        <EntryCell Label="Rx 65127" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx65127}" />
        <EntryCell Label="Rx Align Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxAlignError}" />
        <EntryCell Label="Rx Broadcast" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxBroadcast}" />
        <EntryCell Label="Rx Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxBytes}" />
        <EntryCell Label="Rx Fcs Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxFcsError}" />
        <EntryCell Label="Rx Fragment" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxFragment}" />
        <EntryCell Label="Rx Multicast" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxMulticast}" />
        <EntryCell Label="Rx Overflow" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxOverflow}" />
        <EntryCell Label="Rx Pause" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxPause}" />
        <EntryCell Label="Rx Runt" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxRunt}" />
        <EntryCell Label="Rx Too Long" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxTooLong}" />
        <SwitchCell Text="Slave" On="{Binding Entity.Slave}" />
        <EntryCell Label="Switch" IsEnabled="False" Text="{Binding Entity.Switch}" />
        <EntryCell Label="Tx 10241518" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx10241518}" />
        <EntryCell Label="Tx 128255" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx128255}" />
        <EntryCell Label="Tx 1519 Max" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx1519Max}" />
        <EntryCell Label="Tx 256511" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx256511}" />
        <EntryCell Label="Tx 5121023" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx5121023}" />
        <EntryCell Label="Tx 64" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx64}" />
        <EntryCell Label="Tx 65127" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx65127}" />
        <EntryCell Label="Tx Align Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxAlignError}" />
        <EntryCell Label="Tx Broadcast" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxBroadcast}" />
        <EntryCell Label="Tx Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxBytes}" />
        <EntryCell Label="Tx Fcs Error" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxFcsError}" />
        <EntryCell Label="Tx Fragment" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxFragment}" />
        <EntryCell Label="Tx Multicast" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxMulticast}" />
        <EntryCell Label="Tx Overflow" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxOverflow}" />
        <EntryCell Label="Tx Pause" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxPause}" />
        <EntryCell Label="Tx Runt" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxRunt}" />
        <EntryCell Label="Tx Too Long" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxTooLong}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Interface Ethernet" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Interface Ethernet" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Interface Ethernet"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceEthernetDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceEthernetDetailPage : ContentPage
    {
        public InterfaceEthernetDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceEthernetPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceEthernetPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/ethernet"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Arp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Arp}" FlexLayout.Basis="50%" />
            <Label Text="AutoNegotiation" FlexLayout.Basis="50%" />
            <Label Text="{Binding AutoNegotiation}" FlexLayout.Basis="50%" />
            <Label Text="Bandwidth" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bandwidth}" FlexLayout.Basis="50%" />
            <Label Text="CableSetting" FlexLayout.Basis="50%" />
            <Label Text="{Binding CableSetting}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="DisableRunningCheck" FlexLayout.Basis="50%" />
            <Label Text="{Binding DisableRunningCheck}" FlexLayout.Basis="50%" />
            <Label Text="FlowControlTx" FlexLayout.Basis="50%" />
            <Label Text="{Binding FlowControlTx}" FlexLayout.Basis="50%" />
            <Label Text="FlowControlRx" FlexLayout.Basis="50%" />
            <Label Text="{Binding FlowControlRx}" FlexLayout.Basis="50%" />
            <Label Text="FlowControlAuto" FlexLayout.Basis="50%" />
            <Label Text="{Binding FlowControlAuto}" FlexLayout.Basis="50%" />
            <Label Text="FullDuplex" FlexLayout.Basis="50%" />
            <Label Text="{Binding FullDuplex}" FlexLayout.Basis="50%" />
            <Label Text="L2mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding L2mtu}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="MasterPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding MasterPort}" FlexLayout.Basis="50%" />
            <Label Text="MdixEnable" FlexLayout.Basis="50%" />
            <Label Text="{Binding MdixEnable}" FlexLayout.Basis="50%" />
            <Label Text="Mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mtu}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="OrigMacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding OrigMacAddress}" FlexLayout.Basis="50%" />
            <Label Text="PoeOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding PoeOut}" FlexLayout.Basis="50%" />
            <Label Text="PoePriority" FlexLayout.Basis="50%" />
            <Label Text="{Binding PoePriority}" FlexLayout.Basis="50%" />
            <Label Text="SfpRateSelect" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfpRateSelect}" FlexLayout.Basis="50%" />
            <Label Text="Speed" FlexLayout.Basis="50%" />
            <Label Text="{Binding Speed}" FlexLayout.Basis="50%" />
            <Label Text="Running" FlexLayout.Basis="50%" />
            <Label Text="{Binding Running}" FlexLayout.Basis="50%" />
            <Label Text="Rx10241518" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx10241518}" FlexLayout.Basis="50%" />
            <Label Text="Rx128255" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx128255}" FlexLayout.Basis="50%" />
            <Label Text="Rx1519Max" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx1519Max}" FlexLayout.Basis="50%" />
            <Label Text="Rx256511" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx256511}" FlexLayout.Basis="50%" />
            <Label Text="Rx5121023" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx5121023}" FlexLayout.Basis="50%" />
            <Label Text="Rx64" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx64}" FlexLayout.Basis="50%" />
            <Label Text="Rx65127" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx65127}" FlexLayout.Basis="50%" />
            <Label Text="RxAlignError" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxAlignError}" FlexLayout.Basis="50%" />
            <Label Text="RxBroadcast" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxBroadcast}" FlexLayout.Basis="50%" />
            <Label Text="RxBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxBytes}" FlexLayout.Basis="50%" />
            <Label Text="RxFcsError" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxFcsError}" FlexLayout.Basis="50%" />
            <Label Text="RxFragment" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxFragment}" FlexLayout.Basis="50%" />
            <Label Text="RxMulticast" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxMulticast}" FlexLayout.Basis="50%" />
            <Label Text="RxOverflow" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxOverflow}" FlexLayout.Basis="50%" />
            <Label Text="RxPause" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxPause}" FlexLayout.Basis="50%" />
            <Label Text="RxRunt" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxRunt}" FlexLayout.Basis="50%" />
            <Label Text="RxTooLong" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxTooLong}" FlexLayout.Basis="50%" />
            <Label Text="Slave" FlexLayout.Basis="50%" />
            <Label Text="{Binding Slave}" FlexLayout.Basis="50%" />
            <Label Text="Switch" FlexLayout.Basis="50%" />
            <Label Text="{Binding Switch}" FlexLayout.Basis="50%" />
            <Label Text="Tx10241518" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx10241518}" FlexLayout.Basis="50%" />
            <Label Text="Tx128255" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx128255}" FlexLayout.Basis="50%" />
            <Label Text="Tx1519Max" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx1519Max}" FlexLayout.Basis="50%" />
            <Label Text="Tx256511" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx256511}" FlexLayout.Basis="50%" />
            <Label Text="Tx5121023" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx5121023}" FlexLayout.Basis="50%" />
            <Label Text="Tx64" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx64}" FlexLayout.Basis="50%" />
            <Label Text="Tx65127" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx65127}" FlexLayout.Basis="50%" />
            <Label Text="TxAlignError" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxAlignError}" FlexLayout.Basis="50%" />
            <Label Text="TxBroadcast" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxBroadcast}" FlexLayout.Basis="50%" />
            <Label Text="TxBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxBytes}" FlexLayout.Basis="50%" />
            <Label Text="TxFcsError" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxFcsError}" FlexLayout.Basis="50%" />
            <Label Text="TxFragment" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxFragment}" FlexLayout.Basis="50%" />
            <Label Text="TxMulticast" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxMulticast}" FlexLayout.Basis="50%" />
            <Label Text="TxOverflow" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxOverflow}" FlexLayout.Basis="50%" />
            <Label Text="TxPause" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPause}" FlexLayout.Basis="50%" />
            <Label Text="TxRunt" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxRunt}" FlexLayout.Basis="50%" />
            <Label Text="TxTooLong" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxTooLong}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\InterfaceEthernetPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceEthernetPage : ContentPage
    {
        public InterfaceEthernetPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceMonitorTrafficDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceMonitorTrafficDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Interface Monitor Traffic">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/interface/monitor-traffic"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Name" IsEnabled="False" Text="{Binding Entity.Name}" />
        <EntryCell Label="Rx Packets Per Second" IsEnabled="False" Text="{Binding Entity.RxPacketsPerSecond}" />
        <EntryCell Label="Rx Bits Per Second" IsEnabled="False" Text="{Binding Entity.RxBitsPerSecond}" />
        <EntryCell Label="Rx Drops Per Second" IsEnabled="False" Text="{Binding Entity.RxDropsPerSecond}" />
        <EntryCell Label="Rx Errors Per Second" IsEnabled="False" Text="{Binding Entity.RxErrorsPerSecond}" />
        <EntryCell Label="Tx Packets Per Second" IsEnabled="False" Text="{Binding Entity.TxPacketsPerSecond}" />
        <EntryCell Label="Tx Bits Per Second" IsEnabled="False" Text="{Binding Entity.TxBitsPerSecond}" />
        <EntryCell Label="Tx Drops Per Second" IsEnabled="False" Text="{Binding Entity.TxDropsPerSecond}" />
        <EntryCell Label="Tx Errors Per Second" IsEnabled="False" Text="{Binding Entity.TxErrorsPerSecond}" />
        <EntryCell Label="Tx Queue Drops Per Second" IsEnabled="False" Text="{Binding Entity.TxQueueDropsPerSecond}" />
<!--
        <EntryCell Label="Interface Monitor Traffic" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Interface Monitor Traffic" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Interface Monitor Traffic"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceMonitorTrafficDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceMonitorTrafficDetailPage : ContentPage
    {
        public InterfaceMonitorTrafficDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceMonitorTrafficPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceMonitorTrafficPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/interface/monitor-traffic"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="RxPacketsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxPacketsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="RxBitsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxBitsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="RxDropsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxDropsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="RxErrorsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxErrorsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="TxPacketsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPacketsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="TxBitsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxBitsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="TxDropsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxDropsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="TxErrorsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxErrorsPerSecond}" FlexLayout.Basis="50%" />
            <Label Text="TxQueueDropsPerSecond" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxQueueDropsPerSecond}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\InterfaceMonitorTrafficPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceMonitorTrafficPage : ContentPage
    {
        public InterfaceMonitorTrafficPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfacePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfacePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/interface"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="DefaultName" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultName}" FlexLayout.Basis="50%" />
            <Label Text="Type" FlexLayout.Basis="50%" />
            <Label Text="{Binding Type}" FlexLayout.Basis="50%" />
            <Label Text="Mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mtu}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="FastPath" FlexLayout.Basis="50%" />
            <Label Text="{Binding FastPath}" FlexLayout.Basis="50%" />
            <Label Text="RxByte" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxByte}" FlexLayout.Basis="50%" />
            <Label Text="TxByte" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxByte}" FlexLayout.Basis="50%" />
            <Label Text="RxPacket" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxPacket}" FlexLayout.Basis="50%" />
            <Label Text="TxPacket" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPacket}" FlexLayout.Basis="50%" />
            <Label Text="RxDrop" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxDrop}" FlexLayout.Basis="50%" />
            <Label Text="TxDrop" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxDrop}" FlexLayout.Basis="50%" />
            <Label Text="RxError" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxError}" FlexLayout.Basis="50%" />
            <Label Text="TxError" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxError}" FlexLayout.Basis="50%" />
            <Label Text="Running" FlexLayout.Basis="50%" />
            <Label Text="{Binding Running}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="LastLinkDownTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding LastLinkDownTime}" FlexLayout.Basis="50%" />
            <Label Text="LastLinkUpTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding LastLinkUpTime}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\InterfacePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfacePage : ContentPage
    {
        public InterfacePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceWirelessDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceWirelessDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Interface Wireless">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Adaptive Noise Immunity" Text="{Binding Entity.AdaptiveNoiseImmunity}" />
        <SwitchCell Text="Allow Sharedkey" On="{Binding Entity.AllowSharedkey}" />
        <EntryCell Label="Antenna Gain" Keyboard="Numeric" Text="{Binding Entity.AntennaGain}" />
        <EntryCell Label="Antenna Mode" Text="{Binding Entity.AntennaMode}" />
        <EntryCell Label="Area" Text="{Binding Entity.Area}" />
        <EntryCell Label="Arp" Text="{Binding Entity.Arp}" />
        <EntryCell Label="Band" Text="{Binding Entity.Band}" />
        <EntryCell Label="Basic Rates AG" Text="{Binding Entity.BasicRatesAG}" />
        <EntryCell Label="Basic Rates B" Text="{Binding Entity.BasicRatesB}" />
        <EntryCell Label="Bridge Mode" Text="{Binding Entity.BridgeMode}" />
        <EntryCell Label="Burst Time" Text="{Binding Entity.BurstTime}" />
        <EntryCell Label="Channel Width" Text="{Binding Entity.ChannelWidth}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Compression" On="{Binding Entity.Compression}" />
        <EntryCell Label="Country" Text="{Binding Entity.Country}" />
        <EntryCell Label="Default Ap Tx Limit" Keyboard="Numeric" Text="{Binding Entity.DefaultApTxLimit}" />
        <SwitchCell Text="Default Authentication" On="{Binding Entity.DefaultAuthentication}" />
        <EntryCell Label="Default Client Tx Limit" Keyboard="Numeric" Text="{Binding Entity.DefaultClientTxLimit}" />
        <SwitchCell Text="Default Forwarding" On="{Binding Entity.DefaultForwarding}" />
        <EntryCell Label="Dfs Mode" Text="{Binding Entity.DfsMode}" />
        <SwitchCell Text="Disable Running Check" On="{Binding Entity.DisableRunningCheck}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Disconnect Timeout" Text="{Binding Entity.DisconnectTimeout}" />
        <EntryCell Label="Distance" Text="{Binding Entity.Distance}" />
        <EntryCell Label="Frame Lifetime" Keyboard="Numeric" Text="{Binding Entity.FrameLifetime}" />
        <EntryCell Label="Frequency" Text="{Binding Entity.Frequency}" />
        <EntryCell Label="Frequency Mode" Text="{Binding Entity.FrequencyMode}" />
        <EntryCell Label="Frequency Offset" Keyboard="Numeric" Text="{Binding Entity.FrequencyOffset}" />
        <SwitchCell Text="Hide Ssid" On="{Binding Entity.HideSsid}" />
        <EntryCell Label="Ht Ampdu Priorities" Text="{Binding Entity.HtAmpduPriorities}" />
        <EntryCell Label="Ht Amsdu Limit" Text="{Binding Entity.HtAmsduLimit}" />
        <EntryCell Label="Ht Amsdu Threshold" Text="{Binding Entity.HtAmsduThreshold}" />
        <EntryCell Label="Ht Basic Mcs" Text="{Binding Entity.HtBasicMcs}" />
        <EntryCell Label="Ht Guard Interval" Text="{Binding Entity.HtGuardInterval}" />
        <EntryCell Label="Ht Rxchains" Text="{Binding Entity.HtRxchains}" />
        <EntryCell Label="Ht Supported Mcs" Text="{Binding Entity.HtSupportedMcs}" />
        <EntryCell Label="Ht Txchains" Text="{Binding Entity.HtTxchains}" />
        <EntryCell Label="Hw Fragmentation Threshold" Text="{Binding Entity.HwFragmentationThreshold}" />
        <EntryCell Label="Hw Protection Mode" Text="{Binding Entity.HwProtectionMode}" />
        <EntryCell Label="Hw Protection Threshold" Keyboard="Numeric" Text="{Binding Entity.HwProtectionThreshold}" />
        <EntryCell Label="Hw Retries" Keyboard="Numeric" Text="{Binding Entity.HwRetries}" />
        <EntryCell Label="L 2mtu" Keyboard="Numeric" Text="{Binding Entity.L2mtu}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Master Interface" Text="{Binding Entity.MasterInterface}" />
        <EntryCell Label="Max Station Count" Keyboard="Numeric" Text="{Binding Entity.MaxStationCount}" />
        <EntryCell Label="Mtu" Keyboard="Numeric" Text="{Binding Entity.Mtu}" />
        <EntryCell Label="Multicast Helper" Text="{Binding Entity.MulticastHelper}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Noise Floor Threshold" Text="{Binding Entity.NoiseFloorThreshold}" />
        <EntryCell Label="Nv 2 Cell Radius" Keyboard="Numeric" Text="{Binding Entity.Nv2CellRadius}" />
        <EntryCell Label="Nv 2 Noise Floor Offset" Text="{Binding Entity.Nv2NoiseFloorOffset}" />
        <EntryCell Label="Nv 2 Preshared Key" Text="{Binding Entity.Nv2PresharedKey}" />
        <EntryCell Label="Nv 2 Qos" Text="{Binding Entity.Nv2Qos}" />
        <EntryCell Label="Nv 2 Queue Count" Text="{Binding Entity.Nv2QueueCount}" />
        <EntryCell Label="Nv 2 Security" Text="{Binding Entity.Nv2Security}" />
        <EntryCell Label="On Fail Retry Time" Text="{Binding Entity.OnFailRetryTime}" />
        <EntryCell Label="Periodic Calibration" Text="{Binding Entity.PeriodicCalibration}" />
        <EntryCell Label="Periodic Calibration Interval" Keyboard="Numeric" Text="{Binding Entity.PeriodicCalibrationInterval}" />
        <EntryCell Label="Prism Cardtype" Text="{Binding Entity.PrismCardtype}" />
        <EntryCell Label="Proprietary Extension" Text="{Binding Entity.ProprietaryExtension}" />
        <EntryCell Label="Radio Name" Text="{Binding Entity.RadioName}" />
        <EntryCell Label="Rate Selection" Text="{Binding Entity.RateSelection}" />
        <EntryCell Label="Rate Set" Text="{Binding Entity.RateSet}" />
        <EntryCell Label="Scan List" Text="{Binding Entity.ScanList}" />
        <EntryCell Label="Security Profile" Text="{Binding Entity.SecurityProfile}" />
        <EntryCell Label="Ssid" Text="{Binding Entity.Ssid}" />
        <EntryCell Label="Station Bridge Clone Mac" Text="{Binding Entity.StationBridgeCloneMac}" />
        <EntryCell Label="Supported Rates AG" Text="{Binding Entity.SupportedRatesAG}" />
        <EntryCell Label="Supported Rates B" Text="{Binding Entity.SupportedRatesB}" />
        <EntryCell Label="Tdma Debug" Keyboard="Numeric" Text="{Binding Entity.TdmaDebug}" />
        <EntryCell Label="Tdma Hw Test Mode" Keyboard="Numeric" Text="{Binding Entity.TdmaHwTestMode}" />
        <EntryCell Label="Tdma Override Rate" Text="{Binding Entity.TdmaOverrideRate}" />
        <EntryCell Label="Tdma Override Size" Keyboard="Numeric" Text="{Binding Entity.TdmaOverrideSize}" />
        <EntryCell Label="Tdma Period Size" Keyboard="Numeric" Text="{Binding Entity.TdmaPeriodSize}" />
        <EntryCell Label="Tdma Test Mode" Keyboard="Numeric" Text="{Binding Entity.TdmaTestMode}" />
        <EntryCell Label="Tx Power" Keyboard="Numeric" Text="{Binding Entity.TxPower}" />
        <EntryCell Label="Update Stats Interval" Text="{Binding Entity.UpdateStatsInterval}" />
        <EntryCell Label="Vht Basic Mcs" Text="{Binding Entity.VhtBasicMcs}" />
        <EntryCell Label="Vht Supported Mcs" Text="{Binding Entity.VhtSupportedMcs}" />
        <EntryCell Label="Wds Cost Range" Text="{Binding Entity.WdsCostRange}" />
        <EntryCell Label="Wds Default Bridge" Text="{Binding Entity.WdsDefaultBridge}" />
        <EntryCell Label="Wds Default Cost" Text="{Binding Entity.WdsDefaultCost}" />
        <SwitchCell Text="Wds Ignore Ssid" On="{Binding Entity.WdsIgnoreSsid}" />
        <EntryCell Label="Wds Mode" Text="{Binding Entity.WdsMode}" />
        <EntryCell Label="Wmm Support" Text="{Binding Entity.WmmSupport}" />
<!--
        <EntryCell Label="Interface Wireless" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Interface Wireless" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Interface Wireless"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceWirelessDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceWirelessDetailPage : ContentPage
    {
        public InterfaceWirelessDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\InterfaceWirelessPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.InterfaceWirelessPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AdaptiveNoiseImmunity" FlexLayout.Basis="50%" />
            <Label Text="{Binding AdaptiveNoiseImmunity}" FlexLayout.Basis="50%" />
            <Label Text="AllowSharedkey" FlexLayout.Basis="50%" />
            <Label Text="{Binding AllowSharedkey}" FlexLayout.Basis="50%" />
            <Label Text="AntennaGain" FlexLayout.Basis="50%" />
            <Label Text="{Binding AntennaGain}" FlexLayout.Basis="50%" />
            <Label Text="AntennaMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding AntennaMode}" FlexLayout.Basis="50%" />
            <Label Text="Area" FlexLayout.Basis="50%" />
            <Label Text="{Binding Area}" FlexLayout.Basis="50%" />
            <Label Text="Arp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Arp}" FlexLayout.Basis="50%" />
            <Label Text="Band" FlexLayout.Basis="50%" />
            <Label Text="{Binding Band}" FlexLayout.Basis="50%" />
            <Label Text="BasicRatesAG" FlexLayout.Basis="50%" />
            <Label Text="{Binding BasicRatesAG}" FlexLayout.Basis="50%" />
            <Label Text="BasicRatesB" FlexLayout.Basis="50%" />
            <Label Text="{Binding BasicRatesB}" FlexLayout.Basis="50%" />
            <Label Text="BridgeMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding BridgeMode}" FlexLayout.Basis="50%" />
            <Label Text="BurstTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstTime}" FlexLayout.Basis="50%" />
            <Label Text="ChannelWidth" FlexLayout.Basis="50%" />
            <Label Text="{Binding ChannelWidth}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Compression" FlexLayout.Basis="50%" />
            <Label Text="{Binding Compression}" FlexLayout.Basis="50%" />
            <Label Text="Country" FlexLayout.Basis="50%" />
            <Label Text="{Binding Country}" FlexLayout.Basis="50%" />
            <Label Text="DefaultApTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultApTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="DefaultAuthentication" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultAuthentication}" FlexLayout.Basis="50%" />
            <Label Text="DefaultClientTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultClientTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="DefaultForwarding" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultForwarding}" FlexLayout.Basis="50%" />
            <Label Text="DfsMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding DfsMode}" FlexLayout.Basis="50%" />
            <Label Text="DisableRunningCheck" FlexLayout.Basis="50%" />
            <Label Text="{Binding DisableRunningCheck}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="DisconnectTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding DisconnectTimeout}" FlexLayout.Basis="50%" />
            <Label Text="Distance" FlexLayout.Basis="50%" />
            <Label Text="{Binding Distance}" FlexLayout.Basis="50%" />
            <Label Text="FrameLifetime" FlexLayout.Basis="50%" />
            <Label Text="{Binding FrameLifetime}" FlexLayout.Basis="50%" />
            <Label Text="Frequency" FlexLayout.Basis="50%" />
            <Label Text="{Binding Frequency}" FlexLayout.Basis="50%" />
            <Label Text="FrequencyMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding FrequencyMode}" FlexLayout.Basis="50%" />
            <Label Text="FrequencyOffset" FlexLayout.Basis="50%" />
            <Label Text="{Binding FrequencyOffset}" FlexLayout.Basis="50%" />
            <Label Text="HideSsid" FlexLayout.Basis="50%" />
            <Label Text="{Binding HideSsid}" FlexLayout.Basis="50%" />
            <Label Text="HtAmpduPriorities" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtAmpduPriorities}" FlexLayout.Basis="50%" />
            <Label Text="HtAmsduLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtAmsduLimit}" FlexLayout.Basis="50%" />
            <Label Text="HtAmsduThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtAmsduThreshold}" FlexLayout.Basis="50%" />
            <Label Text="HtBasicMcs" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtBasicMcs}" FlexLayout.Basis="50%" />
            <Label Text="HtGuardInterval" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtGuardInterval}" FlexLayout.Basis="50%" />
            <Label Text="HtRxchains" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtRxchains}" FlexLayout.Basis="50%" />
            <Label Text="HtSupportedMcs" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtSupportedMcs}" FlexLayout.Basis="50%" />
            <Label Text="HtTxchains" FlexLayout.Basis="50%" />
            <Label Text="{Binding HtTxchains}" FlexLayout.Basis="50%" />
            <Label Text="HwFragmentationThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwFragmentationThreshold}" FlexLayout.Basis="50%" />
            <Label Text="HwProtectionMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwProtectionMode}" FlexLayout.Basis="50%" />
            <Label Text="HwProtectionThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwProtectionThreshold}" FlexLayout.Basis="50%" />
            <Label Text="HwRetries" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwRetries}" FlexLayout.Basis="50%" />
            <Label Text="L2mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding L2mtu}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="MasterInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding MasterInterface}" FlexLayout.Basis="50%" />
            <Label Text="MaxStationCount" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxStationCount}" FlexLayout.Basis="50%" />
            <Label Text="Mode" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mode}" FlexLayout.Basis="50%" />
            <Label Text="Mtu" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mtu}" FlexLayout.Basis="50%" />
            <Label Text="MulticastHelper" FlexLayout.Basis="50%" />
            <Label Text="{Binding MulticastHelper}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="NoiseFloorThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding NoiseFloorThreshold}" FlexLayout.Basis="50%" />
            <Label Text="Nv2CellRadius" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2CellRadius}" FlexLayout.Basis="50%" />
            <Label Text="Nv2NoiseFloorOffset" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2NoiseFloorOffset}" FlexLayout.Basis="50%" />
            <Label Text="Nv2PresharedKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2PresharedKey}" FlexLayout.Basis="50%" />
            <Label Text="Nv2Qos" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2Qos}" FlexLayout.Basis="50%" />
            <Label Text="Nv2QueueCount" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2QueueCount}" FlexLayout.Basis="50%" />
            <Label Text="Nv2Security" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nv2Security}" FlexLayout.Basis="50%" />
            <Label Text="OnFailRetryTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnFailRetryTime}" FlexLayout.Basis="50%" />
            <Label Text="PeriodicCalibration" FlexLayout.Basis="50%" />
            <Label Text="{Binding PeriodicCalibration}" FlexLayout.Basis="50%" />
            <Label Text="PeriodicCalibrationInterval" FlexLayout.Basis="50%" />
            <Label Text="{Binding PeriodicCalibrationInterval}" FlexLayout.Basis="50%" />
            <Label Text="PreambleMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding PreambleMode}" FlexLayout.Basis="50%" />
            <Label Text="PrismCardtype" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrismCardtype}" FlexLayout.Basis="50%" />
            <Label Text="ProprietaryExtension" FlexLayout.Basis="50%" />
            <Label Text="{Binding ProprietaryExtension}" FlexLayout.Basis="50%" />
            <Label Text="RadioName" FlexLayout.Basis="50%" />
            <Label Text="{Binding RadioName}" FlexLayout.Basis="50%" />
            <Label Text="RateSelection" FlexLayout.Basis="50%" />
            <Label Text="{Binding RateSelection}" FlexLayout.Basis="50%" />
            <Label Text="RateSet" FlexLayout.Basis="50%" />
            <Label Text="{Binding RateSet}" FlexLayout.Basis="50%" />
            <Label Text="ScanList" FlexLayout.Basis="50%" />
            <Label Text="{Binding ScanList}" FlexLayout.Basis="50%" />
            <Label Text="SecurityProfile" FlexLayout.Basis="50%" />
            <Label Text="{Binding SecurityProfile}" FlexLayout.Basis="50%" />
            <Label Text="Ssid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ssid}" FlexLayout.Basis="50%" />
            <Label Text="StationBridgeCloneMac" FlexLayout.Basis="50%" />
            <Label Text="{Binding StationBridgeCloneMac}" FlexLayout.Basis="50%" />
            <Label Text="SupportedRatesAG" FlexLayout.Basis="50%" />
            <Label Text="{Binding SupportedRatesAG}" FlexLayout.Basis="50%" />
            <Label Text="SupportedRatesB" FlexLayout.Basis="50%" />
            <Label Text="{Binding SupportedRatesB}" FlexLayout.Basis="50%" />
            <Label Text="TdmaDebug" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaDebug}" FlexLayout.Basis="50%" />
            <Label Text="TdmaHwTestMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaHwTestMode}" FlexLayout.Basis="50%" />
            <Label Text="TdmaOverrideRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaOverrideRate}" FlexLayout.Basis="50%" />
            <Label Text="TdmaOverrideSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaOverrideSize}" FlexLayout.Basis="50%" />
            <Label Text="TdmaPeriodSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaPeriodSize}" FlexLayout.Basis="50%" />
            <Label Text="TdmaTestMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaTestMode}" FlexLayout.Basis="50%" />
            <Label Text="TxPower" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPower}" FlexLayout.Basis="50%" />
            <Label Text="TxPowerMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPowerMode}" FlexLayout.Basis="50%" />
            <Label Text="UpdateStatsInterval" FlexLayout.Basis="50%" />
            <Label Text="{Binding UpdateStatsInterval}" FlexLayout.Basis="50%" />
            <Label Text="VhtBasicMcs" FlexLayout.Basis="50%" />
            <Label Text="{Binding VhtBasicMcs}" FlexLayout.Basis="50%" />
            <Label Text="VhtSupportedMcs" FlexLayout.Basis="50%" />
            <Label Text="{Binding VhtSupportedMcs}" FlexLayout.Basis="50%" />
            <Label Text="WdsCostRange" FlexLayout.Basis="50%" />
            <Label Text="{Binding WdsCostRange}" FlexLayout.Basis="50%" />
            <Label Text="WdsDefaultBridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding WdsDefaultBridge}" FlexLayout.Basis="50%" />
            <Label Text="WdsDefaultCost" FlexLayout.Basis="50%" />
            <Label Text="{Binding WdsDefaultCost}" FlexLayout.Basis="50%" />
            <Label Text="WdsIgnoreSsid" FlexLayout.Basis="50%" />
            <Label Text="{Binding WdsIgnoreSsid}" FlexLayout.Basis="50%" />
            <Label Text="WdsMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding WdsMode}" FlexLayout.Basis="50%" />
            <Label Text="WirelessProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding WirelessProtocol}" FlexLayout.Basis="50%" />
            <Label Text="WmmSupport" FlexLayout.Basis="50%" />
            <Label Text="{Binding WmmSupport}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\InterfaceWirelessPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class InterfaceWirelessPage : ContentPage
    {
        public InterfaceWirelessPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpAccountingDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpAccountingDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Accounting">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/accounting"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Account Local Traffic" Text="{Binding Entity.AccountLocalTraffic}" />
        <EntryCell Label="Enabled" Text="{Binding Entity.Enabled}" />
        <EntryCell Label="Threshold" Keyboard="Numeric" Text="{Binding Entity.Threshold}" />
<!--
        <EntryCell Label="Ip Accounting" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Accounting" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Accounting"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpAccountingDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpAccountingDetailPage : ContentPage
    {
        public IpAccountingDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpAccountingPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpAccountingPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/accounting"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="AccountLocalTraffic" FlexLayout.Basis="50%" />
            <Label Text="{Binding AccountLocalTraffic}" FlexLayout.Basis="50%" />
            <Label Text="Enabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Enabled}" FlexLayout.Basis="50%" />
            <Label Text="Threshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding Threshold}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpAccountingPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpAccountingPage : ContentPage
    {
        public IpAccountingPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpAddressDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpAddressDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Address">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/address"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Actual Interface" IsEnabled="False" Text="{Binding Entity.ActualInterface}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Broadcast" Text="{Binding Entity.Broadcast}" />
        <EntryCell Label="Network" Text="{Binding Entity.Network}" />
        <EntryCell Label="Netmask" Text="{Binding Entity.Netmask}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
<!--
        <EntryCell Label="Ip Address" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Address" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Address"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpAddressDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpAddressDetailPage : ContentPage
    {
        public IpAddressDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpAddressPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpAddressPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/address"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="ActualInterface" FlexLayout.Basis="50%" />
            <Label Text="{Binding ActualInterface}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="Broadcast" FlexLayout.Basis="50%" />
            <Label Text="{Binding Broadcast}" FlexLayout.Basis="50%" />
            <Label Text="Network" FlexLayout.Basis="50%" />
            <Label Text="{Binding Network}" FlexLayout.Basis="50%" />
            <Label Text="Netmask" FlexLayout.Basis="50%" />
            <Label Text="{Binding Netmask}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpAddressPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpAddressPage : ContentPage
    {
        public IpAddressPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpArpDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpArpDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Arp">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/arp"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" Text="{Binding Entity.Address}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <SwitchCell Text="Dhcp" On="{Binding Entity.Dhcp}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
<!--
        <EntryCell Label="Ip Arp" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Arp" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Arp"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpArpDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpArpDetailPage : ContentPage
    {
        public IpArpDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpArpPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpArpPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/arp"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="Dhcp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dhcp}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpArpPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpArpPage : ContentPage
    {
        public IpArpPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpClientDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpClientDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Dhcp Client">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-client"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Client Id" Text="{Binding Entity.ClientId}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Default Route Distance" Text="{Binding Entity.DefaultRouteDistance}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Host Name" Text="{Binding Entity.HostName}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <SwitchCell Text="Use Peer Dns" On="{Binding Entity.UsePeerDns}" />
        <SwitchCell Text="Use Peer Ntp" On="{Binding Entity.UsePeerNtp}" />
        <EntryCell Label="Address" IsEnabled="False" Text="{Binding Entity.Address}" />
        <EntryCell Label="Dhcp Server" IsEnabled="False" Text="{Binding Entity.DhcpServer}" />
        <EntryCell Label="Expires After" IsEnabled="False" Text="{Binding Entity.ExpiresAfter}" />
        <EntryCell Label="Gateway" IsEnabled="False" Text="{Binding Entity.Gateway}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <EntryCell Label="Netmask" IsEnabled="False" Text="{Binding Entity.Netmask}" />
        <EntryCell Label="Primary Dns" IsEnabled="False" Text="{Binding Entity.PrimaryDns}" />
        <EntryCell Label="Primary Ntp" IsEnabled="False" Text="{Binding Entity.PrimaryNtp}" />
        <EntryCell Label="Secondary Dns" IsEnabled="False" Text="{Binding Entity.SecondaryDns}" />
        <EntryCell Label="Secondary Ntp" IsEnabled="False" Text="{Binding Entity.SecondaryNtp}" />
        <EntryCell Label="Status" IsEnabled="False" Text="{Binding Entity.Status}" />
<!--
        <EntryCell Label="Ip Dhcp Client" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Dhcp Client" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Dhcp Client"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpClientDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpClientDetailPage : ContentPage
    {
        public IpDhcpClientDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpClientPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpClientPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-client"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AddDefaultRoute" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddDefaultRoute}" FlexLayout.Basis="50%" />
            <Label Text="ClientId" FlexLayout.Basis="50%" />
            <Label Text="{Binding ClientId}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="DefaultRouteDistance" FlexLayout.Basis="50%" />
            <Label Text="{Binding DefaultRouteDistance}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="HostName" FlexLayout.Basis="50%" />
            <Label Text="{Binding HostName}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="UsePeerDns" FlexLayout.Basis="50%" />
            <Label Text="{Binding UsePeerDns}" FlexLayout.Basis="50%" />
            <Label Text="UsePeerNtp" FlexLayout.Basis="50%" />
            <Label Text="{Binding UsePeerNtp}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="DhcpServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding DhcpServer}" FlexLayout.Basis="50%" />
            <Label Text="ExpiresAfter" FlexLayout.Basis="50%" />
            <Label Text="{Binding ExpiresAfter}" FlexLayout.Basis="50%" />
            <Label Text="Gateway" FlexLayout.Basis="50%" />
            <Label Text="{Binding Gateway}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Netmask" FlexLayout.Basis="50%" />
            <Label Text="{Binding Netmask}" FlexLayout.Basis="50%" />
            <Label Text="PrimaryDns" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrimaryDns}" FlexLayout.Basis="50%" />
            <Label Text="PrimaryNtp" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrimaryNtp}" FlexLayout.Basis="50%" />
            <Label Text="SecondaryDns" FlexLayout.Basis="50%" />
            <Label Text="{Binding SecondaryDns}" FlexLayout.Basis="50%" />
            <Label Text="SecondaryNtp" FlexLayout.Basis="50%" />
            <Label Text="{Binding SecondaryNtp}" FlexLayout.Basis="50%" />
            <Label Text="Status" FlexLayout.Basis="50%" />
            <Label Text="{Binding Status}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpClientPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpClientPage : ContentPage
    {
        public IpDhcpClientPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpRelayDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpRelayDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Dhcp Relay">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-relay"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Add Relay Info" Text="{Binding Entity.AddRelayInfo}" />
        <EntryCell Label="Delay Threshold" Text="{Binding Entity.DelayThreshold}" />
        <EntryCell Label="Dhcp Server" Text="{Binding Entity.DhcpServer}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Local Address" Text="{Binding Entity.LocalAddress}" />
        <EntryCell Label="Relay Info Remote Id" Text="{Binding Entity.RelayInfoRemoteId}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
<!--
        <EntryCell Label="Ip Dhcp Relay" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Dhcp Relay" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Dhcp Relay"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpRelayDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpRelayDetailPage : ContentPage
    {
        public IpDhcpRelayDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpRelayPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpRelayPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-relay"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AddRelayInfo" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddRelayInfo}" FlexLayout.Basis="50%" />
            <Label Text="DelayThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding DelayThreshold}" FlexLayout.Basis="50%" />
            <Label Text="DhcpServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding DhcpServer}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="LocalAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding LocalAddress}" FlexLayout.Basis="50%" />
            <Label Text="RelayInfoRemoteId" FlexLayout.Basis="50%" />
            <Label Text="{Binding RelayInfoRemoteId}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpRelayPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpRelayPage : ContentPage
    {
        public IpDhcpRelayPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpServerDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpServerDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Dhcp Server">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dhcp-server"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <SwitchCell Text="Add Arp" On="{Binding Entity.AddArp}" />
        <EntryCell Label="Address Pool" Text="{Binding Entity.AddressPool}" />
        <SwitchCell Text="Always Broadcast" On="{Binding Entity.AlwaysBroadcast}" />
        <EntryCell Label="Delay Threshold" Text="{Binding Entity.DelayThreshold}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Lease Script" Text="{Binding Entity.LeaseScript}" />
        <EntryCell Label="Lease Time" Text="{Binding Entity.LeaseTime}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Relay" Text="{Binding Entity.Relay}" />
        <EntryCell Label="Src Address" Text="{Binding Entity.SrcAddress}" />
        <SwitchCell Text="Use Radius" On="{Binding Entity.UseRadius}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
<!--
        <EntryCell Label="Ip Dhcp Server" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Dhcp Server" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Dhcp Server"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpServerDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpServerDetailPage : ContentPage
    {
        public IpDhcpServerDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpServerPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDhcpServerPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dhcp-server"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AddArp" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddArp}" FlexLayout.Basis="50%" />
            <Label Text="AddressPool" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressPool}" FlexLayout.Basis="50%" />
            <Label Text="AlwaysBroadcast" FlexLayout.Basis="50%" />
            <Label Text="{Binding AlwaysBroadcast}" FlexLayout.Basis="50%" />
            <Label Text="Authoritative" FlexLayout.Basis="50%" />
            <Label Text="{Binding Authoritative}" FlexLayout.Basis="50%" />
            <Label Text="BootpSupport" FlexLayout.Basis="50%" />
            <Label Text="{Binding BootpSupport}" FlexLayout.Basis="50%" />
            <Label Text="DelayThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding DelayThreshold}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="LeaseScript" FlexLayout.Basis="50%" />
            <Label Text="{Binding LeaseScript}" FlexLayout.Basis="50%" />
            <Label Text="LeaseTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding LeaseTime}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Relay" FlexLayout.Basis="50%" />
            <Label Text="{Binding Relay}" FlexLayout.Basis="50%" />
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="UseRadius" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseRadius}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpDhcpServerPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDhcpServerPage : ContentPage
    {
        public IpDhcpServerPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDnsDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDnsDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Dns">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ip/dns"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <SwitchCell Text="Allow Remote Requests" On="{Binding Entity.AllowRemoteRequests}" />
        <EntryCell Label="Cache Max Ttl" Text="{Binding Entity.CacheMaxTtl}" />
        <EntryCell Label="Cache Size" Text="{Binding Entity.CacheSize}" />
        <EntryCell Label="Cache Used" IsEnabled="False" Text="{Binding Entity.CacheUsed}" />
        <EntryCell Label="Servers" Text="{Binding Entity.Servers}" />
<!--
        <EntryCell Label="Ip Dns" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Dns" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Dns"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpDnsDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDnsDetailPage : ContentPage
    {
        public IpDnsDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpDnsPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpDnsPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ip/dns"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="AllowRemoteRequests" FlexLayout.Basis="50%" />
            <Label Text="{Binding AllowRemoteRequests}" FlexLayout.Basis="50%" />
            <Label Text="CacheMaxTtl" FlexLayout.Basis="50%" />
            <Label Text="{Binding CacheMaxTtl}" FlexLayout.Basis="50%" />
            <Label Text="CacheSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding CacheSize}" FlexLayout.Basis="50%" />
            <Label Text="CacheUsed" FlexLayout.Basis="50%" />
            <Label Text="{Binding CacheUsed}" FlexLayout.Basis="50%" />
            <Label Text="Servers" FlexLayout.Basis="50%" />
            <Label Text="{Binding Servers}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpDnsPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpDnsPage : ContentPage
    {
        public IpDnsPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpPoolDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpPoolDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Pool">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/pool"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Ranges" Text="{Binding Entity.Ranges}" />
        <EntryCell Label="Next Pool" Text="{Binding Entity.NextPool}" />
<!--
        <EntryCell Label="Ip Pool" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Pool" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Pool"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpPoolDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpPoolDetailPage : ContentPage
    {
        public IpPoolDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpPoolPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpPoolPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/pool"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Ranges" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ranges}" FlexLayout.Basis="50%" />
            <Label Text="NextPool" FlexLayout.Basis="50%" />
            <Label Text="{Binding NextPool}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpPoolPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpPoolPage : ContentPage
    {
        public IpPoolPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpRouteDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpRouteDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ip Route">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ip/route"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Dst Address" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Gateway" Text="{Binding Entity.Gateway}" />
        <EntryCell Label="Gateway Status" IsEnabled="False" Text="{Binding Entity.GatewayStatus}" />
        <EntryCell Label="Distance" Keyboard="Numeric" Text="{Binding Entity.Distance}" />
        <EntryCell Label="Scope" Keyboard="Numeric" Text="{Binding Entity.Scope}" />
        <EntryCell Label="Target Scope" Keyboard="Numeric" Text="{Binding Entity.TargetScope}" />
        <SwitchCell Text="Active" On="{Binding Entity.Active}" />
        <SwitchCell Text="Static" On="{Binding Entity.Static}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Bgp As Path" IsEnabled="False" Text="{Binding Entity.BgpAsPath}" />
        <EntryCell Label="Bgp Origin" IsEnabled="False" Text="{Binding Entity.BgpOrigin}" />
        <EntryCell Label="Bgp Communities" IsEnabled="False" Text="{Binding Entity.BgpCommunities}" />
        <EntryCell Label="Received From" IsEnabled="False" Text="{Binding Entity.ReceivedFrom}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Bgp" On="{Binding Entity.Bgp}" />
        <EntryCell Label="Pref Src" IsEnabled="False" Text="{Binding Entity.PrefSrc}" />
        <SwitchCell Text="Connect" On="{Binding Entity.Connect}" />
<!--
        <EntryCell Label="Ip Route" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ip Route" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ip Route"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\IpRouteDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpRouteDetailPage : ContentPage
    {
        public IpRouteDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\IpRoutePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.IpRoutePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ip/route"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="Gateway" FlexLayout.Basis="50%" />
            <Label Text="{Binding Gateway}" FlexLayout.Basis="50%" />
            <Label Text="GatewayStatus" FlexLayout.Basis="50%" />
            <Label Text="{Binding GatewayStatus}" FlexLayout.Basis="50%" />
            <Label Text="Distance" FlexLayout.Basis="50%" />
            <Label Text="{Binding Distance}" FlexLayout.Basis="50%" />
            <Label Text="Scope" FlexLayout.Basis="50%" />
            <Label Text="{Binding Scope}" FlexLayout.Basis="50%" />
            <Label Text="TargetScope" FlexLayout.Basis="50%" />
            <Label Text="{Binding TargetScope}" FlexLayout.Basis="50%" />
            <Label Text="Active" FlexLayout.Basis="50%" />
            <Label Text="{Binding Active}" FlexLayout.Basis="50%" />
            <Label Text="Static" FlexLayout.Basis="50%" />
            <Label Text="{Binding Static}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="BgpAsPath" FlexLayout.Basis="50%" />
            <Label Text="{Binding BgpAsPath}" FlexLayout.Basis="50%" />
            <Label Text="BgpOrigin" FlexLayout.Basis="50%" />
            <Label Text="{Binding BgpOrigin}" FlexLayout.Basis="50%" />
            <Label Text="BgpCommunities" FlexLayout.Basis="50%" />
            <Label Text="{Binding BgpCommunities}" FlexLayout.Basis="50%" />
            <Label Text="ReceivedFrom" FlexLayout.Basis="50%" />
            <Label Text="{Binding ReceivedFrom}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Bgp" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bgp}" FlexLayout.Basis="50%" />
            <Label Text="PrefSrc" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrefSrc}" FlexLayout.Basis="50%" />
            <Label Text="Connect" FlexLayout.Basis="50%" />
            <Label Text="{Binding Connect}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\IpRoutePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class IpRoutePage : ContentPage
    {
        public IpRoutePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\LogDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.LogDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Log">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/log"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Message" IsEnabled="False" Text="{Binding Entity.Message}" />
        <EntryCell Label="Time" IsEnabled="False" Text="{Binding Entity.Time}" />
        <EntryCell Label="Topics" IsEnabled="False" Text="{Binding Entity.Topics}" />
<!--
        <EntryCell Label="Log" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Log" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Log"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\LogDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class LogDetailPage : ContentPage
    {
        public LogDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\LogPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.LogPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/log"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Message" FlexLayout.Basis="50%" />
            <Label Text="{Binding Message}" FlexLayout.Basis="50%" />
            <Label Text="Time" FlexLayout.Basis="50%" />
            <Label Text="{Binding Time}" FlexLayout.Basis="50%" />
            <Label Text="Topics" FlexLayout.Basis="50%" />
            <Label Text="{Binding Topics}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\LogPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class LogPage : ContentPage
    {
        public LogPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppAaaDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppAaaDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ppp Aaa">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ppp/aaa"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <SwitchCell Text="Accounting" On="{Binding Entity.Accounting}" />
        <EntryCell Label="Interim Update" Text="{Binding Entity.InterimUpdate}" />
        <SwitchCell Text="Use Radius" On="{Binding Entity.UseRadius}" />
<!--
        <EntryCell Label="Ppp Aaa" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ppp Aaa" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ppp Aaa"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\PppAaaDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppAaaDetailPage : ContentPage
    {
        public PppAaaDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppAaaPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppAaaPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ppp/aaa"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Accounting" FlexLayout.Basis="50%" />
            <Label Text="{Binding Accounting}" FlexLayout.Basis="50%" />
            <Label Text="InterimUpdate" FlexLayout.Basis="50%" />
            <Label Text="{Binding InterimUpdate}" FlexLayout.Basis="50%" />
            <Label Text="UseRadius" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseRadius}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\PppAaaPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppAaaPage : ContentPage
    {
        public PppAaaPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppActiveDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppActiveDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ppp Active">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ppp/active"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address" IsEnabled="False" Text="{Binding Entity.Address}" />
        <EntryCell Label="Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Caller Id" IsEnabled="False" Text="{Binding Entity.CallerId}" />
        <EntryCell Label="Encoding" IsEnabled="False" Text="{Binding Entity.Encoding}" />
        <EntryCell Label="Limit Bytes In" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.LimitBytesIn}" />
        <EntryCell Label="Limit Bytes Out" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.LimitBytesOut}" />
        <EntryCell Label="Name" IsEnabled="False" Text="{Binding Entity.Name}" />
        <EntryCell Label="Packets" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Service" IsEnabled="False" Text="{Binding Entity.Service}" />
        <EntryCell Label="Session Id" IsEnabled="False" Text="{Binding Entity.SessionId}" />
        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
<!--
        <EntryCell Label="Ppp Active" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ppp Active" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ppp Active"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\PppActiveDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppActiveDetailPage : ContentPage
    {
        public PppActiveDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppActivePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppActivePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ppp/active"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="CallerId" FlexLayout.Basis="50%" />
            <Label Text="{Binding CallerId}" FlexLayout.Basis="50%" />
            <Label Text="Encoding" FlexLayout.Basis="50%" />
            <Label Text="{Binding Encoding}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesIn}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesOut}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="Service" FlexLayout.Basis="50%" />
            <Label Text="{Binding Service}" FlexLayout.Basis="50%" />
            <Label Text="SessionId" FlexLayout.Basis="50%" />
            <Label Text="{Binding SessionId}" FlexLayout.Basis="50%" />
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\PppActivePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppActivePage : ContentPage
    {
        public PppActivePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppProfileDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppProfileDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ppp Profile">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ppp/profile"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Address List" Text="{Binding Entity.AddressList}" />
        <EntryCell Label="Bridge" Text="{Binding Entity.Bridge}" />
        <EntryCell Label="Change Tcp Mss" Text="{Binding Entity.ChangeTcpMss}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Dhcpv 6 Pd Pool" Text="{Binding Entity.Dhcpv6PdPool}" />
        <EntryCell Label="Dns Server" Text="{Binding Entity.DnsServer}" />
        <EntryCell Label="Idle Timeout" Text="{Binding Entity.IdleTimeout}" />
        <EntryCell Label="Incoming Filter" Text="{Binding Entity.IncomingFilter}" />
        <EntryCell Label="Local Address" Text="{Binding Entity.LocalAddress}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Only One" Text="{Binding Entity.OnlyOne}" />
        <EntryCell Label="Outgoing Filter" Text="{Binding Entity.OutgoingFilter}" />
        <EntryCell Label="Rate Limit" Text="{Binding Entity.RateLimit}" />
        <EntryCell Label="Remote Address" Text="{Binding Entity.RemoteAddress}" />
        <EntryCell Label="Remote Ipv 6 Prefix Pool" Text="{Binding Entity.RemoteIpv6PrefixPool}" />
        <EntryCell Label="Session Timeout" Text="{Binding Entity.SessionTimeout}" />
        <EntryCell Label="Use Compression" Text="{Binding Entity.UseCompression}" />
        <EntryCell Label="Use Encryption" Text="{Binding Entity.UseEncryption}" />
        <EntryCell Label="Use Ipv 6" Text="{Binding Entity.UseIpv6}" />
        <EntryCell Label="Use Mpls" Text="{Binding Entity.UseMpls}" />
        <EntryCell Label="Use Vj Compression" Text="{Binding Entity.UseVjCompression}" />
        <EntryCell Label="On Up" Text="{Binding Entity.OnUp}" />
        <EntryCell Label="On Down" Text="{Binding Entity.OnDown}" />
        <EntryCell Label="Wins Server" Text="{Binding Entity.WinsServer}" />
<!--
        <EntryCell Label="Ppp Profile" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ppp Profile" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ppp Profile"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\PppProfileDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppProfileDetailPage : ContentPage
    {
        public PppProfileDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppProfilePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppProfilePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ppp/profile"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="AddressList" FlexLayout.Basis="50%" />
            <Label Text="{Binding AddressList}" FlexLayout.Basis="50%" />
            <Label Text="Bridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bridge}" FlexLayout.Basis="50%" />
            <Label Text="ChangeTcpMss" FlexLayout.Basis="50%" />
            <Label Text="{Binding ChangeTcpMss}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Dhcpv6PdPool" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dhcpv6PdPool}" FlexLayout.Basis="50%" />
            <Label Text="DnsServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding DnsServer}" FlexLayout.Basis="50%" />
            <Label Text="IdleTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding IdleTimeout}" FlexLayout.Basis="50%" />
            <Label Text="IncomingFilter" FlexLayout.Basis="50%" />
            <Label Text="{Binding IncomingFilter}" FlexLayout.Basis="50%" />
            <Label Text="LocalAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding LocalAddress}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="OnlyOne" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnlyOne}" FlexLayout.Basis="50%" />
            <Label Text="OutgoingFilter" FlexLayout.Basis="50%" />
            <Label Text="{Binding OutgoingFilter}" FlexLayout.Basis="50%" />
            <Label Text="RateLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding RateLimit}" FlexLayout.Basis="50%" />
            <Label Text="RemoteAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteAddress}" FlexLayout.Basis="50%" />
            <Label Text="RemoteIpv6PrefixPool" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteIpv6PrefixPool}" FlexLayout.Basis="50%" />
            <Label Text="SessionTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding SessionTimeout}" FlexLayout.Basis="50%" />
            <Label Text="UseCompression" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseCompression}" FlexLayout.Basis="50%" />
            <Label Text="UseEncryption" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseEncryption}" FlexLayout.Basis="50%" />
            <Label Text="UseIpv6" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseIpv6}" FlexLayout.Basis="50%" />
            <Label Text="UseMpls" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseMpls}" FlexLayout.Basis="50%" />
            <Label Text="UseVjCompression" FlexLayout.Basis="50%" />
            <Label Text="{Binding UseVjCompression}" FlexLayout.Basis="50%" />
            <Label Text="OnUp" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnUp}" FlexLayout.Basis="50%" />
            <Label Text="OnDown" FlexLayout.Basis="50%" />
            <Label Text="{Binding OnDown}" FlexLayout.Basis="50%" />
            <Label Text="WinsServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding WinsServer}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\PppProfilePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppProfilePage : ContentPage
    {
        public PppProfilePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppSecretDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppSecretDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Ppp Secret">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="ppp/secret"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Caller Id" Text="{Binding Entity.CallerId}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Limit Bytes In" Keyboard="Numeric" Text="{Binding Entity.LimitBytesIn}" />
        <EntryCell Label="Limit Bytes Out" Keyboard="Numeric" Text="{Binding Entity.LimitBytesOut}" />
        <EntryCell Label="Local Address" Text="{Binding Entity.LocalAddress}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Password" Text="{Binding Entity.Password}" />
        <EntryCell Label="Profile" Text="{Binding Entity.Profile}" />
        <EntryCell Label="Remote Address" Text="{Binding Entity.RemoteAddress}" />
        <EntryCell Label="Remote Ipv 6 Prefix" Text="{Binding Entity.RemoteIpv6Prefix}" />
        <EntryCell Label="Routes" Text="{Binding Entity.Routes}" />
        <EntryCell Label="Service" Text="{Binding Entity.Service}" />
<!--
        <EntryCell Label="Ppp Secret" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Ppp Secret" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Ppp Secret"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\PppSecretDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppSecretDetailPage : ContentPage
    {
        public PppSecretDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\PppSecretPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.PppSecretPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="ppp/secret"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="CallerId" FlexLayout.Basis="50%" />
            <Label Text="{Binding CallerId}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesIn}" FlexLayout.Basis="50%" />
            <Label Text="LimitBytesOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitBytesOut}" FlexLayout.Basis="50%" />
            <Label Text="LocalAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding LocalAddress}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Password" FlexLayout.Basis="50%" />
            <Label Text="{Binding Password}" FlexLayout.Basis="50%" />
            <Label Text="Profile" FlexLayout.Basis="50%" />
            <Label Text="{Binding Profile}" FlexLayout.Basis="50%" />
            <Label Text="RemoteAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteAddress}" FlexLayout.Basis="50%" />
            <Label Text="RemoteIpv6Prefix" FlexLayout.Basis="50%" />
            <Label Text="{Binding RemoteIpv6Prefix}" FlexLayout.Basis="50%" />
            <Label Text="Routes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Routes}" FlexLayout.Basis="50%" />
            <Label Text="Service" FlexLayout.Basis="50%" />
            <Label Text="{Binding Service}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\PppSecretPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class PppSecretPage : ContentPage
    {
        public PppSecretPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueSimpleDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueSimpleDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Queue Simple">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/queue/simple"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Target" Text="{Binding Entity.Target}" />
        <EntryCell Label="Parent" Text="{Binding Entity.Parent}" />
        <EntryCell Label="Priority" Text="{Binding Entity.Priority}" />
        <EntryCell Label="Queue" Text="{Binding Entity.Queue}" />
        <EntryCell Label="Limit At" Text="{Binding Entity.LimitAt}" />
        <EntryCell Label="Max Limit" Text="{Binding Entity.MaxLimit}" />
        <EntryCell Label="Burst Limit" Text="{Binding Entity.BurstLimit}" />
        <EntryCell Label="Burst Threshold" Text="{Binding Entity.BurstThreshold}" />
        <EntryCell Label="Burst Time" Text="{Binding Entity.BurstTime}" />
        <EntryCell Label="Bytes" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Total Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalBytes}" />
        <EntryCell Label="Packets" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Total Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalPackets}" />
        <EntryCell Label="Dropped" IsEnabled="False" Text="{Binding Entity.Dropped}" />
        <EntryCell Label="Total Dropped" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalDropped}" />
        <EntryCell Label="Rate" IsEnabled="False" Text="{Binding Entity.Rate}" />
        <EntryCell Label="Total Rate" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalRate}" />
        <EntryCell Label="Packet Rate" IsEnabled="False" Text="{Binding Entity.PacketRate}" />
        <EntryCell Label="Total Packet Rate" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalPacketRate}" />
        <EntryCell Label="Queued Packets" IsEnabled="False" Text="{Binding Entity.QueuedPackets}" />
        <EntryCell Label="Total Queued Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalQueuedPackets}" />
        <EntryCell Label="Queued Bytes" IsEnabled="False" Text="{Binding Entity.QueuedBytes}" />
        <EntryCell Label="Total Queued Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalQueuedBytes}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <SwitchCell Text="Dynamic" On="{Binding Entity.Dynamic}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Dst" Text="{Binding Entity.Dst}" />
        <EntryCell Label="Total Max Limit" Keyboard="Numeric" Text="{Binding Entity.TotalMaxLimit}" />
        <EntryCell Label="Total Queue" Text="{Binding Entity.TotalQueue}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Queue Simple" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Queue Simple" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Queue Simple"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\QueueSimpleDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueSimpleDetailPage : ContentPage
    {
        public QueueSimpleDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueSimplePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueSimplePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/queue/simple"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Target" FlexLayout.Basis="50%" />
            <Label Text="{Binding Target}" FlexLayout.Basis="50%" />
            <Label Text="Parent" FlexLayout.Basis="50%" />
            <Label Text="{Binding Parent}" FlexLayout.Basis="50%" />
            <Label Text="Priority" FlexLayout.Basis="50%" />
            <Label Text="{Binding Priority}" FlexLayout.Basis="50%" />
            <Label Text="Queue" FlexLayout.Basis="50%" />
            <Label Text="{Binding Queue}" FlexLayout.Basis="50%" />
            <Label Text="LimitAt" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitAt}" FlexLayout.Basis="50%" />
            <Label Text="MaxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxLimit}" FlexLayout.Basis="50%" />
            <Label Text="BurstLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstLimit}" FlexLayout.Basis="50%" />
            <Label Text="BurstThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstThreshold}" FlexLayout.Basis="50%" />
            <Label Text="BurstTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstTime}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="TotalBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalBytes}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="TotalPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalPackets}" FlexLayout.Basis="50%" />
            <Label Text="Dropped" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dropped}" FlexLayout.Basis="50%" />
            <Label Text="TotalDropped" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalDropped}" FlexLayout.Basis="50%" />
            <Label Text="Rate" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rate}" FlexLayout.Basis="50%" />
            <Label Text="TotalRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalRate}" FlexLayout.Basis="50%" />
            <Label Text="PacketRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketRate}" FlexLayout.Basis="50%" />
            <Label Text="TotalPacketRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalPacketRate}" FlexLayout.Basis="50%" />
            <Label Text="QueuedPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding QueuedPackets}" FlexLayout.Basis="50%" />
            <Label Text="TotalQueuedPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalQueuedPackets}" FlexLayout.Basis="50%" />
            <Label Text="QueuedBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding QueuedBytes}" FlexLayout.Basis="50%" />
            <Label Text="TotalQueuedBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalQueuedBytes}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Dynamic" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dynamic}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Dst" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dst}" FlexLayout.Basis="50%" />
            <Label Text="TotalMaxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalMaxLimit}" FlexLayout.Basis="50%" />
            <Label Text="TotalQueue" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalQueue}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\QueueSimplePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueSimplePage : ContentPage
    {
        public QueueSimplePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueTreeDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueTreeDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Queue Tree">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/queue/tree"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Parent" Text="{Binding Entity.Parent}" />
        <EntryCell Label="Packet Mark" Text="{Binding Entity.PacketMark}" />
        <EntryCell Label="Limit At" Keyboard="Numeric" Text="{Binding Entity.LimitAt}" />
        <EntryCell Label="Queue" Text="{Binding Entity.Queue}" />
        <EntryCell Label="Priority" Keyboard="Numeric" Text="{Binding Entity.Priority}" />
        <EntryCell Label="Max Limit" Keyboard="Numeric" Text="{Binding Entity.MaxLimit}" />
        <EntryCell Label="Burst Limit" Keyboard="Numeric" Text="{Binding Entity.BurstLimit}" />
        <EntryCell Label="Burst Threshold" Keyboard="Numeric" Text="{Binding Entity.BurstThreshold}" />
        <EntryCell Label="Burst Time" Text="{Binding Entity.BurstTime}" />
        <EntryCell Label="Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Dropped" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Dropped}" />
        <EntryCell Label="Rate" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rate}" />
        <EntryCell Label="Packet Rate" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.PacketRate}" />
        <EntryCell Label="Queued Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.QueuedPackets}" />
        <EntryCell Label="Queued Bytes" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.QueuedBytes}" />
        <SwitchCell Text="Invalid" On="{Binding Entity.Invalid}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="Queue Tree" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Queue Tree" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Queue Tree"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\QueueTreeDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueTreeDetailPage : ContentPage
    {
        public QueueTreeDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueTreePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueTreePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/queue/tree"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Parent" FlexLayout.Basis="50%" />
            <Label Text="{Binding Parent}" FlexLayout.Basis="50%" />
            <Label Text="PacketMark" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketMark}" FlexLayout.Basis="50%" />
            <Label Text="LimitAt" FlexLayout.Basis="50%" />
            <Label Text="{Binding LimitAt}" FlexLayout.Basis="50%" />
            <Label Text="Queue" FlexLayout.Basis="50%" />
            <Label Text="{Binding Queue}" FlexLayout.Basis="50%" />
            <Label Text="Priority" FlexLayout.Basis="50%" />
            <Label Text="{Binding Priority}" FlexLayout.Basis="50%" />
            <Label Text="MaxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxLimit}" FlexLayout.Basis="50%" />
            <Label Text="BurstLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstLimit}" FlexLayout.Basis="50%" />
            <Label Text="BurstThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstThreshold}" FlexLayout.Basis="50%" />
            <Label Text="BurstTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding BurstTime}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="Dropped" FlexLayout.Basis="50%" />
            <Label Text="{Binding Dropped}" FlexLayout.Basis="50%" />
            <Label Text="Rate" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rate}" FlexLayout.Basis="50%" />
            <Label Text="PacketRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketRate}" FlexLayout.Basis="50%" />
            <Label Text="QueuedPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding QueuedPackets}" FlexLayout.Basis="50%" />
            <Label Text="QueuedBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding QueuedBytes}" FlexLayout.Basis="50%" />
            <Label Text="Invalid" FlexLayout.Basis="50%" />
            <Label Text="{Binding Invalid}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\QueueTreePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueTreePage : ContentPage
    {
        public QueueTreePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueTypeDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueTypeDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Queue Type">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/queue/type"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Kind" Text="{Binding Entity.Kind}" />
        <EntryCell Label="Pfifo Limit" Keyboard="Numeric" Text="{Binding Entity.PfifoLimit}" />
        <SwitchCell Text="Default" On="{Binding Entity.Default}" />
        <EntryCell Label="Sfq Perturb" Keyboard="Numeric" Text="{Binding Entity.SfqPerturb}" />
        <EntryCell Label="Sfq Allot" Keyboard="Numeric" Text="{Binding Entity.SfqAllot}" />
        <EntryCell Label="Red Limit" Keyboard="Numeric" Text="{Binding Entity.RedLimit}" />
        <EntryCell Label="Red Min Threshold" Keyboard="Numeric" Text="{Binding Entity.RedMinThreshold}" />
        <EntryCell Label="Red Max Threshold" Keyboard="Numeric" Text="{Binding Entity.RedMaxThreshold}" />
        <EntryCell Label="Red Burst" Keyboard="Numeric" Text="{Binding Entity.RedBurst}" />
        <EntryCell Label="Red Avg Packet" Keyboard="Numeric" Text="{Binding Entity.RedAvgPacket}" />
        <EntryCell Label="Pcq Rate" Keyboard="Numeric" Text="{Binding Entity.PcqRate}" />
        <EntryCell Label="Pcq Limit" Keyboard="Numeric" Text="{Binding Entity.PcqLimit}" />
        <EntryCell Label="Pcq Classifier" Text="{Binding Entity.PcqClassifier}" />
        <EntryCell Label="Pcq Total Limit" Keyboard="Numeric" Text="{Binding Entity.PcqTotalLimit}" />
        <EntryCell Label="Pcq Burst Rate" Keyboard="Numeric" Text="{Binding Entity.PcqBurstRate}" />
        <EntryCell Label="Pcq Burst Threshold" Keyboard="Numeric" Text="{Binding Entity.PcqBurstThreshold}" />
        <EntryCell Label="Pcq Burst Time" Text="{Binding Entity.PcqBurstTime}" />
        <EntryCell Label="Pcq Src Address Mask" Keyboard="Numeric" Text="{Binding Entity.PcqSrcAddressMask}" />
        <EntryCell Label="Pcq Dst Address Mask" Keyboard="Numeric" Text="{Binding Entity.PcqDstAddressMask}" />
        <EntryCell Label="Pcq Src Address 6 Mask" Keyboard="Numeric" Text="{Binding Entity.PcqSrcAddress6Mask}" />
        <EntryCell Label="Pcq Dst Address 6 Mask" Keyboard="Numeric" Text="{Binding Entity.PcqDstAddress6Mask}" />
        <EntryCell Label="Mq Pfifo Limit" Keyboard="Numeric" Text="{Binding Entity.MqPfifoLimit}" />
<!--
        <EntryCell Label="Queue Type" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Queue Type" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Queue Type"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\QueueTypeDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueTypeDetailPage : ContentPage
    {
        public QueueTypeDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\QueueTypePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.QueueTypePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/queue/type"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Kind" FlexLayout.Basis="50%" />
            <Label Text="{Binding Kind}" FlexLayout.Basis="50%" />
            <Label Text="PfifoLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding PfifoLimit}" FlexLayout.Basis="50%" />
            <Label Text="Default" FlexLayout.Basis="50%" />
            <Label Text="{Binding Default}" FlexLayout.Basis="50%" />
            <Label Text="SfqPerturb" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfqPerturb}" FlexLayout.Basis="50%" />
            <Label Text="SfqAllot" FlexLayout.Basis="50%" />
            <Label Text="{Binding SfqAllot}" FlexLayout.Basis="50%" />
            <Label Text="RedLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedLimit}" FlexLayout.Basis="50%" />
            <Label Text="RedMinThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedMinThreshold}" FlexLayout.Basis="50%" />
            <Label Text="RedMaxThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedMaxThreshold}" FlexLayout.Basis="50%" />
            <Label Text="RedBurst" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedBurst}" FlexLayout.Basis="50%" />
            <Label Text="RedAvgPacket" FlexLayout.Basis="50%" />
            <Label Text="{Binding RedAvgPacket}" FlexLayout.Basis="50%" />
            <Label Text="PcqRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqRate}" FlexLayout.Basis="50%" />
            <Label Text="PcqLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqLimit}" FlexLayout.Basis="50%" />
            <Label Text="PcqClassifier" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqClassifier}" FlexLayout.Basis="50%" />
            <Label Text="PcqTotalLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqTotalLimit}" FlexLayout.Basis="50%" />
            <Label Text="PcqBurstRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqBurstRate}" FlexLayout.Basis="50%" />
            <Label Text="PcqBurstThreshold" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqBurstThreshold}" FlexLayout.Basis="50%" />
            <Label Text="PcqBurstTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqBurstTime}" FlexLayout.Basis="50%" />
            <Label Text="PcqSrcAddressMask" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqSrcAddressMask}" FlexLayout.Basis="50%" />
            <Label Text="PcqDstAddressMask" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqDstAddressMask}" FlexLayout.Basis="50%" />
            <Label Text="PcqSrcAddress6Mask" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqSrcAddress6Mask}" FlexLayout.Basis="50%" />
            <Label Text="PcqDstAddress6Mask" FlexLayout.Basis="50%" />
            <Label Text="{Binding PcqDstAddress6Mask}" FlexLayout.Basis="50%" />
            <Label Text="MqPfifoLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding MqPfifoLimit}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\QueueTypePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class QueueTypePage : ContentPage
    {
        public QueueTypePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemIdentityDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemIdentityDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="System Identity">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/system/identity"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
<!--
        <EntryCell Label="System Identity" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="System Identity" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="System Identity"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\SystemIdentityDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemIdentityDetailPage : ContentPage
    {
        public SystemIdentityDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemIdentityPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemIdentityPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/system/identity"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\SystemIdentityPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemIdentityPage : ContentPage
    {
        public SystemIdentityPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemResourceDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemResourceDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="System Resource">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/system/resource"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
        <EntryCell Label="Version" IsEnabled="False" Text="{Binding Entity.Version}" />
        <EntryCell Label="Build Time" IsEnabled="False" Text="{Binding Entity.BuildTime}" />
        <EntryCell Label="Free Memory" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.FreeMemory}" />
        <EntryCell Label="Total Memory" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalMemory}" />
        <EntryCell Label="Cpu" IsEnabled="False" Text="{Binding Entity.Cpu}" />
        <EntryCell Label="Cpu Count" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.CpuCount}" />
        <EntryCell Label="Cpu Frequency" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.CpuFrequency}" />
        <EntryCell Label="Cpu Load" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.CpuLoad}" />
        <EntryCell Label="Free Hdd Space" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.FreeHddSpace}" />
        <EntryCell Label="Total Hdd Space" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TotalHddSpace}" />
        <EntryCell Label="Write Sect Since Reboot" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.WriteSectSinceReboot}" />
        <EntryCell Label="Write Sect Total" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.WriteSectTotal}" />
        <EntryCell Label="Architecture Name" IsEnabled="False" Text="{Binding Entity.ArchitectureName}" />
        <EntryCell Label="Board Name" IsEnabled="False" Text="{Binding Entity.BoardName}" />
        <EntryCell Label="Platform" IsEnabled="False" Text="{Binding Entity.Platform}" />
<!--
        <EntryCell Label="System Resource" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="System Resource" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="System Resource"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\SystemResourceDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemResourceDetailPage : ContentPage
    {
        public SystemResourceDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemResourcePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemResourcePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/system/resource"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />
            <Label Text="Version" FlexLayout.Basis="50%" />
            <Label Text="{Binding Version}" FlexLayout.Basis="50%" />
            <Label Text="BuildTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding BuildTime}" FlexLayout.Basis="50%" />
            <Label Text="FreeMemory" FlexLayout.Basis="50%" />
            <Label Text="{Binding FreeMemory}" FlexLayout.Basis="50%" />
            <Label Text="TotalMemory" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalMemory}" FlexLayout.Basis="50%" />
            <Label Text="Cpu" FlexLayout.Basis="50%" />
            <Label Text="{Binding Cpu}" FlexLayout.Basis="50%" />
            <Label Text="CpuCount" FlexLayout.Basis="50%" />
            <Label Text="{Binding CpuCount}" FlexLayout.Basis="50%" />
            <Label Text="CpuFrequency" FlexLayout.Basis="50%" />
            <Label Text="{Binding CpuFrequency}" FlexLayout.Basis="50%" />
            <Label Text="CpuLoad" FlexLayout.Basis="50%" />
            <Label Text="{Binding CpuLoad}" FlexLayout.Basis="50%" />
            <Label Text="FreeHddSpace" FlexLayout.Basis="50%" />
            <Label Text="{Binding FreeHddSpace}" FlexLayout.Basis="50%" />
            <Label Text="TotalHddSpace" FlexLayout.Basis="50%" />
            <Label Text="{Binding TotalHddSpace}" FlexLayout.Basis="50%" />
            <Label Text="WriteSectSinceReboot" FlexLayout.Basis="50%" />
            <Label Text="{Binding WriteSectSinceReboot}" FlexLayout.Basis="50%" />
            <Label Text="WriteSectTotal" FlexLayout.Basis="50%" />
            <Label Text="{Binding WriteSectTotal}" FlexLayout.Basis="50%" />
            <Label Text="ArchitectureName" FlexLayout.Basis="50%" />
            <Label Text="{Binding ArchitectureName}" FlexLayout.Basis="50%" />
            <Label Text="BoardName" FlexLayout.Basis="50%" />
            <Label Text="{Binding BoardName}" FlexLayout.Basis="50%" />
            <Label Text="Platform" FlexLayout.Basis="50%" />
            <Label Text="{Binding Platform}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\SystemResourcePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemResourcePage : ContentPage
    {
        public SystemResourcePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemRouterboardDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemRouterboardDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="System Routerboard">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/system/routerboard"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <SwitchCell Text="Routerboard" On="{Binding Entity.Routerboard}" />
        <EntryCell Label="Board Name" Text="{Binding Entity.BoardName}" />
        <EntryCell Label="Model" Text="{Binding Entity.Model}" />
        <EntryCell Label="Serial Number" Text="{Binding Entity.SerialNumber}" />
        <EntryCell Label="Firmware Type" Text="{Binding Entity.FirmwareType}" />
        <EntryCell Label="Factory Firmware" Text="{Binding Entity.FactoryFirmware}" />
        <EntryCell Label="Current Firmware" Text="{Binding Entity.CurrentFirmware}" />
        <EntryCell Label="Upgrade Firmware" Text="{Binding Entity.UpgradeFirmware}" />
<!--
        <EntryCell Label="System Routerboard" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="System Routerboard" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="System Routerboard"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\SystemRouterboardDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemRouterboardDetailPage : ContentPage
    {
        public SystemRouterboardDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\SystemRouterboardPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.SystemRouterboardPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/system/routerboard"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Routerboard" FlexLayout.Basis="50%" />
            <Label Text="{Binding Routerboard}" FlexLayout.Basis="50%" />
            <Label Text="BoardName" FlexLayout.Basis="50%" />
            <Label Text="{Binding BoardName}" FlexLayout.Basis="50%" />
            <Label Text="Model" FlexLayout.Basis="50%" />
            <Label Text="{Binding Model}" FlexLayout.Basis="50%" />
            <Label Text="SerialNumber" FlexLayout.Basis="50%" />
            <Label Text="{Binding SerialNumber}" FlexLayout.Basis="50%" />
            <Label Text="FirmwareType" FlexLayout.Basis="50%" />
            <Label Text="{Binding FirmwareType}" FlexLayout.Basis="50%" />
            <Label Text="FactoryFirmware" FlexLayout.Basis="50%" />
            <Label Text="{Binding FactoryFirmware}" FlexLayout.Basis="50%" />
            <Label Text="CurrentFirmware" FlexLayout.Basis="50%" />
            <Label Text="{Binding CurrentFirmware}" FlexLayout.Basis="50%" />
            <Label Text="UpgradeFirmware" FlexLayout.Basis="50%" />
            <Label Text="{Binding UpgradeFirmware}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\SystemRouterboardPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class SystemRouterboardPage : ContentPage
    {
        public SystemRouterboardPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolPingDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolPingDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Tool Ping">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/ping"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Sequence No" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.SequenceNo}" />
        <EntryCell Label="Host" IsEnabled="False" Text="{Binding Entity.Host}" />
        <EntryCell Label="Time To Life" IsEnabled="False" Text="{Binding Entity.TimeToLife}" />
        <EntryCell Label="Time" IsEnabled="False" Text="{Binding Entity.Time}" />
        <EntryCell Label="Sent" IsEnabled="False" Text="{Binding Entity.Sent}" />
        <EntryCell Label="Received" IsEnabled="False" Text="{Binding Entity.Received}" />
        <EntryCell Label="Packet Loss" IsEnabled="False" Text="{Binding Entity.PacketLoss}" />
        <EntryCell Label="Min Rtt" IsEnabled="False" Text="{Binding Entity.MinRtt}" />
        <EntryCell Label="Avg Rtt" IsEnabled="False" Text="{Binding Entity.AvgRtt}" />
        <EntryCell Label="Max Rtt" IsEnabled="False" Text="{Binding Entity.MaxRtt}" />
<!--
        <EntryCell Label="Tool Ping" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Tool Ping" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Tool Ping"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\ToolPingDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolPingDetailPage : ContentPage
    {
        public ToolPingDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolPingPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolPingPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/ping"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="SequenceNo" FlexLayout.Basis="50%" />
            <Label Text="{Binding SequenceNo}" FlexLayout.Basis="50%" />
            <Label Text="Host" FlexLayout.Basis="50%" />
            <Label Text="{Binding Host}" FlexLayout.Basis="50%" />
            <Label Text="TimeToLife" FlexLayout.Basis="50%" />
            <Label Text="{Binding TimeToLife}" FlexLayout.Basis="50%" />
            <Label Text="Time" FlexLayout.Basis="50%" />
            <Label Text="{Binding Time}" FlexLayout.Basis="50%" />
            <Label Text="Sent" FlexLayout.Basis="50%" />
            <Label Text="{Binding Sent}" FlexLayout.Basis="50%" />
            <Label Text="Received" FlexLayout.Basis="50%" />
            <Label Text="{Binding Received}" FlexLayout.Basis="50%" />
            <Label Text="PacketLoss" FlexLayout.Basis="50%" />
            <Label Text="{Binding PacketLoss}" FlexLayout.Basis="50%" />
            <Label Text="MinRtt" FlexLayout.Basis="50%" />
            <Label Text="{Binding MinRtt}" FlexLayout.Basis="50%" />
            <Label Text="AvgRtt" FlexLayout.Basis="50%" />
            <Label Text="{Binding AvgRtt}" FlexLayout.Basis="50%" />
            <Label Text="MaxRtt" FlexLayout.Basis="50%" />
            <Label Text="{Binding MaxRtt}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\ToolPingPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolPingPage : ContentPage
    {
        public ToolPingPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolTorchDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolTorchDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Tool Torch">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/tool/torch"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Src Address" IsEnabled="False" Text="{Binding Entity.SrcAddress}" />
        <EntryCell Label="Dst Address" IsEnabled="False" Text="{Binding Entity.DstAddress}" />
        <EntryCell Label="Ip Protocol" IsEnabled="False" Text="{Binding Entity.IpProtocol}" />
        <EntryCell Label="Src Port" IsEnabled="False" Text="{Binding Entity.SrcPort}" />
        <EntryCell Label="Dst Port" IsEnabled="False" Text="{Binding Entity.DstPort}" />
        <EntryCell Label="Tx" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Tx}" />
        <EntryCell Label="Rx" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Rx}" />
        <EntryCell Label="Tx Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TxPackets}" />
        <EntryCell Label="Rx Packets" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.RxPackets}" />
<!--
        <EntryCell Label="Tool Torch" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Tool Torch" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Tool Torch"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\ToolTorchDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolTorchDetailPage : ContentPage
    {
        public ToolTorchDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolTorchPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolTorchPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/tool/torch"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="SrcAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcAddress}" FlexLayout.Basis="50%" />
            <Label Text="DstAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstAddress}" FlexLayout.Basis="50%" />
            <Label Text="IpProtocol" FlexLayout.Basis="50%" />
            <Label Text="{Binding IpProtocol}" FlexLayout.Basis="50%" />
            <Label Text="SrcPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding SrcPort}" FlexLayout.Basis="50%" />
            <Label Text="DstPort" FlexLayout.Basis="50%" />
            <Label Text="{Binding DstPort}" FlexLayout.Basis="50%" />
            <Label Text="Tx" FlexLayout.Basis="50%" />
            <Label Text="{Binding Tx}" FlexLayout.Basis="50%" />
            <Label Text="Rx" FlexLayout.Basis="50%" />
            <Label Text="{Binding Rx}" FlexLayout.Basis="50%" />
            <Label Text="TxPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxPackets}" FlexLayout.Basis="50%" />
            <Label Text="RxPackets" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxPackets}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\ToolTorchPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolTorchPage : ContentPage
    {
        public ToolTorchPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolTracerouteDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolTracerouteDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Tool Traceroute">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/tool/traceroute"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Address" IsEnabled="False" Text="{Binding Entity.Address}" />
        <EntryCell Label="Loss" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Loss}" />
        <EntryCell Label="Sent" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Sent}" />
        <EntryCell Label="Last" IsEnabled="False" Text="{Binding Entity.Last}" />
        <EntryCell Label="Status" IsEnabled="False" Text="{Binding Entity.Status}" />
        <EntryCell Label="Avg" IsEnabled="False" Text="{Binding Entity.Avg}" />
        <EntryCell Label="Best" IsEnabled="False" Text="{Binding Entity.Best}" />
        <EntryCell Label="Worst" IsEnabled="False" Text="{Binding Entity.Worst}" />
<!--
        <EntryCell Label="Tool Traceroute" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Tool Traceroute" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Tool Traceroute"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\ToolTracerouteDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolTracerouteDetailPage : ContentPage
    {
        public ToolTracerouteDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\ToolTraceroutePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ToolTraceroutePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/tool/traceroute"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Address" FlexLayout.Basis="50%" />
            <Label Text="{Binding Address}" FlexLayout.Basis="50%" />
            <Label Text="Loss" FlexLayout.Basis="50%" />
            <Label Text="{Binding Loss}" FlexLayout.Basis="50%" />
            <Label Text="Sent" FlexLayout.Basis="50%" />
            <Label Text="{Binding Sent}" FlexLayout.Basis="50%" />
            <Label Text="Last" FlexLayout.Basis="50%" />
            <Label Text="{Binding Last}" FlexLayout.Basis="50%" />
            <Label Text="Status" FlexLayout.Basis="50%" />
            <Label Text="{Binding Status}" FlexLayout.Basis="50%" />
            <Label Text="Avg" FlexLayout.Basis="50%" />
            <Label Text="{Binding Avg}" FlexLayout.Basis="50%" />
            <Label Text="Best" FlexLayout.Basis="50%" />
            <Label Text="{Binding Best}" FlexLayout.Basis="50%" />
            <Label Text="Worst" FlexLayout.Basis="50%" />
            <Label Text="{Binding Worst}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\ToolTraceroutePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ToolTraceroutePage : ContentPage
    {
        public ToolTraceroutePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\UserDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.UserDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="User">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/user"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Group" Text="{Binding Entity.Group}" />
        <EntryCell Label="Last Logged In" IsEnabled="False" Text="{Binding Entity.LastLoggedIn}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="User" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="User" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="User"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\UserDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class UserDetailPage : ContentPage
    {
        public UserDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\UserGroupDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.UserGroupDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="User Group">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="/user/group"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Policy" Text="{Binding Entity.Policy}" />
        <EntryCell Label="Skin" Text="{Binding Entity.Skin}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
<!--
        <EntryCell Label="User Group" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="User Group" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="User Group"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\UserGroupDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class UserGroupDetailPage : ContentPage
    {
        public UserGroupDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\UserGroupPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.UserGroupPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/user/group"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Policy" FlexLayout.Basis="50%" />
            <Label Text="{Binding Policy}" FlexLayout.Basis="50%" />
            <Label Text="Skin" FlexLayout.Basis="50%" />
            <Label Text="{Binding Skin}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\UserGroupPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class UserGroupPage : ContentPage
    {
        public UserGroupPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\UserPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.UserPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="/user"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Group" FlexLayout.Basis="50%" />
            <Label Text="{Binding Group}" FlexLayout.Basis="50%" />
            <Label Text="LastLoggedIn" FlexLayout.Basis="50%" />
            <Label Text="{Binding LastLoggedIn}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\UserPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class UserPage : ContentPage
    {
        public UserPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessAccessListDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessAccessListDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Wireless Access List">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless/access-list"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Ap Tx Limit" Keyboard="Numeric" Text="{Binding Entity.ApTxLimit}" />
        <SwitchCell Text="Authentication" On="{Binding Entity.Authentication}" />
        <EntryCell Label="Client Tx Limit" Keyboard="Numeric" Text="{Binding Entity.ClientTxLimit}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Disabled" On="{Binding Entity.Disabled}" />
        <SwitchCell Text="Forwarding" On="{Binding Entity.Forwarding}" />
        <EntryCell Label="Interface" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Mac Address" Text="{Binding Entity.MacAddress}" />
        <EntryCell Label="Management Protection Key" Text="{Binding Entity.ManagementProtectionKey}" />
        <EntryCell Label="Private Algo" Text="{Binding Entity.PrivateAlgo}" />
        <EntryCell Label="Private Key" Text="{Binding Entity.PrivateKey}" />
        <EntryCell Label="Private Pre Shared Key" Text="{Binding Entity.PrivatePreSharedKey}" />
        <EntryCell Label="Signal Range" Text="{Binding Entity.SignalRange}" />
        <EntryCell Label="Time" Text="{Binding Entity.Time}" />
<!--
        <EntryCell Label="Wireless Access List" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Wireless Access List" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Wireless Access List"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\WirelessAccessListDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessAccessListDetailPage : ContentPage
    {
        public WirelessAccessListDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessAccessListPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessAccessListPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless/access-list"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="ApTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding ApTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="Authentication" FlexLayout.Basis="50%" />
            <Label Text="{Binding Authentication}" FlexLayout.Basis="50%" />
            <Label Text="ClientTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding ClientTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Disabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Disabled}" FlexLayout.Basis="50%" />
            <Label Text="Forwarding" FlexLayout.Basis="50%" />
            <Label Text="{Binding Forwarding}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="ManagementProtectionKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding ManagementProtectionKey}" FlexLayout.Basis="50%" />
            <Label Text="PrivateAlgo" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrivateAlgo}" FlexLayout.Basis="50%" />
            <Label Text="PrivateKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrivateKey}" FlexLayout.Basis="50%" />
            <Label Text="PrivatePreSharedKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding PrivatePreSharedKey}" FlexLayout.Basis="50%" />
            <Label Text="SignalRange" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalRange}" FlexLayout.Basis="50%" />
            <Label Text="Time" FlexLayout.Basis="50%" />
            <Label Text="{Binding Time}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\WirelessAccessListPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessAccessListPage : ContentPage
    {
        public WirelessAccessListPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessChannelsDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessChannelsDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Wireless Channels">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless/channels"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="List" Text="{Binding Entity.List}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <EntryCell Label="Frequency" Text="{Binding Entity.Frequency}" />
        <EntryCell Label="Width" Text="{Binding Entity.Width}" />
        <EntryCell Label="Band" Text="{Binding Entity.Band}" />
        <EntryCell Label="Extension Channel" Text="{Binding Entity.ExtensionChannel}" />
<!--
        <EntryCell Label="Wireless Channels" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Wireless Channels" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Wireless Channels"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\WirelessChannelsDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessChannelsDetailPage : ContentPage
    {
        public WirelessChannelsDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessChannelsPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessChannelsPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless/channels"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="List" FlexLayout.Basis="50%" />
            <Label Text="{Binding List}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="Frequency" FlexLayout.Basis="50%" />
            <Label Text="{Binding Frequency}" FlexLayout.Basis="50%" />
            <Label Text="Width" FlexLayout.Basis="50%" />
            <Label Text="{Binding Width}" FlexLayout.Basis="50%" />
            <Label Text="Band" FlexLayout.Basis="50%" />
            <Label Text="{Binding Band}" FlexLayout.Basis="50%" />
            <Label Text="ExtensionChannel" FlexLayout.Basis="50%" />
            <Label Text="{Binding ExtensionChannel}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\WirelessChannelsPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessChannelsPage : ContentPage
    {
        public WirelessChannelsPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessRegistrationTableDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessRegistrationTableDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Wireless Registration Table">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless/registration-table"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Port 8021 Enabled" IsEnabled="False" Text="{Binding Entity.Port8021Enabled}" />
        <EntryCell Label="Ack Timeout" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.AckTimeout}" />
        <SwitchCell Text="Ap" On="{Binding Entity.Ap}" />
        <EntryCell Label="Ap Tx Limit" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.ApTxLimit}" />
        <EntryCell Label="Authentication Type" IsEnabled="False" Text="{Binding Entity.AuthenticationType}" />
        <SwitchCell Text="Bridge" On="{Binding Entity.Bridge}" />
        <EntryCell Label="Bytes" IsEnabled="False" Text="{Binding Entity.Bytes}" />
        <EntryCell Label="Client Tx Limit" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.ClientTxLimit}" />
        <EntryCell Label="Comment" IsEnabled="False" Text="{Binding Entity.Comment}" />
        <SwitchCell Text="Compression" On="{Binding Entity.Compression}" />
        <EntryCell Label="Distance" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.Distance}" />
        <EntryCell Label="Encryption" IsEnabled="False" Text="{Binding Entity.Encryption}" />
        <EntryCell Label="Evm Ch 0" IsEnabled="False" Text="{Binding Entity.EvmCh0}" />
        <EntryCell Label="Evm Ch 1" IsEnabled="False" Text="{Binding Entity.EvmCh1}" />
        <EntryCell Label="Evm Ch 2" IsEnabled="False" Text="{Binding Entity.EvmCh2}" />
        <EntryCell Label="Frame Bytes" IsEnabled="False" Text="{Binding Entity.FrameBytes}" />
        <EntryCell Label="Frames" IsEnabled="False" Text="{Binding Entity.Frames}" />
        <EntryCell Label="Framing Current Size" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.FramingCurrentSize}" />
        <EntryCell Label="Framing Limit" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.FramingLimit}" />
        <EntryCell Label="Framing Mode" IsEnabled="False" Text="{Binding Entity.FramingMode}" />
        <EntryCell Label="Group Encryption" IsEnabled="False" Text="{Binding Entity.GroupEncryption}" />
        <EntryCell Label="Hw Frame Bytes" IsEnabled="False" Text="{Binding Entity.HwFrameBytes}" />
        <EntryCell Label="Hw Frames" IsEnabled="False" Text="{Binding Entity.HwFrames}" />
        <EntryCell Label="Interface" IsEnabled="False" Text="{Binding Entity.Interface}" />
        <EntryCell Label="Last Activity" IsEnabled="False" Text="{Binding Entity.LastActivity}" />
        <EntryCell Label="Last Ip" IsEnabled="False" Text="{Binding Entity.LastIp}" />
        <EntryCell Label="Mac Address" IsEnabled="False" Text="{Binding Entity.MacAddress}" />
        <SwitchCell Text="Management Protection" On="{Binding Entity.ManagementProtection}" />
        <SwitchCell Text="Nstreme" On="{Binding Entity.Nstreme}" />
        <EntryCell Label="P Throughput" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.PThroughput}" />
        <EntryCell Label="Packed Bytes" IsEnabled="False" Text="{Binding Entity.PackedBytes}" />
        <EntryCell Label="Packed Frames" IsEnabled="False" Text="{Binding Entity.PackedFrames}" />
        <EntryCell Label="Packets" IsEnabled="False" Text="{Binding Entity.Packets}" />
        <EntryCell Label="Radio Name" IsEnabled="False" Text="{Binding Entity.RadioName}" />
        <EntryCell Label="Routeros Version" IsEnabled="False" Text="{Binding Entity.RouterosVersion}" />
        <EntryCell Label="Rx Ccq" IsEnabled="False" Text="{Binding Entity.RxCcq}" />
        <EntryCell Label="Rx Rate" IsEnabled="False" Text="{Binding Entity.RxRate}" />
        <EntryCell Label="Signal Strength" IsEnabled="False" Text="{Binding Entity.SignalStrength}" />
        <EntryCell Label="Signal Strength Ch 0" IsEnabled="False" Text="{Binding Entity.SignalStrengthCh0}" />
        <EntryCell Label="Signal Strength Ch 1" IsEnabled="False" Text="{Binding Entity.SignalStrengthCh1}" />
        <EntryCell Label="Signal Strength Ch 2" IsEnabled="False" Text="{Binding Entity.SignalStrengthCh2}" />
        <EntryCell Label="Signal To Noise" IsEnabled="False" Text="{Binding Entity.SignalToNoise}" />
        <EntryCell Label="Strength At Rates" IsEnabled="False" Text="{Binding Entity.StrengthAtRates}" />
        <EntryCell Label="Tdma Retx" IsEnabled="False" Text="{Binding Entity.TdmaRetx}" />
        <EntryCell Label="Tdma Rx Size" IsEnabled="False" Text="{Binding Entity.TdmaRxSize}" />
        <EntryCell Label="Tdma Timing Offset" IsEnabled="False" Text="{Binding Entity.TdmaTimingOffset}" />
        <EntryCell Label="Tdma Tx Size" Keyboard="Numeric" IsEnabled="False" Text="{Binding Entity.TdmaTxSize}" />
        <EntryCell Label="Tdma Windfull" IsEnabled="False" Text="{Binding Entity.TdmaWindfull}" />
        <EntryCell Label="Tx Ccq" IsEnabled="False" Text="{Binding Entity.TxCcq}" />
        <EntryCell Label="Tx Evm Ch 0" IsEnabled="False" Text="{Binding Entity.TxEvmCh0}" />
        <EntryCell Label="Tx Evm Ch 1" IsEnabled="False" Text="{Binding Entity.TxEvmCh1}" />
        <EntryCell Label="Tx Evm Ch 2" IsEnabled="False" Text="{Binding Entity.TxEvmCh2}" />
        <EntryCell Label="Tx Frames Timed Out" IsEnabled="False" Text="{Binding Entity.TxFramesTimedOut}" />
        <EntryCell Label="Tx Rate" IsEnabled="False" Text="{Binding Entity.TxRate}" />
        <EntryCell Label="Tx Signal Strength" IsEnabled="False" Text="{Binding Entity.TxSignalStrength}" />
        <EntryCell Label="Tx Signal Strength Ch 0" IsEnabled="False" Text="{Binding Entity.TxSignalStrengthCh0}" />
        <EntryCell Label="Tx Signal Strength Ch 1" IsEnabled="False" Text="{Binding Entity.TxSignalStrengthCh1}" />
        <EntryCell Label="Tx Signal Strength Ch 2" IsEnabled="False" Text="{Binding Entity.TxSignalStrengthCh2}" />
        <EntryCell Label="Uptime" IsEnabled="False" Text="{Binding Entity.Uptime}" />
        <SwitchCell Text="Wds" On="{Binding Entity.Wds}" />
        <SwitchCell Text="Wmm Enabled" On="{Binding Entity.WmmEnabled}" />
<!--
        <EntryCell Label="Wireless Registration Table" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Wireless Registration Table" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Wireless Registration Table"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\WirelessRegistrationTableDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessRegistrationTableDetailPage : ContentPage
    {
        public WirelessRegistrationTableDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessRegistrationTablePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessRegistrationTablePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless/registration-table"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Port8021Enabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding Port8021Enabled}" FlexLayout.Basis="50%" />
            <Label Text="AckTimeout" FlexLayout.Basis="50%" />
            <Label Text="{Binding AckTimeout}" FlexLayout.Basis="50%" />
            <Label Text="Ap" FlexLayout.Basis="50%" />
            <Label Text="{Binding Ap}" FlexLayout.Basis="50%" />
            <Label Text="ApTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding ApTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="AuthenticationType" FlexLayout.Basis="50%" />
            <Label Text="{Binding AuthenticationType}" FlexLayout.Basis="50%" />
            <Label Text="Bridge" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bridge}" FlexLayout.Basis="50%" />
            <Label Text="Bytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding Bytes}" FlexLayout.Basis="50%" />
            <Label Text="ClientTxLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding ClientTxLimit}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Compression" FlexLayout.Basis="50%" />
            <Label Text="{Binding Compression}" FlexLayout.Basis="50%" />
            <Label Text="Distance" FlexLayout.Basis="50%" />
            <Label Text="{Binding Distance}" FlexLayout.Basis="50%" />
            <Label Text="Encryption" FlexLayout.Basis="50%" />
            <Label Text="{Binding Encryption}" FlexLayout.Basis="50%" />
            <Label Text="EvmCh0" FlexLayout.Basis="50%" />
            <Label Text="{Binding EvmCh0}" FlexLayout.Basis="50%" />
            <Label Text="EvmCh1" FlexLayout.Basis="50%" />
            <Label Text="{Binding EvmCh1}" FlexLayout.Basis="50%" />
            <Label Text="EvmCh2" FlexLayout.Basis="50%" />
            <Label Text="{Binding EvmCh2}" FlexLayout.Basis="50%" />
            <Label Text="FrameBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding FrameBytes}" FlexLayout.Basis="50%" />
            <Label Text="Frames" FlexLayout.Basis="50%" />
            <Label Text="{Binding Frames}" FlexLayout.Basis="50%" />
            <Label Text="FramingCurrentSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding FramingCurrentSize}" FlexLayout.Basis="50%" />
            <Label Text="FramingLimit" FlexLayout.Basis="50%" />
            <Label Text="{Binding FramingLimit}" FlexLayout.Basis="50%" />
            <Label Text="FramingMode" FlexLayout.Basis="50%" />
            <Label Text="{Binding FramingMode}" FlexLayout.Basis="50%" />
            <Label Text="GroupEncryption" FlexLayout.Basis="50%" />
            <Label Text="{Binding GroupEncryption}" FlexLayout.Basis="50%" />
            <Label Text="HwFrameBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwFrameBytes}" FlexLayout.Basis="50%" />
            <Label Text="HwFrames" FlexLayout.Basis="50%" />
            <Label Text="{Binding HwFrames}" FlexLayout.Basis="50%" />
            <Label Text="Interface" FlexLayout.Basis="50%" />
            <Label Text="{Binding Interface}" FlexLayout.Basis="50%" />
            <Label Text="LastActivity" FlexLayout.Basis="50%" />
            <Label Text="{Binding LastActivity}" FlexLayout.Basis="50%" />
            <Label Text="LastIp" FlexLayout.Basis="50%" />
            <Label Text="{Binding LastIp}" FlexLayout.Basis="50%" />
            <Label Text="MacAddress" FlexLayout.Basis="50%" />
            <Label Text="{Binding MacAddress}" FlexLayout.Basis="50%" />
            <Label Text="ManagementProtection" FlexLayout.Basis="50%" />
            <Label Text="{Binding ManagementProtection}" FlexLayout.Basis="50%" />
            <Label Text="Nstreme" FlexLayout.Basis="50%" />
            <Label Text="{Binding Nstreme}" FlexLayout.Basis="50%" />
            <Label Text="PThroughput" FlexLayout.Basis="50%" />
            <Label Text="{Binding PThroughput}" FlexLayout.Basis="50%" />
            <Label Text="PackedBytes" FlexLayout.Basis="50%" />
            <Label Text="{Binding PackedBytes}" FlexLayout.Basis="50%" />
            <Label Text="PackedFrames" FlexLayout.Basis="50%" />
            <Label Text="{Binding PackedFrames}" FlexLayout.Basis="50%" />
            <Label Text="Packets" FlexLayout.Basis="50%" />
            <Label Text="{Binding Packets}" FlexLayout.Basis="50%" />
            <Label Text="RadioName" FlexLayout.Basis="50%" />
            <Label Text="{Binding RadioName}" FlexLayout.Basis="50%" />
            <Label Text="RouterosVersion" FlexLayout.Basis="50%" />
            <Label Text="{Binding RouterosVersion}" FlexLayout.Basis="50%" />
            <Label Text="RxCcq" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxCcq}" FlexLayout.Basis="50%" />
            <Label Text="RxRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding RxRate}" FlexLayout.Basis="50%" />
            <Label Text="SignalStrength" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalStrength}" FlexLayout.Basis="50%" />
            <Label Text="SignalStrengthCh0" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalStrengthCh0}" FlexLayout.Basis="50%" />
            <Label Text="SignalStrengthCh1" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalStrengthCh1}" FlexLayout.Basis="50%" />
            <Label Text="SignalStrengthCh2" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalStrengthCh2}" FlexLayout.Basis="50%" />
            <Label Text="SignalToNoise" FlexLayout.Basis="50%" />
            <Label Text="{Binding SignalToNoise}" FlexLayout.Basis="50%" />
            <Label Text="StrengthAtRates" FlexLayout.Basis="50%" />
            <Label Text="{Binding StrengthAtRates}" FlexLayout.Basis="50%" />
            <Label Text="TdmaRetx" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaRetx}" FlexLayout.Basis="50%" />
            <Label Text="TdmaRxSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaRxSize}" FlexLayout.Basis="50%" />
            <Label Text="TdmaTimingOffset" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaTimingOffset}" FlexLayout.Basis="50%" />
            <Label Text="TdmaTxSize" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaTxSize}" FlexLayout.Basis="50%" />
            <Label Text="TdmaWindfull" FlexLayout.Basis="50%" />
            <Label Text="{Binding TdmaWindfull}" FlexLayout.Basis="50%" />
            <Label Text="TxCcq" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxCcq}" FlexLayout.Basis="50%" />
            <Label Text="TxEvmCh0" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxEvmCh0}" FlexLayout.Basis="50%" />
            <Label Text="TxEvmCh1" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxEvmCh1}" FlexLayout.Basis="50%" />
            <Label Text="TxEvmCh2" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxEvmCh2}" FlexLayout.Basis="50%" />
            <Label Text="TxFramesTimedOut" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxFramesTimedOut}" FlexLayout.Basis="50%" />
            <Label Text="TxRate" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxRate}" FlexLayout.Basis="50%" />
            <Label Text="TxSignalStrength" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxSignalStrength}" FlexLayout.Basis="50%" />
            <Label Text="TxSignalStrengthCh0" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxSignalStrengthCh0}" FlexLayout.Basis="50%" />
            <Label Text="TxSignalStrengthCh1" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxSignalStrengthCh1}" FlexLayout.Basis="50%" />
            <Label Text="TxSignalStrengthCh2" FlexLayout.Basis="50%" />
            <Label Text="{Binding TxSignalStrengthCh2}" FlexLayout.Basis="50%" />
            <Label Text="Uptime" FlexLayout.Basis="50%" />
            <Label Text="{Binding Uptime}" FlexLayout.Basis="50%" />
            <Label Text="Wds" FlexLayout.Basis="50%" />
            <Label Text="{Binding Wds}" FlexLayout.Basis="50%" />
            <Label Text="WmmEnabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding WmmEnabled}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\WirelessRegistrationTablePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessRegistrationTablePage : ContentPage
    {
        public WirelessRegistrationTablePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSecurityProfileDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessSecurityProfileDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Wireless Security Profile">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless/security-profiles"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <EntryCell Label="Comment" Text="{Binding Entity.Comment}" />
        <EntryCell Label="Name" Text="{Binding Entity.Name}" />
        <SwitchCell Text="Management Protection" On="{Binding Entity.ManagementProtection}" />
        <EntryCell Label="Management Protection Key" Text="{Binding Entity.ManagementProtectionKey}" />
        <EntryCell Label="Wpa Pre Shared Key" Text="{Binding Entity.WpaPreSharedKey}" />
        <EntryCell Label="Wpa 2 Pre Shared Key" Text="{Binding Entity.Wpa2PreSharedKey}" />
        <EntryCell Label="Authentication Types" Text="{Binding Entity.AuthenticationTypes}" />
        <EntryCell Label="Group Ciphers" Text="{Binding Entity.GroupCiphers}" />
        <EntryCell Label="Unicast Ciphers" Text="{Binding Entity.UnicastCiphers}" />
        <EntryCell Label="Supplicant Identiy" Text="{Binding Entity.SupplicantIdentiy}" />
        <EntryCell Label="Group Key Update" Text="{Binding Entity.GroupKeyUpdate}" />
<!--
        <EntryCell Label="Wireless Security Profile" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Wireless Security Profile" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Wireless Security Profile"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSecurityProfileDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessSecurityProfileDetailPage : ContentPage
    {
        public WirelessSecurityProfileDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSecurityProfilePage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessSecurityProfilePage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless/security-profiles"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="Comment" FlexLayout.Basis="50%" />
            <Label Text="{Binding Comment}" FlexLayout.Basis="50%" />
            <Label Text="Mode" FlexLayout.Basis="50%" />
            <Label Text="{Binding Mode}" FlexLayout.Basis="50%" />
            <Label Text="Name" FlexLayout.Basis="50%" />
            <Label Text="{Binding Name}" FlexLayout.Basis="50%" />
            <Label Text="ManagementProtection" FlexLayout.Basis="50%" />
            <Label Text="{Binding ManagementProtection}" FlexLayout.Basis="50%" />
            <Label Text="ManagementProtectionKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding ManagementProtectionKey}" FlexLayout.Basis="50%" />
            <Label Text="WpaPreSharedKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding WpaPreSharedKey}" FlexLayout.Basis="50%" />
            <Label Text="Wpa2PreSharedKey" FlexLayout.Basis="50%" />
            <Label Text="{Binding Wpa2PreSharedKey}" FlexLayout.Basis="50%" />
            <Label Text="AuthenticationTypes" FlexLayout.Basis="50%" />
            <Label Text="{Binding AuthenticationTypes}" FlexLayout.Basis="50%" />
            <Label Text="GroupCiphers" FlexLayout.Basis="50%" />
            <Label Text="{Binding GroupCiphers}" FlexLayout.Basis="50%" />
            <Label Text="UnicastCiphers" FlexLayout.Basis="50%" />
            <Label Text="{Binding UnicastCiphers}" FlexLayout.Basis="50%" />
            <Label Text="SupplicantIdentiy" FlexLayout.Basis="50%" />
            <Label Text="{Binding SupplicantIdentiy}" FlexLayout.Basis="50%" />
            <Label Text="GroupKeyUpdate" FlexLayout.Basis="50%" />
            <Label Text="{Binding GroupKeyUpdate}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\WirelessSecurityProfilePage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessSecurityProfilePage : ContentPage
    {
        public WirelessSecurityProfilePage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSnifferDetailPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessSnifferDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="Wireless Sniffer">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="interface/wireless/sniffer"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>

        <EntryCell Label="Id" IsEnabled="False" Text="{Binding Entity.Id}" />
        <SwitchCell Text="Streaming Enabled" On="{Binding Entity.StreamingEnabled}" />
        <EntryCell Label="Streaming Server" Text="{Binding Entity.StreamingServer}" />
        <SwitchCell Text="Multiple Channels" On="{Binding Entity.MultipleChannels}" />
        <EntryCell Label="Channel Time" Text="{Binding Entity.ChannelTime}" />
<!--
        <EntryCell Label="Wireless Sniffer" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="Wireless Sniffer" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="Wireless Sniffer"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSnifferDetailPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessSnifferDetailPage : ContentPage
    {
        public WirelessSnifferDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Generated\Views\WirelessSnifferPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.WirelessSnifferPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="interface/wireless/sniffer"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
            <Label Text="Id" FlexLayout.Basis="50%" />
            <Label Text="{Binding Id}" FlexLayout.Basis="50%" />
            <Label Text="StreamingEnabled" FlexLayout.Basis="50%" />
            <Label Text="{Binding StreamingEnabled}" FlexLayout.Basis="50%" />
            <Label Text="StreamingServer" FlexLayout.Basis="50%" />
            <Label Text="{Binding StreamingServer}" FlexLayout.Basis="50%" />
            <Label Text="MultipleChannels" FlexLayout.Basis="50%" />
            <Label Text="{Binding MultipleChannels}" FlexLayout.Basis="50%" />
            <Label Text="ChannelTime" FlexLayout.Basis="50%" />
            <Label Text="{Binding ChannelTime}" FlexLayout.Basis="50%" />

          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Generated\Views\WirelessSnifferPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class WirelessSnifferPage : ContentPage
    {
        public WirelessSnifferPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\MikroTik.EntityBuilder.csproj
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp3.1</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="tik4net" Version="3.5.0" />
    <PackageReference Include="Humanizer.Core" Version="2.7.9" />
  </ItemGroup>

  <ItemGroup>
    <Compile Remove="Generated\**" />
    <None Remove="Generated\**" />
    <EmbeddedResource Remove="Generated\**" />
  </ItemGroup>

  <ItemGroup>
    <None Update="Templates\ViewModelTemplate">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Update="Templates\ViewTemplate">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Update="Templates\ViewTemplateCodeBehind">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
  </ItemGroup>
</Project>


File: /MikroTik.EntityBuilder\MikroTik.EntityBuilder.sln
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio 15
VisualStudioVersion = 15.0.26124.0
MinimumVisualStudioVersion = 15.0.26124.0
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "MikroTik.EntityBuilder", "MikroTik.EntityBuilder.csproj", "{620B99E2-189A-464B-A02A-181E4C2D52ED}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Debug|x64 = Debug|x64
		Debug|x86 = Debug|x86
		Release|Any CPU = Release|Any CPU
		Release|x64 = Release|x64
		Release|x86 = Release|x86
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|x64.ActiveCfg = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|x64.Build.0 = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|x86.ActiveCfg = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Debug|x86.Build.0 = Debug|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|Any CPU.Build.0 = Release|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|x64.ActiveCfg = Release|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|x64.Build.0 = Release|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|x86.ActiveCfg = Release|Any CPU
		{620B99E2-189A-464B-A02A-181E4C2D52ED}.Release|x86.Build.0 = Release|Any CPU
	EndGlobalSection
EndGlobal


File: /MikroTik.EntityBuilder\Program.cs
﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;
using tik4net.Objects;
using Humanizer;

namespace MikroTik.EntityBuilder
{
    class Program
    {
        private const string XmlNamespace = @"
             xmlns:XMLPREFIX=""clr-namespace:TIK4NETNAMESPACE;assembly=tik4net.objects""";
        private const string GeneratedExtensions = @"using ModemConfigurator.Views;
using ModemConfigurator.ViewModels;
using Prism.Ioc;

namespace ModemConfigurator
{
    public static class GeneratedExtensions
    {
        public static void RegisterAutoGeneratedViews(this IContainerRegistry containerRegistry)
        {
Registrations
        }
    }
}";
        private const string LabelTemplate = @"            <Label Text=""PropertyName"" FlexLayout.Basis=""50%"" />
            <Label Text=""{Binding PropertyName}"" FlexLayout.Basis=""50%"" />
";
        private const string MenuTemplate = @"                        <Button Text=""FriendlyName"" 
                                Command=""{Binding NavigateCommand}"" 
                                CommandParameter=""NavigationPage/TEntityPage"" 
                                Margin=""20"" />
";
        private const string RegistrationTemplate = "            containerRegistry.RegisterForNavigation<TEntityPage, TEntityPageViewModel>();\n            containerRegistry.RegisterForNavigation<TEntityDetailPage, TEntityDetailPageViewModel>();\n";
        private const string EntryCellTemplate = @"
        <EntryCell Label=""FriendlyName""OTHERTAGS Text=""{Binding Entity.PropertyName}"" />";
        private const string SwitchCellTemplate = @"
        <SwitchCell Text=""FriendlyName"" On=""{Binding Entity.PropertyName}"" />";
        private const string PickerCellTemplate = @"
        <ViewCell>
            <FlexLayout Wrap=""Wrap"">
              <Label Text=""FriendlyName""
                     FlexLayout.Basis=""25%"" />
              <controls:Picker x:TypeArguments=""XMLPREFIX:EnumName""
                               SelectedItem=""{Binding Entity.PropertyName}""
                               FlexLayout.Basis=""75%"" />
            </FlexLayout>
        </ViewCell>";



        static void Main(string[] args)
        {
            Directory.Delete("Generated", true);
            tik4net.Objects.System.SystemResource resource;
            var assembly = typeof(tik4net.Objects.MacAddress).Assembly;

            string menu = string.Empty;
            string registration = string.Empty;
            int i = 1;
            foreach(var type in assembly.ExportedTypes.Where(t => t.GetCustomAttributes().Any(a => a is TikEntityAttribute)))
            {
                Console.WriteLine($" {i++}) {type.FullName}");
                GenerateViewModel(type);
                GenerateXAMLView(type);
                GenerateCodeBehind(type);
                GenerateDetailCodeBehind(type);
                GenerateDetailViewModel(type);
                GenerateDetailXAML(type);

                // var entity = Regex.Replace(MenuTemplate, "TEntity", type.Name);
                // entity = Regex.Replace(entity, "FriendlyName", type.Name.Humanize());
                // menu += entity;

                registration += Regex.Replace(RegistrationTemplate, "TEntity", type.Name);
            }

            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}GeneratedExtensions.cs", Regex.Replace(GeneratedExtensions, "Registrations", registration));
        }

        static void GenerateViewModel(Type type)
        {
            var viewmodel = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}ViewModelTemplate");
            viewmodel = Regex.Replace(viewmodel, "TypeNamespace", type.Namespace);
            viewmodel = Regex.Replace(viewmodel, "TEntity", type.Name);
            viewmodel = Regex.Replace(viewmodel, "FriendlyName", type.Name.Humanize(LetterCasing.Title));

            if(type.Namespace == "tik4net.Objects")
            {
                viewmodel = Regex.Replace(viewmodel, "using tik4net.Objects;\nusing tik4net.Objects;", "using tik4net.Objects;");
            }

            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}ViewModels");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}ViewModels{Path.DirectorySeparatorChar}{type.Name}PageViewModel.cs", viewmodel); 
        }

        static void GenerateXAMLView(Type type)
        {
            var xaml = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}ViewTemplate");

            string properties = string.Empty;
            foreach(var prop in type.GetProperties())
            {
                properties += Regex.Replace(LabelTemplate, "PropertyName", prop.Name);
            }

            var entityAttribute = type.GetCustomAttribute<TikEntityAttribute>();
            xaml = Regex.Replace(xaml, "EntityPath", entityAttribute.EntityPath);
            xaml = Regex.Replace(xaml, "PropertyLabels", properties);
            xaml = Regex.Replace(xaml, "TEntity", type.Name);

            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}Views");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}Views{Path.DirectorySeparatorChar}{type.Name}Page.xaml", xaml); 
        }

        static void GenerateCodeBehind(Type type)
        {
            var codeBehind = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}ViewTemplateCodeBehind");
            codeBehind = Regex.Replace(codeBehind, "TEntity", type.Name);
            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}Views");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}Views{Path.DirectorySeparatorChar}{type.Name}Page.xaml.cs", codeBehind);
        }

        static void GenerateDetailViewModel(Type type)
        {
            var viewmodel = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}DetailViewModelTemplate");
            viewmodel = Regex.Replace(viewmodel, "TypeNamespace", type.Namespace);
            viewmodel = Regex.Replace(viewmodel, "TEntity", type.Name);
            viewmodel = Regex.Replace(viewmodel, "FriendlyName", type.Name.Humanize(LetterCasing.Title));

            if(type.Namespace == "tik4net.Objects")
            {
                viewmodel = Regex.Replace(viewmodel, "using tik4net.Objects;\nusing tik4net.Objects;", "using tik4net.Objects;");
            }

            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}ViewModels");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}ViewModels{Path.DirectorySeparatorChar}{type.Name}DetailPageViewModel.cs", viewmodel); 
        }

        static void GenerateDetailXAML(Type type)
        {
            var xaml = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}DetailPageTemplate");
            string namespaces = string.Empty;
            string properties = string.Empty;
            foreach(var prop in type.GetProperties())
            {
                string cell = string.Empty;
                string tags = string.Empty;
                var tikProperty = prop.GetCustomAttribute<TikPropertyAttribute>();

                if(prop.PropertyType == typeof(string))
                {
                    cell = EntryCellTemplate;
                }
                else if(prop.PropertyType == typeof(bool))
                {
                    cell = SwitchCellTemplate;
                }
                else if(prop.PropertyType == typeof(int) || prop.PropertyType == typeof(long))
                {
                    tags += @" Keyboard=""Numeric""";
                    cell = EntryCellTemplate;
                }
                else if(prop.PropertyType.IsEnum && prop.PropertyType.MemberType != MemberTypes.NestedType)
                {
                    var temp = prop.PropertyType.MemberType == MemberTypes.NestedType ?
                                        $"{prop.PropertyType.Namespace}.{prop.DeclaringType.Name}" :
                                          prop.PropertyType.Namespace;
                    var entityNamespace = Regex.Replace(XmlNamespace, "TIK4NETNAMESPACE", temp);
                    var entityName = prop.PropertyType.Name.ToLower();
                    entityNamespace = Regex.Replace(entityNamespace, "XMLPREFIX", entityName);
                    if(!namespaces.Contains(entityName))
                    {
                        namespaces += entityNamespace;
                    }

                    // string enumName = prop.PropertyType.MemberType == MemberTypes.NestedType ?
                    //                       $"{prop.DeclaringType.Name}.{prop.PropertyType.Name}" :
                    //                       prop.PropertyType.Name;
                    cell = Regex.Replace(PickerCellTemplate, "EnumName", prop.PropertyType.Name);
                    cell = Regex.Replace(cell, "XMLPREFIX", entityName);
                }
                else if(prop.PropertyType == typeof(TimeSpan) && tikProperty.IsReadOnly)
                {
                    cell = EntryCellTemplate;
                }
                // TODO: Add cell for TimeSpan
                else
                {
                    Console.WriteLine($"{type.Name} - {prop.Name} is of type: {prop.PropertyType.Name}");
                }

                if(tikProperty.IsReadOnly)
                {
                    tags += @" IsEnabled=""False""";
                }
                
                cell = Regex.Replace(cell, "OTHERTAGS", tags);
                cell = Regex.Replace(cell, "FriendlyName", prop.Name.Humanize(LetterCasing.Title));
                cell = Regex.Replace(cell, "PropertyName", prop.Name);
                properties += cell;
            }

            var entityAttribute = type.GetCustomAttribute<TikEntityAttribute>();
            xaml = Regex.Replace(xaml, "EntityPath", entityAttribute.EntityPath);
            xaml = Regex.Replace(xaml, "PropertyCells", properties);
            xaml = Regex.Replace(xaml, "TEntity", type.Name);
            xaml = Regex.Replace(xaml, "TIK4NETNAMESPACE", namespaces);
            xaml = Regex.Replace(xaml, "FriendlyName", type.Name.Humanize(LetterCasing.Title));

            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}Views");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}Views{Path.DirectorySeparatorChar}{type.Name}DetailPage.xaml", xaml); 
        }

        static void GenerateDetailCodeBehind(Type type)
        {
            var codeBehind = File.ReadAllText($"Templates{Path.DirectorySeparatorChar}DetailPageTemplateCodeBehind");
            codeBehind = Regex.Replace(codeBehind, "TEntity", type.Name);
            Directory.CreateDirectory($"Generated{Path.DirectorySeparatorChar}Views");
            File.WriteAllText($"Generated{Path.DirectorySeparatorChar}Views{Path.DirectorySeparatorChar}{type.Name}DetailPage.xaml.cs", codeBehind);
        }
    }
}


File: /MikroTik.EntityBuilder\Templates\DetailPageTemplate
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             xmlns:controls="clr-namespace:ModemConfigurator.Controls;ModemConfigurator"TIK4NETNAMESPACE
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.TEntityDetailPage">
  <TableView HasUnevenRows="true"
             Intent="Form">
    <TableRoot>
      <TableSection Title="FriendlyName">
        <ViewCell>
          <Frame BackgroundColor="Teal">
            <Label Text="EntityPath"
                   FontSize="Large"
                   TextColor="WhiteSmoke" />
          </Frame>
        </ViewCell>
PropertyCells
<!--
        <EntryCell Label="FriendlyName" Text="{Binding Entity.PropertyName}" />
        <SwitchCell Text="FriendlyName" On="{Binding Entity.PropertyName}" />
        <ViewCell>
            <FlexLayout Wrap="Wrap">
              <Label Text="FriendlyName"
                     FlexLayout.Basis="25%" />
              <controls:Picker x:TypeArguments="models:EnumName"
                               SelectedItem="{Binding Entity.PropertyName}"
                               FlexLayout.Basis="75%" />
            </FlexLayout>
        </ViewCell>
-->
      </TableSection>
      <TableSection Title="Commands">
        <ViewCell>
          <Button Text="Save"
                  Command="{Binding SaveCommand}" />
        </ViewCell>
      </TableSection>
    </TableRoot>
  </TableView>
</ContentPage>


File: /MikroTik.EntityBuilder\Templates\DetailPageTemplateCodeBehind
﻿using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class TEntityDetailPage : ContentPage
    {
        public TEntityDetailPage()
        {
            InitializeComponent();
        }
    }
}


File: /MikroTik.EntityBuilder\Templates\DetailViewModelTemplate
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using TypeNamespace;

namespace ModemConfigurator.ViewModels
{
    public class TEntityDetailPageViewModel : BaseDetailViewModel<TEntity>
    {
        public TEntityDetailPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "FriendlyName Detail";
        }
    }
}


File: /MikroTik.EntityBuilder\Templates\ViewModelTemplate
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using System.Collections.ObjectModel;
using tik4net.Objects;
using TypeNamespace;

namespace ModemConfigurator.ViewModels
{
    public class TEntityPageViewModel : BaseCollectionViewModel<TEntity>
    {
        public TEntityPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService)
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "FriendlyName";
        }
    }
}


File: /MikroTik.EntityBuilder\Templates\ViewTemplate
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.TEntityPage">
  <ContentPage.ToolbarItems>
    <ToolbarItem Icon="add.png"
                 Text="Add"
                 Command="{Binding AddItemCommand}" />
  </ContentPage.ToolbarItems>
  <ListView ItemsSource="{Binding Items}"
              HasUnevenRows="true">
    <ListView.Behaviors>
      <prism:EventToCommandBehavior EventName="ItemTapped"
                                        EventArgsParameterPath="Item"
                                        Command="{Binding ItemSelectedCommand}" />
    </ListView.Behaviors>
    <ListView.Header>
      <Frame BackgroundColor="Teal">
        <Label Text="EntityPath"
               FontSize="Large"
               TextColor="WhiteSmoke" />
      </Frame>
    </ListView.Header>
    <ListView.ItemTemplate>
      <DataTemplate>
        <ViewCell>
          <FlexLayout Padding="20,0"
                      Wrap="Wrap">
PropertyLabels
          </FlexLayout>
        </ViewCell>
      </DataTemplate>
    </ListView.ItemTemplate>
    <ListView.Footer>
      <StackLayout Spacing="0">
        <Label Text="    Connected"
                TextColor="White"
                BackgroundColor="Green"
                IsVisible="{Binding IsConnected}" />
        <Label Text="    Not Connected"
                TextColor="White"
                BackgroundColor="Red"
                IsVisible="{Binding IsNotConnected}" />
      </StackLayout>
    </ListView.Footer>
  </ListView>
</ContentPage>

File: /MikroTik.EntityBuilder\Templates\ViewTemplateCodeBehind
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class TEntityPage : ContentPage
    {
        public TEntityPage()
        {
            InitializeComponent();
        }
    }
}


File: /ModemConfigurator\ModemConfigurator.sln
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 16
VisualStudioVersion = 16.0.29721.120
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "ModemConfigurator", "src\ModemConfigurator\ModemConfigurator.csproj", "{EC2573EC-6583-420A-AA16-F1A25B6D2B70}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ModemConfigurator.iOS", "src\ModemConfigurator.iOS\ModemConfigurator.iOS.csproj", "{0F462199-2685-4E47-83AD-201D939E9BDF}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Ad-Hoc|Any CPU = Ad-Hoc|Any CPU
		Ad-Hoc|iPhone = Ad-Hoc|iPhone
		Ad-Hoc|iPhoneSimulator = Ad-Hoc|iPhoneSimulator
		AppStore|Any CPU = AppStore|Any CPU
		AppStore|iPhone = AppStore|iPhone
		AppStore|iPhoneSimulator = AppStore|iPhoneSimulator
		Debug|Any CPU = Debug|Any CPU
		Debug|iPhone = Debug|iPhone
		Debug|iPhoneSimulator = Debug|iPhoneSimulator
		Release|Any CPU = Release|Any CPU
		Release|iPhone = Release|iPhone
		Release|iPhoneSimulator = Release|iPhoneSimulator
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|Any CPU.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|Any CPU.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|iPhone.ActiveCfg = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|iPhone.Build.0 = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|iPhoneSimulator.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Ad-Hoc|iPhoneSimulator.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|Any CPU.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|Any CPU.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|iPhone.ActiveCfg = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|iPhone.Build.0 = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|iPhoneSimulator.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.AppStore|iPhoneSimulator.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|iPhone.ActiveCfg = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|iPhone.Build.0 = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|iPhoneSimulator.ActiveCfg = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Debug|iPhoneSimulator.Build.0 = Debug|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|Any CPU.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|iPhone.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|iPhone.Build.0 = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|iPhoneSimulator.ActiveCfg = Release|Any CPU
		{EC2573EC-6583-420A-AA16-F1A25B6D2B70}.Release|iPhoneSimulator.Build.0 = Release|Any CPU
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Ad-Hoc|Any CPU.ActiveCfg = Ad-Hoc|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Ad-Hoc|iPhone.ActiveCfg = Ad-Hoc|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Ad-Hoc|iPhone.Build.0 = Ad-Hoc|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Ad-Hoc|iPhoneSimulator.ActiveCfg = Ad-Hoc|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Ad-Hoc|iPhoneSimulator.Build.0 = Ad-Hoc|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.AppStore|Any CPU.ActiveCfg = AppStore|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.AppStore|iPhone.ActiveCfg = AppStore|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.AppStore|iPhone.Build.0 = AppStore|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.AppStore|iPhoneSimulator.ActiveCfg = AppStore|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.AppStore|iPhoneSimulator.Build.0 = AppStore|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|Any CPU.ActiveCfg = Debug|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|Any CPU.Build.0 = Debug|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|iPhone.ActiveCfg = Debug|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|iPhone.Build.0 = Debug|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|iPhoneSimulator.ActiveCfg = Debug|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Debug|iPhoneSimulator.Build.0 = Debug|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|Any CPU.ActiveCfg = Release|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|Any CPU.Build.0 = Release|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|iPhone.ActiveCfg = Release|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|iPhone.Build.0 = Release|iPhone
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|iPhoneSimulator.ActiveCfg = Release|iPhoneSimulator
		{0F462199-2685-4E47-83AD-201D939E9BDF}.Release|iPhoneSimulator.Build.0 = Release|iPhoneSimulator
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {9D540C3E-8FDE-4A8D-A4C3-47EF2C37B3D4}
	EndGlobalSection
EndGlobal


File: /ModemConfigurator\NuGet.config
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="NuGet.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
  <activePackageSource>
    <add key="All" value="(Aggregate source)" />
  </activePackageSource>
</configuration>

File: /ModemConfigurator\src\ModemConfigurator\App.xaml
<?xml version="1.0" encoding="utf-8"?>
<prism:PrismApplication xmlns="http://xamarin.com/schemas/2014/forms"
                        xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                        xmlns:prism="http://prismlibrary.com"
                        x:Class="ModemConfigurator.App">
  <prism:PrismApplication.Resources>
    <ResourceDictionary>
      <Color x:Key="PrimaryDark">#000066</Color>
      <Style TargetType="NavigationPage">
        <Setter Property="BackgroundColor" Value="{StaticResource PrimaryDark}" />
        <Setter Property="BarTextColor" Value="White" />
      </Style>
      <Style TargetType="Entry">
        <Setter Property="BackgroundColor" Value="White" />
        <Setter Property="TextColor" Value="Black" />
        <Setter Property="PlaceholderColor" Value="Gray" />
      </Style>
    </ResourceDictionary>
  </prism:PrismApplication.Resources>
</prism:PrismApplication>

File: /ModemConfigurator\src\ModemConfigurator\App.xaml.cs
﻿using System;
using System.Diagnostics;
using System.Threading.Tasks;
using Microsoft.AppCenter;
using Microsoft.AppCenter.Analytics;
using Microsoft.AppCenter.Crashes;
using Microsoft.AppCenter.Distribute;
using ModemConfigurator.Helpers;
using ModemConfigurator.Services;
using Prism;
using Prism.Ioc;
using Prism.Navigation;
using Xamarin.Forms.Xaml;

[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace ModemConfigurator
{
    [AutoRegisterForNavigation]
    public partial class App : PrismApplication
    {
        /* 
         * The Xamarin Forms XAML Previewer in Visual Studio uses System.Activator.CreateInstance.
         * This imposes a limitation in which the App class must have a default constructor. 
         * App(IPlatformInitializer initializer = null) cannot be handled by the Activator.
         */
        public App() : this(null) { }

        public App(IPlatformInitializer initializer) : base(initializer) { }

        protected override void Initialize()
        {
            var sw = new Stopwatch();
            sw.Start();
            base.Initialize();
            sw.Stop();
            Console.WriteLine($"Total Initialization: {sw.ElapsedMilliseconds} milliseconds");
        }

        protected override async void OnInitialized()
        {
            Xamarin.Forms.Internals.Log.Listeners.Add(new FormsLogListener());
            Distribute.ReleaseAvailable = OnReleaseAvailable;
            AppCenter.Start(Secrets.AppCenterSecret,
                            typeof(Analytics), typeof(Crashes), typeof(Distribute));
            //await NavigationService.NavigateAsync("/LoadingPage");

            var result = await NavigationService.NavigateAsync("/MainPage/NavigationPage/ModemSettingsPage");
            if (!result.Success)
            {
                Console.WriteLine(result.Exception);
                await NavigationService.NavigateAsync("/ErrorPage", ("exception", result.Exception));
            }
        }

        protected override void RegisterTypes(IContainerRegistry containerRegistry)
        {
            InitializeComponent();
            containerRegistry.RegisterSingleton<IModemSettings, ModemSettings>();
            containerRegistry.RegisterForNavigation<Xamarin.Forms.NavigationPage>();
        }

        private bool OnReleaseAvailable(ReleaseDetails releaseDetails)
        {
            // Look at releaseDetails public properties to get version information, release notes text or release notes URL
            string versionName = releaseDetails.ShortVersion;
            string versionCodeOrBuildNumber = releaseDetails.Version;
            string releaseNotes = releaseDetails.ReleaseNotes;
            Uri releaseNotesUrl = releaseDetails.ReleaseNotesUrl;

            // custom dialog
            var title = "Version " + versionName + " available!";
            Task answer;

            // On mandatory update, user cannot postpone
            if (releaseDetails.MandatoryUpdate)
            {
                answer = Current.MainPage.DisplayAlert(title, releaseNotes, "Download and Install");
            }
            else
            {
                answer = Current.MainPage.DisplayAlert(title, releaseNotes, "Download and Install", "Maybe tomorrow...");
            }
            answer.ContinueWith((task) =>
            {
                // If mandatory or if answer was positive
                if (releaseDetails.MandatoryUpdate || (task as Task<bool>).Result)
                {
                    // Notify SDK that user selected update
                    Distribute.NotifyUpdateAction(UpdateAction.Update);
                }
                else
                {
                    // Notify SDK that user selected postpone (for 1 day)
                    // Note that this method call is ignored by the SDK if the update is mandatory
                    Distribute.NotifyUpdateAction(UpdateAction.Postpone);
                }
            });

            // Return true if you are using your own dialog, false otherwise
            return true;
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Controls\Picker{T}.cs
﻿using System;
using Xamarin.Forms;

namespace ModemConfigurator.Controls
{
    public class Picker<T> : Picker
    {
        public Picker()
        {
            foreach(var value in Enum.GetValues(typeof(T)))
            {
                ItemsSource.Add(value);
            }
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ModemConfigurator.csproj
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="tik4net" Version="3.5.0" />
    <PackageReference Include="Xamarin.Forms" Version="4.4.0.991640" />
    <PackageReference Include="Prism.Forms.Extended" Version="7.2.0.898" />
    <PackageReference Include="Shiny.Prism" Version="7.2.0.898" />
    <PackageReference Include="Humanizer.Core" Version="2.7.9" />
    <PackageReference Include="Refractored.MvvmHelpers" Version="1.6.1-beta" />
    <PackageReference Include="Microsoft.AppCenter.Crashes" Version="3.0.0" />
    <PackageReference Include="Microsoft.AppCenter.Analytics" Version="3.0.0" />
    <PackageReference Include="Microsoft.AppCenter.Distribute" Version="3.0.0" />
    <PackageReference Include="Mobile.BuildTools" Version="1.4.0.638" PrivateAssets="all" />
    <PackageReference Include="Shiny.Notifications" Version="1.0.0.1182" />
    <PackageReference Include="Shiny.Core" Version="1.0.0.1182" />
  </ItemGroup>

  <ItemGroup>
    <EmbeddedResource Include="$(GeneratedFilesFolder)\**\*.xaml"
                      Link="Views\Generated\%(Filename)%(Extension)"
                      Generator="MSBuild:UpdateDesignTimeXaml"
                      Visible="true" />
    <Compile Include="$(GeneratedFilesFolder)\ViewModels\*.cs"
             Link="ViewModels\Generated\%(Filename)%(Extension)"
             Visible="true" />
    <Compile Include="$(GeneratedFilesFolder)\Views\*.xaml.cs"
             Link="Views\Generated\%(Filename)%(Extension)"
             DependsOn="%(Filename)"
             Visible="true" />
  </ItemGroup>

</Project>

File: /ModemConfigurator\src\ModemConfigurator\ModemStartup.cs
﻿using System;
using Microsoft.Extensions.DependencyInjection;
using Shiny;
using Shiny.Prism;

namespace ModemConfigurator
{
    public class ModemStartup : PrismStartup
    {
        protected override void ConfigureServices(IServiceCollection services)
        {
            services.UseNotifications();
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Services\FormsLogListener.cs
﻿using System;
using Xamarin.Forms.Internals;

namespace ModemConfigurator.Services
{
    public class FormsLogListener : LogListener
    {
        public override void Warning(string category, string message)
        {
            Console.WriteLine($"**** {category}: {message}");
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Services\IModemSettings.cs
﻿namespace ModemConfigurator.Services
{
    public interface IModemSettings
    {
        string Host { get; set; }

        string User { get; set; }

        string Password { get; set; }


    }
}


File: /ModemConfigurator\src\ModemConfigurator\Services\ModemSettings.cs
﻿using Prism.Mvvm;
namespace ModemConfigurator.Services
{
    public class ModemSettings : BindableBase, IModemSettings
    {
        public ModemSettings()
        {
            Host = "192.168.88.1";
            User = "admin";
            Password = string.Empty;
        }

        public string Host { get; set; }
        public string User { get; set; }
        public string Password { get; set; }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\BaseCollectionViewModel.cs
using System;
using System.Collections.ObjectModel;
using Prism.Navigation;
using tik4net.Objects;
using Prism.Services;
using Prism.Commands;

namespace ModemConfigurator.ViewModels
{
    public class BaseCollectionViewModel<TEntity> : ViewModelBase
        where TEntity : new()
    {
        public BaseCollectionViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService) 
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Items = new ObservableCollection<TEntity>();
            ItemSelectedCommand = new DelegateCommand<TEntity>(OnItemSelectedCommandExecuted);
            AddItemCommand = new DelegateCommand(OnAddItemCommandExecuted);
        }

        public ObservableCollection<TEntity> Items { get; }

        public DelegateCommand<TEntity> ItemSelectedCommand { get; }

        public DelegateCommand AddItemCommand { get; }

        public override void OnNavigatedTo(INavigationParameters parameters)
        {
            try
            {
                using(var connection = CreateConnection())
                {
                    Items.Clear();
                    foreach(var item in connection.LoadAll<TEntity>())
                    {
                        Items.Add(item);
                    }
                }
            }
            catch (Exception ex)
            {
                _pageDialogService.DisplayAlertAsync(ex.GetType().Name, ex.Message, "Ok");
                Console.WriteLine(ex);
            }
        }

        public void OnAddItemCommandExecuted() => OnItemSelectedCommandExecuted(default(TEntity));

        private async void OnItemSelectedCommandExecuted(TEntity entity)
        {
            await NavigationService.NavigateAsync($"{typeof(TEntity).Name}DetailPage", new NavigationParameters
            {
                { "Entity", entity }
            });
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\BaseDetailViewModel.cs
﻿using System;
using ModemConfigurator.Services;
using Prism.Navigation;
using Prism.Services;
using Prism.Commands;
using tik4net.Objects;

namespace ModemConfigurator.ViewModels
{
    public class BaseDetailViewModel<TEntity> : ViewModelBase
        where TEntity : new()
    {
        public BaseDetailViewModel(INavigationService navigationService, IPageDialogService pageDialogService, IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService) 
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
        }

        public TEntity Entity { get; set; }

        public DelegateCommand SaveCommand { get; }

        public override void OnNavigatingTo(INavigationParameters parameters)
        {
            Entity = parameters.GetValue<TEntity>("Entity");
        }

        private void OnSaveCommandExecuted()
        {
            using(var connection = CreateConnection())
            {
                connection.Save(Entity);
            }
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\ErrorPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using Shiny.Net;

namespace ModemConfigurator.ViewModels
{
    public class ErrorPageViewModel : ViewModelBase
    {
        public ErrorPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, Services.IModemSettings modemSettings, IConnectivity connectivity, IDeviceService deviceService) 
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
        }

        public string ErrorText { get; set; }

        public override void OnNavigatingTo(INavigationParameters parameters)
        {
            ErrorText = parameters.GetValue<Exception>("exception").ToString();
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\LoadingPageViewModel.cs
using ModemConfigurator.Views;
using Prism.Ioc;
using Prism.Navigation;
using Prism.Services;
using Xamarin.Forms;
using Xamarin.Forms.PlatformConfiguration;
using Xamarin.Forms.PlatformConfiguration.iOSSpecific;
using Prism.Common;

namespace ModemConfigurator.ViewModels
{
    //public class LoadingPageViewModel : ViewModelBase
    //{
    //    private IContainerRegistry _containerRegistry { get; }

    //    public LoadingPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, 
    //                                Services.IModemSettings modemSettings, IContainerRegistry containerRegistry) 
    //        : base(navigationService, pageDialogService, modemSettings)
    //    {
    //        _containerRegistry = containerRegistry;
    //    }

    //    public override async void OnNavigatedTo(INavigationParameters parameters)
    //    {
    //        _containerRegistry.RegisterForNavigation<MainPage, MainPageViewModel>();
    //        _containerRegistry.RegisterForNavigation<ModemSettingsPage, ModemSettingsPageViewModel>();
    //        _containerRegistry.RegisterForNavigation<ErrorPage, ErrorPageViewModel>();

    //        _containerRegistry.RegisterAutoGeneratedViews();

    //        var result = await NavigationService.NavigateAsync("/MainPage/NavigationPage/ModemSettingsPage");
    //        if (!result.Success)
    //        {
    //            await NavigationService.NavigateAsync("/ErrorPage", new NavigationParameters { { "exception", result.Exception } });
    //        }
    //    }
    //}
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\MainPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using ModemConfigurator.Services;
using MvvmHelpers;
using Prism.Commands;
using Prism.Logging;
using Prism.Navigation;
using Prism.Services;
using tik4net.Objects;
using tik4net.Objects.System;
using System.Text.RegularExpressions;
using Humanizer;

namespace ModemConfigurator.ViewModels
{
    public class MainPageViewModel : ViewModelBase
    {
        public MainPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService) 
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Menu";
            NavigateCommand = new DelegateCommand<string>(OnNavigateCommandExecuted);
            MenuItems = new ObservableRangeCollection<Grouping<string, MasterMenuItem>>();
            MenuItems.Add(new Grouping<string, MasterMenuItem>("App Settings", new MasterMenuItem[] { new MasterMenuItem
                {
                    Group = "App Settings",
                    FriendlyName = "Modem Connection Settings",
                    Uri = "NavigationPage/ModemSettingsPage",
                    TypeName = "AppSettings"
                }}));

            var types = typeof(SystemResource).Assembly.ExportedTypes.Where(t => t.GetCustomAttributes().Any(a => a is TikEntityAttribute));
            List<MasterMenuItem> menuItems = new List<MasterMenuItem>();
            foreach(var type in types)
            {
                menuItems.Add(new MasterMenuItem
                {
                    Group = Regex.Replace(type.Namespace, @"tik4net\.Objects\.", ""),
                    FriendlyName = type.Name.Humanize(LetterCasing.Title),
                    Uri = $"NavigationPage/{type.Name}Page",
                    TypeName = type.Name
                });
            }

            var groups = from item in menuItems
                         orderby item.Group, item.FriendlyName
                         group item by item.Group into itemGroup
                         select new Grouping<string, MasterMenuItem>(itemGroup.Key, itemGroup);
            MenuItems.AddRange(groups);
        }

        public ObservableRangeCollection<Grouping<string, MasterMenuItem>> MenuItems { get; set; }

        //public MainPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, IModemSettings modemSettings) 
        //    : base(navigationService, pageDialogService, modemSettings)
        //{
        //}

        public DelegateCommand<string> NavigateCommand { get; }

        private async void OnNavigateCommandExecuted(string path)
        {
            var result = await NavigationService.NavigateAsync(path);
            if(!result.Success)
            {
                Console.WriteLine(result.Exception);
                await _pageDialogService.DisplayAlertAsync(result.Exception.GetType().Name, result.Exception.Message, "Ok");
            }
        }
    }

    public class MasterMenuItem
    {
        public string Group { get; set; }

        public string FriendlyName { get; set; }

        public string Uri { get; set; }

        public string TypeName { get; set; }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\ModemSettingsPageViewModel.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Prism.Commands;
using Prism.Navigation;
using Prism.Logging;
using Prism.Services;
using ModemConfigurator.Services;
using tik4net.Objects.System;
using tik4net.Objects;
using System.ComponentModel;

namespace ModemConfigurator.ViewModels
{
    public class ModemSettingsPageViewModel : ViewModelBase
    {
        public ModemSettingsPageViewModel(INavigationService navigationService, IPageDialogService pageDialogService, IModemSettings modemSettings, Shiny.Net.IConnectivity connectivity, IDeviceService deviceService) 
            : base(navigationService, pageDialogService, modemSettings, connectivity, deviceService)
        {
            Title = "Modem Settings";
            if (ModemSettings is INotifyPropertyChanged inpc)
            {
                inpc.PropertyChanged += OnModemSettingsPropertyChanged;
            }
        }

        public IModemSettings ModemSettings => _modemSettings;

        private void OnModemSettingsPropertyChanged(object sender, PropertyChangedEventArgs e)
        {
            try
            {
                CheckConnection();
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine(ex);
            }
        }

        public override void Destroy()
        {
            if(ModemSettings is INotifyPropertyChanged inpc)
            {
                inpc.PropertyChanged -= OnModemSettingsPropertyChanged;
            }
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\ViewModels\ViewModelBase.cs
﻿using Prism.Commands;
using Prism.Mvvm;
using Prism.Navigation;
using System;
using System.Collections.Generic;
using System.Text;
using ModemConfigurator.Services;
using tik4net;
using Prism.Services;
using Xamarin.Forms;
using Prism.AppModel;
using System.Linq;
using System.Net;
using System.Net.NetworkInformation;
using Shiny.Net;
using System.Reactive;
using System.Reactive.Linq;
using System.Reactive.Disposables;
using Shiny;

namespace ModemConfigurator.ViewModels
{
    public class ViewModelBase : BindableBase, INavigationAware, IDestructible, IPageLifecycleAware
    {
        protected CompositeDisposable DestroyWith { get; } = new CompositeDisposable();

        protected INavigationService NavigationService { get; }

        protected IModemSettings _modemSettings { get; }

        protected IPageDialogService _pageDialogService { get; }

        protected IConnectivity _connectivity { get; }

        public ViewModelBase(INavigationService navigationService, IPageDialogService pageDialogService, IModemSettings modemSettings, IConnectivity connectivity, IDeviceService deviceService)
        {
            NavigationService = navigationService;
            _modemSettings = modemSettings;
            _pageDialogService = pageDialogService;
            _connectivity = connectivity;
            _connectivity.WhenInternetStatusChanged()
                .Subscribe(x => deviceService.BeginInvokeOnMainThread(CheckConnection))
                .DisposedBy(DestroyWith);
        }

        private string _title;
        public string Title
        {
            get { return _title; }
            set { SetProperty(ref _title, value); }
        }

        private bool _isConnected;
        public bool IsConnected
        {
            get => _isConnected;
            set => SetProperty(ref _isConnected, value, () => IsNotConnected = !value);
        }

        private bool _isNotConnected = true;
        public bool IsNotConnected
        {
            get => _isNotConnected;
            set => SetProperty(ref _isNotConnected, value, () => IsConnected = !value);
        }

        protected ITikConnection CreateConnection()
        {
            var connection = ConnectionFactory.CreateConnection(TikConnectionType.Api);
            connection.Open(_modemSettings.Host, _modemSettings.User, _modemSettings.Password);
            return connection;
        }

        public virtual void OnNavigatedFrom(INavigationParameters parameters)
        {

        }

        public virtual void OnNavigatedTo(INavigationParameters parameters)
        {
        }

        public virtual void OnNavigatingTo(INavigationParameters parameters)
        {

        }

        public virtual void Destroy()
        {
            DestroyWith.Dispose();
        }

        public void OnAppearing()
        {
            CheckConnection();
        }

        public void OnDisappearing()
        {
        }

        protected void CheckConnection()
        {
            try
            {
                if(_connectivity.Access == NetworkAccess.Ethernet &&
                    !string.IsNullOrWhiteSpace(_modemSettings.Host) &&
                    PingHost(_modemSettings.Host))
                {
                    using (var connection = CreateConnection())
                    {
                        IsConnected = connection.IsOpened;
                    }
                }
                else
                {
                    IsConnected = false;
                }
            }
            catch
            {
                IsConnected = false;
            }
        }

        private static bool PingHost(string nameOrAddress)
        {
            bool pingable = false;
            Ping pinger = null;

            try
            {
                pinger = new Ping();
                PingReply reply = pinger.Send(nameOrAddress);
                pingable = reply.Status == IPStatus.Success;
            }
            catch (PingException ex)
            {
                Console.WriteLine(ex);
                // Discard PingExceptions and return false;
            }
            finally
            {
                if (pinger != null)
                {
                    pinger.Dispose();
                }
            }

            return pingable;
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Views\ErrorPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms" 
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ErrorPage">
    <ScrollView>
        <StackLayout>
            <Label Text="Error"
                   Style="{DynamicResource TitleStyle}" />
            <Label Text="{Binding ErrorText}" />
        </StackLayout>
    </ScrollView>
</ContentPage>

File: /ModemConfigurator\src\ModemConfigurator\Views\ErrorPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ErrorPage : ContentPage
    {
        public ErrorPage()
        {
            InitializeComponent();
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Views\LoadingPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms" 
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             Title="{Binding Title}"
             BackgroundColor="{StaticResource PrimaryDark}"
             x:Class="ModemConfigurator.Views.LoadingPage">
     <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="2*" />
            <RowDefinition Height="1*" />
        </Grid.RowDefinitions>
        <Image Source="Modem"
               HorizontalOptions="Center"
               VerticalOptions="End"
               WidthRequest="200"
               HeightRequest="200"
               Aspect="AspectFit" />
        <StackLayout Grid.Row="1"
                     HorizontalOptions="Center"
                     Spacing="20">
            <Label Text="Loading..."
                   TextColor="White" />
            <ActivityIndicator IsRunning="true"
                               Color="White"
                               Scale="1.5" />
        </StackLayout>
    </Grid>
</ContentPage>

File: /ModemConfigurator\src\ModemConfigurator\Views\LoadingPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class LoadingPage : ContentPage
    {
        public LoadingPage()
        {
            InitializeComponent();
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Views\MainPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<MasterDetailPage xmlns="http://xamarin.com/schemas/2014/forms"
                  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                  xmlns:prism="http://prismlibrary.com"
                  xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
                  ios:NavigationPage.PrefersLargeTitles="true"
                  ios:Page.UseSafeArea="true"
                  Title="Main Page"
                  x:Name="page"
                  x:Class="ModemConfigurator.Views.MainPage">
    <MasterDetailPage.Master>
        <ContentPage Title="Menu"
                     IconImageSource="hamburger">
            <StackLayout>
                <StackLayout MinimumHeightRequest="80"
                             BackgroundColor="{StaticResource PrimaryDark}"
                             Orientation="Horizontal"
                             Padding="20,20,20,0">
                    <Image Source="Modem"
                           HeightRequest="30"
                           WidthRequest="30"/>
                    <Label Text="Configurator"
                           LineBreakMode="WordWrap"
                           FontSize="Large"
                           VerticalOptions="Center"
                           Margin="20"
                           TextColor="WhiteSmoke"/>
                </StackLayout>
                <!--<Frame BackgroundColor="{StaticResource PrimaryDark}"
                       HeightRequest="60">
                </Frame>-->
                <ScrollView>
                  <StackLayout BindableLayout.ItemsSource="{Binding MenuItems}">
                    <BindableLayout.ItemTemplate>
                      <DataTemplate>
                        <Grid>
                          <Grid.RowDefinitions>
                            <RowDefinition Height="Auto" />
                            <RowDefinition Height="*" />
                          </Grid.RowDefinitions>
                          <Label Text="{Binding Key}"
                                 Margin="20,5"
                                 FontAttributes="Bold"
                                 FontSize="Subtitle"/>
                          <StackLayout BindableLayout.ItemsSource="{Binding .}"
                                       Grid.Row="1">
                            <BindableLayout.ItemTemplate>
                              <DataTemplate>
                                <Label AutomationId="{Binding TypeName}"
                                       Text="{Binding FriendlyName}"
                                       Margin="25,0"
                                       TextColor="DodgerBlue">
                                  <Label.GestureRecognizers>
                                    <TapGestureRecognizer Command="{Binding BindingContext.NavigateCommand, Source={x:Reference page}}"
                                                          CommandParameter="{Binding Uri}" />
                                  </Label.GestureRecognizers>
                                </Label>
                              </DataTemplate>
                            </BindableLayout.ItemTemplate>
                          </StackLayout>
                        </Grid>
                      </DataTemplate>
                    </BindableLayout.ItemTemplate>
                  </StackLayout>
                </ScrollView>
                <!--<ListView ItemsSource="{Binding MenuItems}"
                          IsGroupingEnabled="true"
                          HasUnevenRows="true">
                    <ListView.Behaviors>
                        <prism:EventToCommandBehavior EventName="ItemTapped"
                                                          EventArgsParameterPath="Item.Uri"
                                                          Command="{Binding NavigateCommand}" />
                    </ListView.Behaviors>
                    <ListView.GroupHeaderTemplate>
                        <DataTemplate>
                            <TextCell Text="{Binding Key}" />
                        </DataTemplate>
                    </ListView.GroupHeaderTemplate>
                    <ListView.ItemTemplate>
                        <DataTemplate>
                            <TextCell Text="{Binding FriendlyName}"
                                      TextColor="DodgerBlue"
                                      />
                        </DataTemplate>
                    </ListView.ItemTemplate>
                </ListView>-->
            </StackLayout>
        </ContentPage>
    </MasterDetailPage.Master>
</MasterDetailPage>


File: /ModemConfigurator\src\ModemConfigurator\Views\MainPage.xaml.cs
﻿using Prism.Navigation;
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class MainPage : MasterDetailPage, IMasterDetailPageOptions
    {
        public MainPage()
        {
            InitializeComponent();
        }

        public bool IsPresentedAfterNavigation
        {
            get { return Device.Idiom != TargetIdiom.Phone; }
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator\Views\ModemSettingsPage.xaml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:prism="http://prismlibrary.com"
             prism:ViewModelLocator.AutowireViewModel="true"
             xmlns:ios="clr-namespace:Xamarin.Forms.PlatformConfiguration.iOSSpecific;assembly=Xamarin.Forms.Core"
             ios:NavigationPage.PrefersLargeTitles="true"
             ios:Page.UseSafeArea="true"
             Title="{Binding Title}"
             x:Class="ModemConfigurator.Views.ModemSettingsPage">
  <Grid RowSpacing="0">
    <Grid.RowDefinitions>
      <RowDefinition Height="*" />
      <RowDefinition Height="Auto" />
      <RowDefinition Height="Auto" />
    </Grid.RowDefinitions>
    <StackLayout Padding="20">
      <Label Text="Host" />
      <Frame HasShadow="True"
             Padding="0">
        <Entry Text="{Binding ModemSettings.Host}" />
      </Frame>
      <Label Text="User" />
      <Frame HasShadow="True"
             Padding="0">
        <Entry Text="{Binding ModemSettings.User}" />
      </Frame>
      <Label Text="Password" />
      <Frame HasShadow="True"
             Padding="0">
        <Entry Text="{Binding ModemSettings.Password}"
               IsPassword="true" />
      </Frame>
    </StackLayout>
    <Label Text="    Connected"
            BackgroundColor="Green"
            TextColor="WhiteSmoke"
            Grid.Row="1"
            IsVisible="{Binding IsConnected}"/>
    <Label Text="    Not Connected"
            BackgroundColor="Red"
            TextColor="WhiteSmoke"
            Grid.Row="2"
            IsVisible="{Binding IsNotConnected}" />
  </Grid>
</ContentPage>

File: /ModemConfigurator\src\ModemConfigurator\Views\ModemSettingsPage.xaml.cs
using Xamarin.Forms;

namespace ModemConfigurator.Views
{
    public partial class ModemSettingsPage : ContentPage
    {
        public ModemSettingsPage()
        {
            InitializeComponent();
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator.iOS\AppDelegate.cs
﻿using Foundation;
using Prism;
using Prism.Ioc;
using UIKit;

namespace ModemConfigurator.iOS
{
    // The UIApplicationDelegate for the application. This class is responsible for launching the
    // User Interface of the application, as well as listening (and optionally responding) to
    // application events from iOS.
    [Register("AppDelegate")]
    public partial class AppDelegate : global::Xamarin.Forms.Platform.iOS.FormsApplicationDelegate
    {
        //
        // This method is invoked when the application has loaded and is ready to run. In this
        // method you should instantiate the window, load the UI into it and then make the window
        // visible.
        //
        // You have 17 seconds to return from this method, or iOS will terminate your application.
        //
        public override bool FinishedLaunching(UIApplication uiApplication, NSDictionary options)
        {
            Prism.DryIoc.PrismContainerExtension.Create();
            Shiny.iOSShinyHost.Init(new ModemStartup());
            global::Xamarin.Forms.Forms.Init();
            Microsoft.AppCenter.Distribute.Distribute.DontCheckForUpdatesInDebug();

            LoadApplication(Xamarin.Forms.Application.Current ?? new App());

            return base.FinishedLaunching(uiApplication, options);
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator.iOS\Assets.xcassets\AppIcon.appiconset\Contents.json
{
    "images":[
        {
            "idiom":"iphone",
            "size":"20x20",
            "scale":"2x",
            "filename":"Icon-App-20x20@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"20x20",
            "scale":"3x",
            "filename":"Icon-App-20x20@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"1x",
            "filename":"Icon-App-29x29@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"2x",
            "filename":"Icon-App-29x29@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"29x29",
            "scale":"3x",
            "filename":"Icon-App-29x29@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"40x40",
            "scale":"1x",
            "filename":"Icon-App-40x40@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"40x40",
            "scale":"2x",
            "filename":"Icon-App-40x40@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"40x40",
            "scale":"3x",
            "filename":"Icon-App-40x40@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"57x57",
            "scale":"1x",
            "filename":"Icon-App-57x57@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"57x57",
            "scale":"2x",
            "filename":"Icon-App-57x57@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"60x60",
            "scale":"1x",
            "filename":"Icon-App-60x60@1x.png"
        },
        {
            "idiom":"iphone",
            "size":"60x60",
            "scale":"2x",
            "filename":"Icon-App-60x60@2x.png"
        },
        {
            "idiom":"iphone",
            "size":"60x60",
            "scale":"3x",
            "filename":"Icon-App-60x60@3x.png"
        },
        {
            "idiom":"iphone",
            "size":"76x76",
            "scale":"1x",
            "filename":"Icon-App-76x76@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"20x20",
            "scale":"1x",
            "filename":"Icon-App-20x20@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"20x20",
            "scale":"2x",
            "filename":"Icon-App-20x20@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"29x29",
            "scale":"1x",
            "filename":"Icon-App-29x29@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"29x29",
            "scale":"2x",
            "filename":"Icon-App-29x29@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"40x40",
            "scale":"1x",
            "filename":"Icon-App-40x40@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"40x40",
            "scale":"2x",
            "filename":"Icon-App-40x40@2x.png"
        },
        {
          "size" : "50x50",
          "idiom" : "ipad",
          "filename" : "Icon-Small-50x50@1x.png",
          "scale" : "1x"
        },
        {
          "size" : "50x50",
          "idiom" : "ipad",
          "filename" : "Icon-Small-50x50@2x.png",
          "scale" : "2x"
        },
        {
            "idiom":"ipad",
            "size":"72x72",
            "scale":"1x",
            "filename":"Icon-App-72x72@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"72x72",
            "scale":"2x",
            "filename":"Icon-App-72x72@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"76x76",
            "scale":"1x",
            "filename":"Icon-App-76x76@1x.png"
        },
        {
            "idiom":"ipad",
            "size":"76x76",
            "scale":"2x",
            "filename":"Icon-App-76x76@2x.png"
        },
        {
            "idiom":"ipad",
            "size":"76x76",
            "scale":"3x",
            "filename":"Icon-App-76x76@3x.png"
        },
        {
            "idiom":"ipad",
            "size":"83.5x83.5",
            "scale":"2x",
            "filename":"Icon-App-83.5x83.5@2x.png"
        },
        {
          "size" : "1024x1024",
          "idiom" : "ios-marketing",
          "filename" : "ItunesArtwork@2x.png",
          "scale" : "1x"
        }
    ],
    "info":{
        "version":1,
        "author":"makeappicon"
    }
}


File: /ModemConfigurator\src\ModemConfigurator.iOS\Assets.xcassets\Contents.json
{
  "info": {
    "version": 1,
    "author": "xcode"
  }
}

File: /ModemConfigurator\src\ModemConfigurator.iOS\Entitlements.plist
﻿<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
</dict>
</plist>



File: /ModemConfigurator\src\ModemConfigurator.iOS\Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>UIDeviceFamily</key>
	<array>
		<integer>1</integer>
		<integer>2</integer>
	</array>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>MinimumOSVersion</key>
	<string>13.0</string>
	<key>CFBundleDisplayName</key>
	<string>ModemConfigurator</string>
	<key>CFBundleIdentifier</key>
	<string>com.avantipoint.modemconfigurator</string>
	<key>CFBundleVersion</key>
	<string>1.0</string>
	<key>UILaunchStoryboardName</key>
	<string>LaunchScreen</string>
	<key>CFBundleName</key>
	<string>ModemConfigurator</string>
	<key>XSAppIconAssets</key>
	<string>Assets.xcassets/AppIcon.appiconset</string>
	<key>CFBundleShortVersionString</key>
	<string>1</string>
	<key>UIBackgroundModes</key>
	<array>
		<string>fetch</string>
		<string>processing</string>
	</array>
</dict>
</plist>


File: /ModemConfigurator\src\ModemConfigurator.iOS\Main.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;

using Foundation;
using UIKit;

namespace ModemConfigurator.iOS
{
    public class Application
    {
        // This is the main entry point of the application.
        static void Main(string[] args)
        {
            // if you want to use a different Application Delegate class from "AppDelegate"
            // you can specify it here.
            UIApplication.Main(args, null, "AppDelegate");
        }
    }
}


File: /ModemConfigurator\src\ModemConfigurator.iOS\ModemConfigurator.iOS.csproj
﻿<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup>
    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
    <Platform Condition=" '$(Platform)' == '' ">iPhoneSimulator</Platform>
    <ProductVersion>8.0.30703</ProductVersion>
    <SchemaVersion>2.0</SchemaVersion>
    <ProjectGuid>{0F462199-2685-4E47-83AD-201D939E9BDF}</ProjectGuid>
    <ProjectTypeGuids>{FEACFBD2-3405-455C-9665-78FE426C6842};{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}</ProjectTypeGuids>
    <OutputType>Exe</OutputType>
    <RootNamespace>ModemConfigurator.iOS</RootNamespace>
    <IPhoneResourcePrefix>Resources</IPhoneResourcePrefix>
    <AssemblyName>ModemConfigurator.iOS</AssemblyName>
    <MtouchEnableSGenConc>true</MtouchEnableSGenConc>
    <MtouchHttpClientHandler>NSUrlSessionHandler</MtouchHttpClientHandler>
    <CodesignEntitlements>Entitlements.plist</CodesignEntitlements>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|iPhoneSimulator' ">
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\iPhoneSimulator\Debug</OutputPath>
    <DefineConstants>DEBUG</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <ConsolePause>false</ConsolePause>
    <MtouchArch>x86_64</MtouchArch>
    <MtouchLink>None</MtouchLink>
    <MtouchDebug>true</MtouchDebug>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|iPhoneSimulator' ">
    <DebugType>none</DebugType>
    <Optimize>true</Optimize>
    <OutputPath>bin\iPhoneSimulator\Release</OutputPath>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <MtouchLink>None</MtouchLink>
    <MtouchArch>i386, x86_64</MtouchArch>
    <ConsolePause>false</ConsolePause>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|iPhone' ">
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\iPhone\Debug</OutputPath>
    <DefineConstants>DEBUG</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <ConsolePause>false</ConsolePause>
    <MtouchArch>ARM64</MtouchArch>
    <CodesignKey>iPhone Developer</CodesignKey>
    <MtouchDebug>true</MtouchDebug>
    <CodesignEntitlements>Entitlements.plist</CodesignEntitlements>
    <MtouchFastDev>true</MtouchFastDev>
    <MtouchInterpreter>-all</MtouchInterpreter>
    <MtouchLink>None</MtouchLink>
    <MtouchNoSymbolStrip>true</MtouchNoSymbolStrip>
    <MtouchProfiling>true</MtouchProfiling>
    <BuildIpa>true</BuildIpa>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|iPhone' ">
    <DebugType>none</DebugType>
    <Optimize>true</Optimize>
    <OutputPath>bin\iPhone\Release</OutputPath>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <MtouchArch>x86_64</MtouchArch>
    <ConsolePause>false</ConsolePause>
    <CodesignKey>iPhone Distribution</CodesignKey>
    <MtouchUseLlvm>true</MtouchUseLlvm>
    <MtouchNoSymbolStrip>true</MtouchNoSymbolStrip>
    <MtouchEnableSGenConc>true</MtouchEnableSGenConc>
    <DeviceSpecificBuild>false</DeviceSpecificBuild>
    <OptimizePNGs>true</OptimizePNGs>
    <BuildIpa>true</BuildIpa>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Ad-Hoc|iPhone' ">
    <DebugType>none</DebugType>
    <Optimize>True</Optimize>
    <OutputPath>bin\iPhone\Ad-Hoc</OutputPath>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <ConsolePause>False</ConsolePause>
    <MtouchArch>ARM64</MtouchArch>
    <BuildIpa>True</BuildIpa>
    <CodesignProvision>Automatic:AdHoc</CodesignProvision>
    <CodesignKey>iPhone Distribution</CodesignKey>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'AppStore|iPhone' ">
    <DebugType>none</DebugType>
    <Optimize>True</Optimize>
    <OutputPath>bin\iPhone\AppStore</OutputPath>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
    <ConsolePause>False</ConsolePause>
    <MtouchArch>ARM64</MtouchArch>
    <CodesignProvision>Automatic:AppStore</CodesignProvision>
    <CodesignKey>iPhone Distribution</CodesignKey>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(RunConfiguration)' == 'Default' ">
    <AppExtensionDebugBundleId />
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="Main.cs" />
    <Compile Include="AppDelegate.cs" />
    <None Include="Entitlements.plist" />
    <None Include="Info.plist" />
    <Compile Include="Properties\AssemblyInfo.cs" />
  </ItemGroup>
  <ItemGroup>
    <ImageAsset Include="Assets.xcassets\Contents.json">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Contents.json">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-20x20@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-20x20@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-20x20@3x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-29x29@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-29x29@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-29x29@3x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-40x40@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-40x40@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-40x40@3x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-57x57@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-57x57@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-60x60@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-60x60@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-60x60@3x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-72x72@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-72x72@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-76x76@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-76x76@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-76x76@3x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-App-83.5x83.5@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-Small-50x50@1x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\Icon-Small-50x50@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Assets.xcassets\AppIcon.appiconset\ItunesArtwork@2x.png">
      <Visible>false</Visible>
    </ImageAsset>
    <ImageAsset Include="Resources\Media.xcassets\Contents.json" Visible="false" />
    <ImageAsset Include="Resources\Media.xcassets\AvantiPointLogo.imageset\Contents.json" Visible="false" />
    <ImageAsset Include="Resources\Media.xcassets\AvantiPointLogo.imageset\avantipoint@1x.png" Visible="false" />
    <ImageAsset Include="Resources\Media.xcassets\AvantiPointLogo.imageset\avantipoint@2x.png" Visible="false" />
    <ImageAsset Include="Resources\Media.xcassets\AvantiPointLogo.imageset\avantipoint@3x.png" Visible="false" />
  </ItemGroup>
  <ItemGroup>
    <InterfaceDefinition Include="Resources\LaunchScreen.storyboard" />
    <BundleResource Include="Resources\add.png" />
    <BundleResource Include="Resources\add%402x.png" />
    <BundleResource Include="Resources\hamburger.png" />
    <BundleResource Include="Resources\hamburger%402x.png" />
    <BundleResource Include="Resources\Modem.png" />
  </ItemGroup>
  <ItemGroup>
    <Reference Include="System" />
    <Reference Include="System.Xml" />
    <Reference Include="System.Core" />
    <Reference Include="Xamarin.iOS" />
  </ItemGroup>
  <ItemGroup>
    <PackageReference Include="tik4net">
      <Version>3.5.0</Version>
    </PackageReference>
    <PackageReference Include="Xamarin.Forms">
      <Version>4.4.0.991640</Version>
    </PackageReference>
    <PackageReference Include="Prism.Forms.Extended">
      <Version>7.2.0.898</Version>
    </PackageReference>
    <PackageReference Include="Prism.DryIoc.Extensions">
      <Version>7.2.0.898</Version>
    </PackageReference>
    <PackageReference Include="Humanizer.Core">
      <Version>2.7.9</Version>
    </PackageReference>
    <PackageReference Include="Refractored.MvvmHelpers">
      <Version>1.6.1-beta</Version>
    </PackageReference>
    <PackageReference Include="Microsoft.AppCenter.Crashes">
      <Version>3.0.0</Version>
    </PackageReference>
    <PackageReference Include="Microsoft.AppCenter.Analytics">
      <Version>3.0.0</Version>
    </PackageReference>
  </ItemGroup>
  <ItemGroup>
    <ProjectReference Include="..\ModemConfigurator\ModemConfigurator.csproj">
      <Project>{EC2573EC-6583-420A-AA16-F1A25B6D2B70}</Project>
      <Name>ModemConfigurator</Name>
    </ProjectReference>
  </ItemGroup>
  <Import Project="$(MSBuildExtensionsPath)\Xamarin\iOS\Xamarin.iOS.CSharp.targets" />
</Project>

File: /ModemConfigurator\src\ModemConfigurator.iOS\Properties\AssemblyInfo.cs
﻿using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("ModemConfigurator.iOS")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("")]
[assembly: AssemblyProduct("ModemConfigurator.iOS")]
[assembly: AssemblyCopyright("Copyright ©  2014")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]

// Setting ComVisible to false makes the types in this assembly not visible 
// to COM components.  If you need to access a type in this assembly from 
// COM, set the ComVisible attribute to true on that type.
[assembly: ComVisible(false)]

// The following GUID is for the ID of the typelib if this project is exposed to COM
[assembly: Guid("72bdc44f-c588-44f3-b6df-9aace7daafdd")]

// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers 
// by using the '*' as shown below:
// [assembly: AssemblyVersion("1.0.*")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]


File: /ModemConfigurator\src\ModemConfigurator.iOS\Resources\LaunchScreen.storyboard
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="15705" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" useTraitCollections="YES" colorMatched="YES" initialViewController="X5k-f2-b5h">
    <device id="retina6_1" orientation="portrait" appearance="light"/>
    <dependencies>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="15706"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="gAE-YM-kbH">
            <objects>
                <viewController id="X5k-f2-b5h" sceneMemberID="viewController">
                    <layoutGuides>
                        <viewControllerLayoutGuide type="top" id="Y8P-hJ-Z43"/>
                        <viewControllerLayoutGuide type="bottom" id="9ZL-r4-8FZ"/>
                    </layoutGuides>
                    <view key="view" contentMode="scaleToFill" id="yd7-JS-zBw">
                        <rect key="frame" x="0.0" y="0.0" width="414" height="896"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <subviews>
                            <imageView userInteractionEnabled="NO" contentMode="scaleAspectFill" misplaced="YES" image="AvantiPointLogo" translatesAutoresizingMaskIntoConstraints="NO" id="23">
                                <rect key="frame" x="198" y="482" width="60" height="60"/>
                                <rect key="contentStretch" x="0.0" y="0.0" width="0.0" height="0.0"/>
                                <edgeInsets key="layoutMargins" top="8" left="20" bottom="8" right="20"/>
                            </imageView>
                        </subviews>
                        <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                        <constraints>
                            <constraint firstItem="23" firstAttribute="centerY" secondItem="yd7-JS-zBw" secondAttribute="centerY" priority="1" id="39"/>
                            <constraint firstItem="23" firstAttribute="centerX" secondItem="yd7-JS-zBw" secondAttribute="centerX" priority="1" id="41"/>
                        </constraints>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="XAI-xm-WK6" userLabel="First Responder" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="349" y="339"/>
        </scene>
    </scenes>
    <resources>
        <image name="AvantiPointLogo" width="300" height="98"/>
    </resources>
</document>

File: /ModemConfigurator\src\ModemConfigurator.iOS\Resources\Media.xcassets\AvantiPointLogo.imageset\Contents.json
{
  "images": [
    {
      "idiom": "universal"
    },
    {
      "filename": "avantipoint@1x.png",
      "scale": "1x",
      "idiom": "universal"
    },
    {
      "filename": "avantipoint@2x.png",
      "scale": "2x",
      "idiom": "universal"
    },
    {
      "filename": "avantipoint@3x.png",
      "scale": "3x",
      "idiom": "universal"
    },
    {
      "idiom": "iphone"
    },
    {
      "scale": "1x",
      "idiom": "iphone"
    },
    {
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "subtype": "retina4",
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "scale": "3x",
      "idiom": "iphone"
    },
    {
      "idiom": "ipad"
    },
    {
      "scale": "1x",
      "idiom": "ipad"
    },
    {
      "scale": "2x",
      "idiom": "ipad"
    },
    {
      "idiom": "watch"
    },
    {
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{130,145}",
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{146,165}",
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "idiom": "mac"
    },
    {
      "scale": "1x",
      "idiom": "mac"
    },
    {
      "scale": "2x",
      "idiom": "mac"
    },
    {
      "idiom": "car"
    },
    {
      "scale": "2x",
      "idiom": "car"
    },
    {
      "scale": "3x",
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "1x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "3x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "1x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "subtype": "retina4",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "3x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "1x",
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "watch"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{130,145}",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{146,165}",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "1x",
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "2x",
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "dark"
        }
      ],
      "scale": "3x",
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "1x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "3x",
      "idiom": "universal"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "1x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "subtype": "retina4",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "3x",
      "idiom": "iphone"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "1x",
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "ipad"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "watch"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{130,145}",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "screenWidth": "{146,165}",
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "watch"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "1x",
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "mac"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "2x",
      "idiom": "car"
    },
    {
      "appearances": [
        {
          "appearance": "luminosity",
          "value": "light"
        }
      ],
      "scale": "3x",
      "idiom": "car"
    }
  ],
  "info": {
    "version": 1,
    "author": "xcode"
  }
}

File: /ModemConfigurator\src\ModemConfigurator.iOS\Resources\Media.xcassets\Contents.json
﻿{
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}

File: /ReadMe.md
# MikroTik Demo

This demo app is built around the MikroTik .NET Library Tik4Net. This is broken up into two parts:

- Entity Builder
- ModemConfigurator

The Entity Builder is a .NET Core app that will dynamically build Views/ViewModels as well an extension for Prism's IContainerRegistry to register what has been generated. If a newer version of Tik4Net is available just update the NuGet package and re-run the Entity Builder, the ModemConfigurator project will automatically update to use any newly generated entities.

The ModemConfigurator is fairly simple Xamarin.Forms app using Prism. For [@PrismLib](https://twitter.com/PrismLib) fans you'll notice an excess of 100 Views/ViewModels which get registered while still providing an incredibly short hit to the total initialization time.

## Build Note

The ModemConfigurator relies on the [Mobile.BuildTools](https://github.com/dansiegel/Mobile.BuildTools) to inject the App Center app secret. This is intentionally left out of Source Control. To build the app you will need to add a file to the ModemConfigurator project in the same directory as the `App.xaml` named `secrets.json` like the following sample json.

```json
{
  "AppCenterSecret": "{Your App Center Secret}"
}
```

