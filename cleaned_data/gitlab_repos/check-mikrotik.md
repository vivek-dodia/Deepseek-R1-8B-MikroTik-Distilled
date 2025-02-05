# Repository Information
Name: check-mikrotik

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
	url = https://gitlab.com/karosveduni/check-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: CheckMikroTik.cs
================================================
﻿using Check.Enum;
using Microsoft.Extensions.Logging;
using tik4net;
using tik4net.Objects;
using tik4net.Objects.Interface;
namespace Check.Models
{
	public class Port(string name, bool running, Status status)
	{
		public const string Up = "Up";
		public const string Down = "Down";
		public string Name { get; set; } = name;
		public bool Running { get; set; } = running;
		/// <summary>
		/// True - Up, False - Down
		/// </summary>
		public Status Status { get; set; } = status;
		public static Status GetStatusFromString(string value)
		{
			return Up.Equals(value, StringComparison.OrdinalIgnoreCase) ? Status.Up : Status.Down;
		}
	}
	public class CheckMicroTik
	{
		private readonly ILogger<CheckMicroTik> logger;
		private readonly ITikConnection connection;
		private static readonly Lazy<CheckMicroTik> lazy = new(() => new CheckMicroTik());
		public static CheckMicroTik Instance { get { return lazy.Value; } }
		public readonly List<Port> Ports = [];
		public bool IsOpen => Ports.Count != 0;
		public event Action<string, bool, Status> ChangePort;
		public CheckMicroTik()
		{
			logger = MauiProgram.Services.GetRequiredService<ILogger<CheckMicroTik>>();
			connection = ConnectionFactory.CreateConnection(TikConnectionType.Api);
		}
		public bool OpenConnection(string host, string user, string password)
		{
			try
			{
				connection.Open(host, user, password);
				List<Interface> interfaces = connection.LoadAll<Interface>().ToList();
				Ports.Clear();
				Ports.AddRange(interfaces.ConvertAll(inte => new Port(inte.Name, inte.Running, Port.GetStatusFromString(inte.Comment))));
				return true;
			}
			catch (Exception ex)
			{
				logger.LogError(ex, "Open connection error");
				return false;
			}
		}
		public void CloseConnection()
		{
			if (!IsOpen)
				return;
			logger.LogInformation("Close connection");
			connection.Close();
			Ports.Clear();
		}
		public List<Interface> MonitorPortChanges()
		{
			List<Interface> interfaces = null;
			try
			{
				interfaces = connection.LoadAll<Interface>().ToList();
			}
			catch (Exception ex)
			{
				logger.LogError(ex, "Monitor port changes error");
				return [];
			}
			Ports.ForEach(port =>
			{
				Interface inte = interfaces.Find(inte => inte.Name == port.Name && Port.GetStatusFromString(inte.Comment) != port.Status)!;
				if (inte is not null)
				{
					port.Running = inte.Running;
					port.Status = port.Status == Status.Up ? Status.Down : Status.Up;
					ChangePort?.Invoke(port.Name, port.Running, port.Status);
				}
			});
			return interfaces;
		}
	}
}
================================================

File: launchSettings.json
================================================
{
  "profiles": {
    "Windows Machine": {
      "commandName": "MsixPackage",
      "nativeDebugging": false
    }
  }
}
================================================

File: AboutAssets.txt
================================================
﻿Any raw assets you want to be deployed with your application can be placed in
this directory (and child directories). Deployment of the asset to your application
is automatically handled by the following `MauiAsset` Build Action within your `.csproj`.
	<MauiAsset Include="Resources\Raw\**" LogicalName="%(RecursiveDir)%(Filename)%(Extension)" />
These files will be deployed with your package and will be accessible using Essentials:
	async Task LoadMauiAsset()
	{
		using var stream = await FileSystem.OpenAppPackageFileAsync("AboutAssets.txt");
		using var reader = new StreamReader(stream);
		var contents = reader.ReadToEnd();
	}
================================================

File: README.md
================================================
Программа позволяет проконтролировать есть ли интернет на портах Mikrotik.