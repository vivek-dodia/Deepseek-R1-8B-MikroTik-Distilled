# Repository Information
Name: mikrotik-port-forwarder-gui

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
	url = https://gitlab.com/kiss.m.aron/mikrotik-port-forwarder-gui.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: App.config
================================================
﻿<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5.2" />
    </startup>
</configuration>
================================================

File: Mikrotik.cs
================================================
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Kisem.Debug;
namespace MikroTikPortForwarder
{
    public class Router
    {
        private string ip = "192.168.1.1",
                       username = "admin", 
                       password = "";
        private int port = 22;
        public string IP
        {
            get
            {
                return ip;
            }
            set
            {
                ip = value;
                Debug.Info("Router IP address set to " + ip);
            }
        }
        public int Port
        {
            get
            {
                return port;
            }
            set
            {
                port = value;
                Debug.Info("SSH port set to " + port);
            }
        }
        public string Username
        {
            get
            {
                return username;
            }
            set
            {
                username = value;
                Debug.Info("SSH username set to " + username);
            }
        }
        public string Password
        {
            get
            {
                return password;
            }
            set
            {
                password = value;
                Debug.Info("SSH password set to " + password);
            }
        }
        public Router()
        {
        }
        public Router(string IP)
        {
            ip = IP;
        }
        public Router(string IP, string Password)
        {
            ip = IP;
            password = Password;
        }
        public Router(string IP, string Username, string Password)
        {
            ip = IP;
            username = Username;
            password = Password;
        }
        public Router(string IP, int Port, string Username, string Password)
        {
            ip = IP;
            port = Port;
            username = Username;
            password = Password;
        }
    }
}
================================================

File: MikroTikPortForwarder.csproj
================================================
﻿<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="14.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />
  <PropertyGroup>
    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
    <Platform Condition=" '$(Platform)' == '' ">AnyCPU</Platform>
    <ProjectGuid>{9E5C6298-2052-4FCE-992B-D530A5D298B2}</ProjectGuid>
    <OutputType>Exe</OutputType>
    <AppDesignerFolder>Properties</AppDesignerFolder>
    <RootNamespace>MikroTikPortForwarder</RootNamespace>
    <AssemblyName>MikroTik Port Forwarder</AssemblyName>
    <TargetFrameworkVersion>v4.5.2</TargetFrameworkVersion>
    <FileAlignment>512</FileAlignment>
    <AutoGenerateBindingRedirects>true</AutoGenerateBindingRedirects>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <PlatformTarget>AnyCPU</PlatformTarget>
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\Debug\</OutputPath>
    <DefineConstants>DEBUG;TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">
    <PlatformTarget>AnyCPU</PlatformTarget>
    <DebugType>pdbonly</DebugType>
    <Optimize>true</Optimize>
    <OutputPath>bin\Release\</OutputPath>
    <DefineConstants>TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <PropertyGroup>
    <StartupObject>MikroTikPortForwarder.Program</StartupObject>
  </PropertyGroup>
  <PropertyGroup>
    <NoWin32Manifest>true</NoWin32Manifest>
  </PropertyGroup>
  <ItemGroup>
    <Reference Include="Renci.SshNet, Version=2016.0.0.0, Culture=neutral, PublicKeyToken=1cee9f8bde3db106, processorArchitecture=MSIL">
      <HintPath>..\packages\SSH.NET.2016.0.0\lib\net40\Renci.SshNet.dll</HintPath>
      <Private>True</Private>
    </Reference>
    <Reference Include="System" />
    <Reference Include="System.Core" />
    <Reference Include="System.Xml.Linq" />
    <Reference Include="System.Data.DataSetExtensions" />
    <Reference Include="Microsoft.CSharp" />
    <Reference Include="System.Data" />
    <Reference Include="System.Deployment" />
    <Reference Include="System.Drawing" />
    <Reference Include="System.Net.Http" />
    <Reference Include="System.Windows.Forms" />
    <Reference Include="System.Xml" />
  </ItemGroup>
  <ItemGroup>
    <Compile Include="Form_Main.cs">
      <SubType>Form</SubType>
    </Compile>
    <Compile Include="Form_Main.Designer.cs">
      <DependentUpon>Form_Main.cs</DependentUpon>
    </Compile>
    <Compile Include="Debug.cs" />
    <Compile Include="Language.cs" />
    <Compile Include="Mikrotik.cs" />
    <Compile Include="Form_Settings.cs">
      <SubType>Form</SubType>
    </Compile>
    <Compile Include="Form_Settings.Designer.cs">
      <DependentUpon>Form_Settings.cs</DependentUpon>
    </Compile>
    <Compile Include="Program.cs" />
    <Compile Include="Properties\AssemblyInfo.cs" />
    <Compile Include="Settings.cs" />
    <EmbeddedResource Include="Form_Main.en.resx">
      <DependentUpon>Form_Main.cs</DependentUpon>
    </EmbeddedResource>
    <EmbeddedResource Include="Form_Main.resx">
      <DependentUpon>Form_Main.cs</DependentUpon>
    </EmbeddedResource>
    <EmbeddedResource Include="Form_Settings.resx">
      <DependentUpon>Form_Settings.cs</DependentUpon>
    </EmbeddedResource>
    <EmbeddedResource Include="Properties\Resources.resx">
      <Generator>ResXFileCodeGenerator</Generator>
      <LastGenOutput>Resources.Designer.cs</LastGenOutput>
      <SubType>Designer</SubType>
    </EmbeddedResource>
    <Compile Include="Properties\Resources.Designer.cs">
      <AutoGen>True</AutoGen>
      <DependentUpon>Resources.resx</DependentUpon>
    </Compile>
    <None Include="packages.config" />
    <None Include="Properties\Settings.settings">
      <Generator>SettingsSingleFileGenerator</Generator>
      <LastGenOutput>Settings.Designer.cs</LastGenOutput>
    </None>
    <Compile Include="Properties\Settings.Designer.cs">
      <AutoGen>True</AutoGen>
      <DependentUpon>Settings.settings</DependentUpon>
      <DesignTimeSharedInput>True</DesignTimeSharedInput>
    </Compile>
  </ItemGroup>
  <ItemGroup>
    <None Include="App.config" />
  </ItemGroup>
  <Import Project="$(MSBuildToolsPath)\Microsoft.CSharp.targets" />
  <!-- To modify your build process, add your task inside one of the targets below and uncomment it. 
       Other similar extension points exist, see Microsoft.Common.targets.
  <Target Name="BeforeBuild">
  </Target>
  <Target Name="AfterBuild">
  </Target>
  -->
</Project>
================================================

File: MikroTikPortForwarder.csproj.CoreCompileInputs.cache
================================================
b6a6052a3db05535a9a04676cb9f5ded5e12fa58
================================================

File: MikroTikPortForwarder.csproj.FileListAbsolute.txt
================================================
c:\users\kisem\documents\visual studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\Renci.SshNet.dll
c:\users\kisem\documents\visual studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\Renci.SshNet.xml
c:\users\kisem\documents\visual studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.csprojResolveAssemblyReference.cache
c:\users\kisem\documents\visual studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.Properties.Resources.resources
c:\users\kisem\documents\visual studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.csproj.GenerateResource.Cache
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.Form_Main.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.Form_Settings.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\MikroTik Port Forwarder.exe.config
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\MikroTik Port Forwarder.exe
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\MikroTik Port Forwarder.pdb
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTik Port Forwarder.exe
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTik Port Forwarder.pdb
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Debug\en\MikroTik Port Forwarder.resources.dll
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\MikroTikPortForwarder.Form_Main.en.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Debug\en\MikroTik Port Forwarder.resources.dll
================================================

File: MikroTikPortForwarder.csproj.FileListAbsolute.txt
================================================
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Release\MikroTik Port Forwarder.exe.config
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Release\MikroTik Port Forwarder.exe
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Release\MikroTik Port Forwarder.pdb
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Release\Renci.SshNet.dll
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\bin\Release\Renci.SshNet.xml
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTikPortForwarder.Form_Main.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTikPortForwarder.Form_Settings.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTikPortForwarder.Properties.Resources.resources
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTikPortForwarder.csproj.GenerateResource.Cache
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTik Port Forwarder.exe
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTik Port Forwarder.pdb
C:\Users\Kisem\Documents\Visual Studio 2015\Projects\MikroTikPortForwarder\MikroTikPortForwarder\obj\Release\MikroTikPortForwarder.csprojResolveAssemblyReference.cache
================================================

File: packages.config
================================================
﻿<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="SSH.NET" version="2016.0.0" targetFramework="net452" />
</packages>
================================================

File: MikroTikPortForwarder.sln
================================================
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio 14
VisualStudioVersion = 14.0.25123.0
MinimumVisualStudioVersion = 10.0.40219.1
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "MikroTikPortForwarder", "MikroTikPortForwarder\MikroTikPortForwarder.csproj", "{9E5C6298-2052-4FCE-992B-D530A5D298B2}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{9E5C6298-2052-4FCE-992B-D530A5D298B2}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{9E5C6298-2052-4FCE-992B-D530A5D298B2}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{9E5C6298-2052-4FCE-992B-D530A5D298B2}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{9E5C6298-2052-4FCE-992B-D530A5D298B2}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
EndGlobal
================================================