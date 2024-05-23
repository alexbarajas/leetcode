import json
import copy

# The response body returned by the API
decrypted_body = {
    "id": 50,
    "text": "Here is some text that contains personal info: email@email.com",
    "obj1": {
        "obj2": {
            "text": "Email@email.com featured in deeply nested text with personal info.",
            "obj3": {
                "text1": "Nope, no personal data to see here! Foiled!",
                "text2": "I too have no personal email@email.com data - oh, shoot. Fine, here's more: 999-999-9999.",
            },
        },
    },
    "text2": "No PII to see here! Try again next time.",
    "text3": "redact everything",
}

# The indices to redact
redact_indices = {
    "$.text": [[47, 61]],
    "$.text3": [[0, 16]],
    "$.obj1.obj2.text": [[0, 14]],
    "$.obj1.obj2.obj3.text2": [
        [23, 37],
        [76, 87],
    ],
}


def redact(decrypted_body, redact_indices):
    redacted_body = copy.deepcopy(decrypted_body)  # Work on a copy of the object

    for test, ranges in redact_indices.items():
        split_test = test.split('.')[1:]  # Split and remove the initial '$'
        current = redacted_body

        # Navigate to the correct property
        for key in split_test:
            current = current[key]

        final_string = current
        adjustments = []

        # Apply redactions
        for start, end in ranges:
            adj_start = start + sum(adjustments)
            adj_end = end + sum(adjustments)
            final_string = final_string[:adj_start] + '[REDACTED]' + final_string[adj_end + 1:]
            adjustments.append(len('[REDACTED]') - (end - start + 1))

        # Set the redacted string back in the redacted_body
        current = redacted_body
        for key in split_test[:-1]:
            current = current[key]
        current[split_test[-1]] = final_string

    return redacted_body


print(json.dumps(redact(decrypted_body, redact_indices), indent=2))
