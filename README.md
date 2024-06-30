# Model Usage  
This document illustrates how to query the models hosted in hugging face spaces. Two models exist:
- Exit status model
- Follow on funding model

## Description

**Exit status model**: This Model predicts the outcome of a startup. That is, whether it ends up private, IPO or M&A.
**Follow on Funding Model**: This model predicts whether a startup will recieve future funding or not.

## Access Link

```
https://karcadan-unicorn-startups.hf.space
```

To query the Exit status model, add `/exit` to the end of the link and for the follow on funding model, add `/funding`.

## Data format

The model endpoints expects a json input as shown in the example below:

```
{
    "Funding Type": "Seed",
    "Money Raised": 1000000,
    "Organization Industries": "3D Printing",
    "Funding Stage": "Seed",
    "Region": " Middle_East_and_Africa",
    "Country": " Kenya",
    "City": "Nairobi",
    "Total Funding": 5000000,
    "Company Type": "For Profit",
    "Number of Founders": 2,
    "Number of Employees": "11-50"
}
```
For the `string` input values, the list of each unique value is in this [json file](https://github.com/xtealer/karcadan-python-ai/blob/main/feature_values.json). The model expect values explicitly on this file.

**Note** `Money Raised` and `Total Funding` should be `integers` or `floats` and not a `string`

## Output

Expect the following response:

Exit status model:

```
{
    "prediction": "Privado"
}
```
Follow on Funding model:

```
{
    "Answer": {
        "Prediction": "Funded",
        "confidence": 99
    }
}
```


