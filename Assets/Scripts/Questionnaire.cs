using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Questionnaire : MonoBehaviour
{
    public GameObject[] questionGroupArr;
    public SelfReport[] qaArr;
    public string responses;
    private string path;

    public string participant;
    public string group;
    public string marker;
    public string arousal;
    public string valence;
    public string dominance;
    public string timestamp;
    public string startTime;
    public string endTS;


    void Start()
    {
        qaArr = new SelfReport[questionGroupArr.Length];
        participant = PlayerPrefs.GetString("participant");
        group = PlayerPrefs.GetString("group");
    }

    public void SubmitAnswer()
    {
        for (int i = 0; i < qaArr.Length; i++)
        {
            qaArr[i] = ReadQuestionAndAnswer(questionGroupArr[i]);
        }

        valence = qaArr[0].Answer;
        arousal = qaArr[1].Answer;
        dominance = qaArr[2].Answer;
        timestamp = DateTime.UtcNow.ToString("yyyy-MM-dd,HH.mm.ss");
        participant = PlayerPrefs.GetString("participant");
        marker = PlayerPrefs.GetString("Marker");

        responses = participant + "," + group + "," + marker + "," + valence + "," + arousal + "," + dominance;

        // For running in Windows
        System.IO.Directory.CreateDirectory(@"Data");
        System.IO.File.WriteAllText(@"Data\" + timestamp + ".csv", responses);

        // For running in Oculus Quest
        //path = Application.persistentDataPath + "/" + timestamp + ".csv";
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