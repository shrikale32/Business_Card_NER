import {CognitoUserPool} from "amazon-cognito-identity-js";

const poolData = {
    UserPoolId: "ca-central-1_OVvFOAMBP",
    ClientId: "1kv32ob350eau1bvg1j9jlptqn"
}

export default new CognitoUserPool(poolData);