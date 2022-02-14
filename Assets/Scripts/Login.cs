using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
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
    private Userdata User;
    private bool LoginStarted;
    private bool LoginSuccess;

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

    private void DisableLoginButton(bool disable)
    {
        if (disable)
        {
            LoginButton.enabled = false;
            LoginButton.image.color = LoginButton.colors.disabledColor;
        }
        else
        {
            LoginButton.enabled = true;
            LoginButton.image.color = LoginButton.colors.normalColor;
        }
    }

    private void Update()
    {
        DisableLoginButton(LoginStarted);

        if (!LoginSuccess && User != null)
        {
            LoginSuccess = true;
            LoginStarted = false;

            InfoText("Authentification complete", Color.green);
            
            LoginButton.gameObject.SetActive(false);
            StartButton.gameObject.SetActive(true);            
        }
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

    private async Task RegisterUserAsync()
    {
        User = RegisterUser(UsernameField.text, PasswordField.text);
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
        LoginStarted = true;

        if (string.IsNullOrEmpty(UsernameField.text) || string.IsNullOrEmpty(PasswordField.text))
        {
            InfoText("Please enter Username and Password", Color.red);
            LoginStarted = false;
            return;
        }

        InfoText("Authentification...", Color.white);

        User = UserdataList.FirstOrDefault(x => x.Username == UsernameField.text);

        if (User == null)
        {
            Task.Run(RegisterUserAsync);
        }
    }
}
