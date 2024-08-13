
# State Input
=====
{
  "employee": {
    "jobs": [
      {
        "title": "engineer",
        "salary": "2000",
        "city": "france",
        "street": "love street"
      },
      {
        "title": "cook",
        "salary": "1900",
        "city": "taipei",
        "street": "Zhong street"
      }
    ]
  },
  "version": 3
}
===== 

# InputPath
 - "$.employee"
=====
{
  "jobs": [
    {
      "title": "engineer",
      "salary": "2000",
      "city": "france",
      "street": "love street"
    },
    {
      "title": "cook",
      "salary": "1900",
      "city": "taipei",
      "street": "Zhong street"
    }
  ]
}
=====

# Parameter 
===== 
{
  "newKey": "newVal",
  "recentJob.$": "$.jobs.[0]",
  "recentJobAddr.$": "States.Format('{} {}', $.jobs[0].city, $.jobs[0].street)",
  "jobTitles.$": "States.Array($.jobs[0].title, $.jobs[1].title)",
  "salaryBase64.$": "States.Base64Encode($.jobs[0].salary)"
}
====

- result
=====
{
  "newKey": "newVal",
  "recentJob": {
    "title": "engineer",
    "salary": "2000",
    "city": "france",
    "street": "love street"
  },
  "recentJobAddr": "france love street",
  "jobTitles": [
    "engineer",
    "cook"
  ],
  "salaryBase64": "MjAwMA=="
}
=====

# Task Result 

===== 
{
  "ExecutedVersion": "$LATEST",
  "Payload": {
    "statusCode": "200",
    "body": {
      "decision": {
        "status": "hired",
        "salary": "2200"
      }
    }
  },
  "SdkHttpMetadata": {
    "HttpHeaders": {
      "Connection": "keep-alive"
    },
    "HttpStatusCode": 200
  },
  "SdkResponseMetadata": {
    "RequestId": "88fba57b-adbe-467f-abf4-daca36fc9028"
  },
  "StatusCode": 200
}  
=====

# ResultSelector (like Parameters for input)
=====
{
  "modifiedPayload": {
    "body.$": "$.Payload.body",
    "statusCode.$": "$.Payload.statusCode",
    "requestId.$": "$.SdkResponseMetadata.RequestId"
  }
}
===== 

- result
=====
{
  "modifiedPayload": {
    "body": {
      "decision": {
        "status": "hired",
        "salary": "2200"
      }
    },
    "statusCode": "200",
    "requestId": "88fba57b-adbe-467f-abf4-daca36fc9028"
  }
}
=====

# ResultPath 
 - $.myTaskResult

=====
{
  "employee": {
    "jobs": [
      {
        "title": "engineer",
        "salary": "2000",
        "city": "france",
        "street": "love street"
      },
      {
        "title": "cook",
        "salary": "1900",
        "city": "taipei",
        "street": "Zhong street"
      }
    ]
  },
  "version": 3,
  "myTaskResult": {
    "modifiedPayload": {
      "body": {
        "decision": {
          "status": "hired",
          "salary": "2200"
        }
      },
      "statusCode": "200",
      "requestId": "88fba57b-adbe-467f-abf4-daca36fc9028"
    }
  }
}
=====

# OutputPath (like InputPath for input)
 - $
=====
{
  "employee": {
    "jobs": [
      {
        "title": "engineer",
        "salary": "2000",
        "city": "france",
        "street": "love street"
      },
      {
        "title": "cook",
        "salary": "1900",
        "city": "taipei",
        "street": "Zhong street"
      }
    ]
  },
  "version": 3,
  "myTaskResult": {
    "modifiedPayload": {
      "body": {
        "decision": {
          "status": "hired",
          "salary": "2200"
        }
      },
      "statusCode": "200",
      "requestId": "88fba57b-adbe-467f-abf4-daca36fc9028"
    }
  }
}
=====

# OutputPath (like InputPath for input)
 - $.employee
=====
{
  "jobs": [
    {
      "title": "engineer",
      "salary": "2000",
      "city": "france",
      "street": "love street"
    },
    {
      "title": "cook",
      "salary": "1900",
      "city": "taipei",
      "street": "Zhong street"
    }
  ]
}
=====

# OutputPath (like InputPath for input)
 - $.myTaskResult.modifiedPayload
=====
{
  "jobs": [
    {
      "title": "engineer",
      "salary": "2000",
      "city": "france",
      "street": "love street"
    },
    {
      "title": "cook",
      "salary": "1900",
      "city": "taipei",
      "street": "Zhong street"
    }
  ]
}
=====

# State Output
=====
{
  "jobs": [
    {
      "title": "engineer",
      "salary": "2000",
      "city": "france",
      "street": "love street"
    },
    {
      "title": "cook",
      "salary": "1900",
      "city": "taipei",
      "street": "Zhong street"
    }
  ]
}
=====
