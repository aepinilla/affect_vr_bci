using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;

public class Login : MonoBehaviour
{
    public InputField UsernameField;
    public InputField PasswordField;
    public Button LoginButton;
    public Button StartButton;
    public Text ResponseText;
    private string UserdataPath = @"./Data/userdata.json";
    private List<Userdata> UserdataList;
    

    // Start is called before the first frame update
    void Start()
    {
        StartButton.gameObject.SetActive(false);

        if (!File.Exists(UserdataPath))
        {
            File.WriteAllText(UserdataPath, JsonConvert.SerializeObject(new List<Userdata>()));
        }

        var jsontext = File.ReadAllText(UserdataPath);
        UserdataList = JsonConvert.DeserializeObject<List<Userdata>>(jsontext);
    }

    private void InfoText(string text, Color color)
    {
        ResponseText.text = text;
        ResponseText.color = color;
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

    private Userdata RegisterUser(string username, string password)
    {
        Userdata user = new Userdata
        {
            Username = UsernameField.text
        };

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
            user.PrivateKey = createDidResponse.Key.Private;
            user.PublicKey = createDidResponse.Key.Public;
            
            UserdataList.Add(user);
            File.WriteAllText(UserdataPath, JsonConvert.SerializeObject(UserdataList));
        }
        catch (Exception e)
        {
            InfoText("ERROR: " + rawResult, Color.red);
        }

        return user;
    }

    public void SubmitLogin()
    {
        StartButton.gameObject.SetActive(false);
            
        if (string.IsNullOrEmpty(UsernameField.text) || string.IsNullOrEmpty(PasswordField.text))
        {
            InfoText("Please enter Username and Password", Color.red);
            return;
        }

        InfoText("Authentification...", Color.white);

        Userdata user = UserdataList.FirstOrDefault(x => x.Username == UsernameField.text);

        if (user == null)
        {
            user = RegisterUser(UsernameField.text, PasswordField.text);
        }


        InfoText("Authentification complete", Color.green);
        
        LoginButton.gameObject.SetActive(false);
        StartButton.gameObject.SetActive(true);
    }
}
