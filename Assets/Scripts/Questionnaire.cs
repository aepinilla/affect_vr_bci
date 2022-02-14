using Newtonsoft.Json;
using System;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class Questionnaire : MonoBehaviour
{
    private TangleConnection tangleConnection;
    private string dataPath = @"./Data/";

    public GameObject[] questionGroupArr;
    public SelfReport[] qaArr;
    public string responses;

    public string startTime;
    public string endTS;


    void Start()
    {
        qaArr = new SelfReport[questionGroupArr.Length];

        GameObject tangleConnectionObject = GameObject.Find("TangleConnection");
        tangleConnection = tangleConnectionObject.GetComponent<TangleConnection>();

        if (tangleConnection == null)
        {
            throw new Exception("Login: tangleConnection is null");
        }
    }

    public void SubmitAnswer()
    {
        for (int i = 0; i < qaArr.Length; i++)
        {
            qaArr[i] = ReadQuestionAndAnswer(questionGroupArr[i]);
        }

        QuestionnaireResponse response = new QuestionnaireResponse
        {
            User = tangleConnection.User,
            Timestamp = DateTime.UtcNow.ToString("yyyy-MM-dd,HH.mm.ss"),
            Marker = PlayerPrefs.GetString("Marker"),
            Valence = qaArr[0].Answer,
            Arousal = qaArr[1].Answer,
            Dominance = qaArr[2].Answer
        };


        // For running in Windows
        File.WriteAllText(dataPath + response.User.Username + "_" + response.Timestamp + ".json", JsonConvert.SerializeObject(response));

        // For running in Oculus Quest
        //path = Application.persistentDataPath + " / " + timestamp + ".csv";
        //System.IO.File.WriteAllText(path, responses);
    }

    SelfReport ReadQuestionAndAnswer(GameObject QuestionGroup)
    {
        SelfReport result = new SelfReport();

        GameObject q = QuestionGroup.transform.Find("Question").gameObject;
        GameObject a = QuestionGroup.transform.Find("Answer").gameObject;

        result.Question = q.GetComponent<Text>().text;

        for (int i = 0; i < a.transform.childCount; i++)
        {
            if (a.transform.GetChild(i).GetComponent<Toggle>().isOn)
            {
                result.Answer = a.transform.GetChild(i).
                    Find("Label").GetComponent<Text>().text;
                break;
            }
        }

        return result;

    }
}


[System.Serializable]
public class SelfReport
{
    public string Question = "";
    public string Answer = "";
}