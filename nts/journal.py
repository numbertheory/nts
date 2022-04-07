#! /usr/bin/env python3
import json
import uuid
import time, datetime
import toml

def default_subject(args):
    ts = datetime.datetime.now().strftime(args.time_format)
    if args.default_subject:
        return args.default_subject.replace("$time", ts)
    else:
        return ts

def list(args):
    list_source = "{}/{}/journal.json".format(args.storage_path, args.journal)
    with open(list_source, "r") as f:
        list_posts = json.loads(f.read())

    for post in list_posts['posts']:
        print(post['journal_post_path'])

    return list_posts['posts']

def add(args):
    # Load the storage_path's json
    json_file = "{}/{}/journal.json".format(args.storage_path, args.journal)
    try:
        with open(json_file, "r") as f:
            journal = json.loads(f.read())
    except FileNotFoundError:
        print("Journal not found: {}".format(args.journal))
        print(json_file)
        return False
    # Add post to journal JSON
    millisec = time.time_ns() // 1000000
    journal_post_path = "{}/{}/post_{}.toml".format(
        args.storage_path, args.journal, millisec)
    new_post = {"id": str(uuid.uuid4()),
                "journal_post_path": journal_post_path }
    journal["posts"].append(new_post)
    with open(json_file, "w") as f:
        f.write(json.dumps(journal, indent=4, sort_keys=True))
    subject_content = args.subject
    if not subject_content:
        subject_content = default_subject(args)
    with open(journal_post_path, "w") as f:
        content = {
            "post":{
                "subject": subject_content,
                "body": args.notebody
            }
        }
        f.write(toml.dumps(content))
    return True
