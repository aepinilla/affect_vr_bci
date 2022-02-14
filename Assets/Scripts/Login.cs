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
    private TangleConnection tangleConnection;

    public InputField UsernameField;
    public InputField PasswordField;
    public Button LoginButton;
    public Button StartButton;
    public Text ResponseText;
    private bool LoginStarted;
    private bool LoginSuccess;

    // Start is called before the first frame update
    void Start()
    {
        StartButton.gameObject.SetActive(false);

        GameObject tangleConnectionObject = GameObject.Find("TangleConnection");
        tangleConnection = tangleConnectionObject.GetComponent<TangleConnection>();

        if (tangleConnection == null)
        {
            throw new Exception("Login: tangleConnection is null");
        }
    }

    private void Update()
    {
        DisableLoginButton(LoginStarted);

        if (!LoginSuccess && tangleConnection.User != null)
        {
            LoginSuccess = true;
            LoginStarted = false;

            InfoText("Authentification complete", Color.green);
            
            StartButton.gameObject.SetActive(true);            
        }

        if (LoginStarted)
        {
            InfoText("Authentification" + new string('.', DateTime.Now.Second % 4), Color.white);
        }
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

    public void SubmitLogin()
    {
        if (string.IsNullOrEmpty(UsernameField.text) || string.IsNullOrEmpty(PasswordField.text))
        {
            InfoText("Please enter Username and Password", Color.red);
            return;
        }

        LoginStarted = true;
        tangleConnection.Login(UsernameField.text, PasswordField.text);
    }

    private void InfoText(string text, Color color)
    {
        ResponseText.text = text;
        ResponseText.color = color;
    }
}
