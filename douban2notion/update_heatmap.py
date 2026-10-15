import argparse
import os
import shutil
import time

from douban2notion.notion_helper import NotionHelper


def move_and_rename_file(type):
    source_path = os.path.join("./OUT_FOLDER", "notion.svg")
    target_dir = os.path.join("./OUT_FOLDER", type)
    os.makedirs(target_dir, exist_ok=True)

    timestamp = int(time.time())
    new_filename = f"{timestamp}.svg"
    target_path = os.path.join(target_dir, new_filename)

    shutil.move(source_path, target_path)
    return target_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    options = parser.parse_args()
    type = options.type

    notion_helper = NotionHelper(type)
    image_file = move_and_rename_file(type)

    if image_file:
        repository = os.environ["REPOSITORY"]
        artifact_branch = os.getenv("ARTIFACT_BRANCH", "heatmap-artifacts")
        image_path = image_file[2:]
        image_url = (
            f"https://raw.githubusercontent.com/{repository}/"
            f"{artifact_branch}/{image_path}"
        )
        heatmap_url = f"https://heatmap.malinkang.com/?image={image_url}"

        if notion_helper.heatmap_block_id:
            notion_helper.update_heatmap(
                block_id=notion_helper.heatmap_block_id,
                url=heatmap_url,
            )


if __name__ == "__main__":
    main()
