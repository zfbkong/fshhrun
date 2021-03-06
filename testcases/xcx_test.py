# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/xcx.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseXcx(HttpRunner):

    config = Config("微信授权登录").export(*["xcx_token"])

    teststeps = [
        Step(
            RunRequest("微信授权登录")
            .post("https://api.fanshouhou.com/business/login/wxlogin")
            .with_data({"code": "011Ss60w3SkqlV2g9r3w30Vqj20Ss60V"})
            .extract()
            .with_jmespath("headers.Authorization", "xcx_token")
            .validate()
            .assert_equal("body.code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseXcx().test_start()
