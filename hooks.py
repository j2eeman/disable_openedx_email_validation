from tutor import hooks

@hooks.ENV_PATCHES
def patch_email_validation(env_patches):
    env_patches.setdefault("common-env-features", "").append('"SKIP_EMAIL_VALIDATION": true')
    return env_patches