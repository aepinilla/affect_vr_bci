using Newtonsoft.Json;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using UnityEngine;

public class TangleConnection : MonoBehaviour
{
    private string UserdataPath = @"./Data/userdata.json";
    private List<Userdata> UserdataList;

    public Userdata User;

    // Start is called before the first frame update
    void Start()
    {
        if (!File.Exists(UserdataPath))
        {
            File.WriteAllText(UserdataPath, JsonConvert.SerializeObject(new List<Userdata>()));
        }

        var jsontext = File.ReadAllText(UserdataPath);
        UserdataList = JsonConvert.DeserializeObject<List<Userdata>>(jsontext);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void Login(string username, string password)
    {
        User = UserdataList.FirstOrDefault(x => x.Username == username);

        if (User == null)
        {
            Task.Run(() => RegisterUser(username, password));
        }
    }

    private Process CreateIotaAuthProcess(string args)
    {
        return new Process
        {
            StartInfo = new ProcessStartInfo
            {
                WorkingDirectory = @"./Assets/IotaAuth/src/",
                WindowStyle = ProcessWindowStyle.Hidden,
                FileName = "cmd.exe",
                Arguments = "/c node main.js " + args,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            }
        };
    }

    private void RegisterUser(string username, string password)
    {
        Process create_did = CreateIotaAuthProcess("create_did");
        create_did.Start();

        string rawResult = "";
        while (!create_did.StandardOutput.EndOfStream)
        {
            string line = create_did.StandardOutput.ReadLine();
            rawResult += line;
        }

        try
        {
            CreateDidResponse createDidResponse = JsonConvert.DeserializeObject<CreateDidResponse>(rawResult);

            Userdata user = new Userdata
            {
                Username = username,
                PrivateKey = createDidResponse.Key.Private,
                PublicKey = createDidResponse.Key.Public
            };

            UserdataList.Add(user);
            File.WriteAllText(UserdataPath, JsonConvert.SerializeObject(UserdataList));

            User = user;
        }
        catch (Exception e)
        {
            throw new Exception(e.Message);
        }
    }
}
